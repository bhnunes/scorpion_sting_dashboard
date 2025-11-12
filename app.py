from flask import Flask, render_template, request, jsonify, redirect, url_for, session
import pandas as pd
import joblib
import plotly.express as px
import plotly.graph_objects as go
import json
import plotly
import numpy as np
from datetime import date
from epiweeks import Week # <-- New import
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.secret_key = os.getenv('SECRET_KEY', 'your_very_secret_and_random_string')

df = pd.read_parquet('data\\scorpion_data.parquet')

# Load the locations dataset for the prediction form
df_locations = pd.read_parquet('data\\locations.parquet')

# Professional Step: Clean up column names immediately after loading
df_locations.rename(columns={
    'Nome_UF': 'state',
    'Nome_Município': 'municipality',
    ' POPULAÇÃO ESTIMADA ': 'population' # Handles leading/trailing spaces
}, inplace=True)

df_locations['population'] = df_locations['population'].str.replace('.', '').astype(int)

# Load the prediction model
model = joblib.load('models\\scorpion_model.joblib')


# --- Helper Function (provided in the prompt) ---
def get_epi_week_features(iso_date_string):
    """
    Calculates epidemiological features from a standard date.
    """
    dt = date.fromisoformat(iso_date_string)
    epi_week_obj = Week.fromdate(dt)
    epi_week = epi_week_obj.week

    week_sin = np.sin(2 * np.pi * epi_week / 52)
    week_cos = np.cos(2 * np.pi * epi_week / 52)

    return {
        'epidemiological_week': epi_week,
        'week_sin': week_sin,
        'week_cos': week_cos
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    # --- Data Processing for the New Schema ---
    df_processed = df.copy()
    df_processed['data_acidente'] = pd.to_datetime(df_processed['data_acidente'])
    df_processed['year'] = df_processed['data_acidente'].dt.year

    # --- Calculations based on the new, raw data ---
    total_accidents = len(df_processed)
    total_deaths = df_processed['obito'].sum()
    top_10_df = df_processed['municipio'].value_counts().nlargest(10).reset_index()
    top_10_df.columns = ['name', 'number_of_accidents']
    top_locations = top_10_df.to_dict('records')
    time_series_df = df_processed.groupby('year').size().reset_index(name='number_of_accidents')
    time_series_df = time_series_df.sort_values('year')

    # --- Chart Generation (with new customizations) ---
    fig = px.line(time_series_df, 
                  x='year', 
                  y='number_of_accidents', 
                  title='Acidentes com Escorpiões no Brasil',
                  labels={'year': 'Ano', 'number_of_accidents': 'Número de Acidentes'}) # <-- TRANSLATED LABELS
    
    # --- Customizations for Color and Layout ---

    # 1. Change the line color to red
    # You can use color names ('red', 'blue') or hex codes ('#FF0000').
    fig.update_traces(line=dict(color='red')) # <-- ADDED THIS LINE FOR RED COLOR

    # 2. Make the chart look cleaner
    fig.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        font_color='#333',
        title_x=0.5
    )
    
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    # --- Pass all calculated data to the template ---
    return render_template('dashboard.html', 
                           graphJSON=graphJSON,
                           total_accidents=f'{total_accidents:,}',
                           total_deaths=f'{total_deaths:,}',
                           top_locations=top_locations)

# --- Prediction Route (Corrected Logic) ---
@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    # --- POST Request Logic (Process Form) ---
    if request.method == 'POST':
        # 1. Get user inputs from the form
        selected_municipality = request.form.get('municipality')
        selected_state = request.form.get('state')
        prediction_date = request.form.get('prediction_date')

        # 2. Get location features (lat, lon, pop)
        location_data = df_locations[
            (df_locations['state'] == selected_state) & 
            (df_locations['municipality'] == selected_municipality)
        ].iloc[0]
        
        lat = location_data['latitude']
        lon = location_data['longitude']
        pop = location_data['population']

        # 3. Get epidemiological features
        epi_features = get_epi_week_features(prediction_date)

        # 4. Assemble the feature vector
        features_df = pd.DataFrame([{
            'longitude': lon, 'latitude': lat, 'population': pop,
            'epidemiological_week': epi_features['epidemiological_week'],
            'week_sin': epi_features['week_sin'], 'week_cos': epi_features['week_cos']
        }])

        # 5. Run prediction
        probability = model.predict_proba(features_df)[:, 1][0]
        
        # 6. Store the result and user input in the session
        session['prediction_result'] = {
            'probability': f'{probability * 100:.2f}%',
            'municipality': selected_municipality,
            'state': selected_state
        }
        session['user_input'] = request.form

        # 7. Redirect to the same page (this will be a GET request)
        return redirect(url_for('prediction'))

    # --- GET Request Logic (Handles BOTH initial load AND post-redirect load) ---
    # This block now runs for any GET request.
    
    # Retrieve the result and user input from the session, if they exist.
    # .pop() gets the item and removes it, so it's only shown once.
    result = session.pop('prediction_result', None)
    user_input = session.pop('user_input', None)

    # Always get the list of states for the dropdown.
    states = sorted(df_locations['state'].unique().tolist())
    
    # Render the page. If 'result' is None (initial visit), it shows an empty form.
    # If 'result' has data (after redirect), it shows the result.
    return render_template('prediction.html', states=states, result=result, user_input=user_input)
    

    # --- NEW API Endpoint for Dynamic Dropdowns ---
@app.route('/get_municipalities/<state>')
def get_municipalities(state):
    """
    API endpoint that returns a list of municipalities for a given state.
    Called by the JavaScript on the prediction page.
    """
    municipalities = df_locations[df_locations['state'] == state]['municipality'].tolist()
    return jsonify(sorted(municipalities))

if __name__ == '__main__':
    app.run(debug=True)