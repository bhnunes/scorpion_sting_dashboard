# 🦂 Dashboard Preditivo de Escorpionismo no Brasil

![GitHub repo size](https://img.shields.io/github/repo-size/bhnunes/scorpion_sting_dashboard?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/bhnunes/scorpion_sting_dashboard?style=for-the-badge)
![GitHub top language](https://img.shields.io/github/languages/top/bhnunes/scorpion_sting_dashboard?style=for-the-badge)


## 📄 Sobre o Projeto

O escorpionismo é um problema de saúde pública crescente e negligenciado no Brasil. A vigilância epidemiológica atual opera de forma predominantemente reativa, agindo apenas após a consolidação de surtos.

Este projeto visa mudar esse paradigma, apresentando uma **plataforma de vigilância preditiva** desenvolvida como uma aplicação web interativa. A ferramenta foi projetada para ser um recurso proativo, apoiando gestores de saúde na tomada de decisão e permitindo a alocação otimizada e preventiva de recursos.

A plataforma integra dados do **Sistema de Informação de Agravos de Notificação (SINAN)**, dados demográficos e geográficos para fornecer insights valiosos através de duas funcionalidades principais:

1.  **Dashboard de Monitoramento:** Uma visão geral e atualizada da situação do escorpionismo no país.
2.  **Ferramenta de Previsão:** Um modelo de Machine Learning que calcula o risco de acidentes para um local e data específicos.

_Este trabalho foi desenvolvido como parte do Projeto Integrador em Computação da Universidade Virtual do Estado de São Paulo (UNIVESP)._

---

## ✨ Funcionalidades

*   **📊 Dashboard Interativo:**
    *   **KPIs (Indicadores-Chave):** Visualização rápida do número total de acidentes e óbitos registrados.
    *   **Ranking Top 10:** Tabela com os 10 municípios que apresentam o maior número de acidentes.
    *   **Série Temporal:** Gráfico interativo que mostra a evolução dos acidentes ao longo dos anos.

*   **🤖 Ferramenta de Previsão de Risco:**
    *   **Seleção Dinâmica:** Escolha um Estado (UF) e a lista de municípios é atualizada automaticamente.
    *   **Entrada de Dados Simplificada:** O usuário informa apenas o local e a data desejada.
    *   **Inferência em Tempo Real:** O modelo preditivo retorna a probabilidade de risco de acidente para a localidade.

*   **🌐 Interface Responsiva e Amigável:** Projetado para ser acessível e fácil de usar.

---

## 🚀 Tecnologias Utilizadas

A plataforma foi construída utilizando uma stack moderna de tecnologias de desenvolvimento web e ciência de dados.

| Componente              | Tecnologia                                                                                               |
| ----------------------- | -------------------------------------------------------------------------------------------------------- |
| **Backend**             | ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white) |
| **Análise de Dados**    | ![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)                                                                                                |
| **Machine Learning**    | ![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white) LightGBM, Joblib, Epiweeks |
| **Visualização de Dados** | ![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)                                                                                                  |
| **Frontend**            | ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white) ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black) |
| **Servidor de Produção**| Nginx, Waitress                                                                                         |

---

## 🏁 Como Executar o Projeto Localmente

Para executar esta aplicação em sua máquina local, siga os passos abaixo.

### Pré-requisitos

*   Python 3.9+
*   Git

### Instalação

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git
    ```

2.  **Navegue até o diretório do projeto:**
    ```bash
    cd SEU-REPOSITORIO
    ```

3.  **Crie e ative um ambiente virtual:**
    ```bash
    # Para Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Para macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

4.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Adicione os arquivos de dados e modelo:**
    É crucial que você coloque os arquivos necessários nas pastas corretas para que a aplicação funcione. Crie as pastas se elas não existirem.
    *   `data/scorpion_data.parquet`
    *   `data/locations.parquet`
    *   `models/scorpion_model.joblib`

6.  **Execute a aplicação:**
    ```bash
    python app.py
    ```

7.  **Acesse no seu navegador:**
    Abra seu navegador e vá para `http://127.0.0.1:5000`

---

## 📁 Estrutura de Arquivos

```
/scorpion_sting_dashboard
|
|-- app.py                  # Lógica principal da aplicação Flask
|-- requirements.txt        # Lista de dependências Python
|-- .gitignore              # Arquivos e pastas ignorados pelo Git
|
|-- /data/
|   |-- scorpion_data.parquet # Dados para o dashboard
|   |-- locations.parquet     # Dados para a ferramenta de previsão
|
|-- /models/
|   |-- scorpion_model.joblib # Modelo de Machine Learning treinado
|
|-- /static/
|   |-- /css/
|   |   |-- style.css       # Folha de estilos principal
|   |-- /js/
|   |   |-- prediction.js   # Lógica interativa da página de previsão
|   |-- /images/
|       |-- scorpion.jpg      # Imagem da página inicial
|
|-- /templates/
|   |-- index.html          # Página inicial
|   |-- dashboard.html      # Página do dashboard
|   |-- prediction.html     # Página da ferramenta de previsão
```

---

## 👨‍💻 Autores

Este projeto foi desenvolvido por:
*   Bruno Henrique Nunes
*   Camila dos Santos Marcolino
*   Fernando Pires Barbosa
*   João Luiz de Andrade
*   Jose Donizete de Lima
*   Melvin Fernando Silveira
*   Renan Cermaria Bressan
*   Simone Simoso de Moraes

---

## 🙏 Agradecimentos

*   À **Universidade Virtual do Estado de São Paulo (UNIVESP)** pela oportunidade de desenvolver este projeto.
*   Ao **Sistema de Informação de Agravos de Notificação (SINAN)**, por disponibilizar os dados que são a base desta análise.

---

## 📄 Licença

Este projeto é distribuído sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
