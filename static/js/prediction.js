document.addEventListener('DOMContentLoaded', function () {
    const stateSelect = document.getElementById('state-select');
    const municipalitySelect = document.getElementById('municipality-select');
    const municipalityWrapper = document.getElementById('municipality-wrapper');

    stateSelect.addEventListener('change', function () {
        const selectedState = this.value;

        // Clear and disable municipality select if no state is chosen
        municipalitySelect.innerHTML = '<option value="">-- Select Municipality --</option>';
        municipalitySelect.disabled = true;
        municipalityWrapper.style.display = 'none';

        if (selectedState) {
            // Show a loading state
            municipalitySelect.innerHTML = '<option value="">Loading...</option>';
            municipalityWrapper.style.display = 'block';
            municipalitySelect.disabled = false;
            
            // Fetch the municipalities for the selected state
            fetch(`/get_municipalities/${selectedState}`)
                .then(response => response.json())
                .then(data => {
                    // Clear loading and populate with new options
                    municipalitySelect.innerHTML = '<option value="">-- Select Municipality --</option>';
                    data.forEach(function (municipality) {
                        const option = new Option(municipality, municipality);
                        municipalitySelect.add(option);
                    });
                })
                .catch(error => {
                    console.error('Error fetching municipalities:', error);
                    municipalitySelect.innerHTML = '<option value="">Error loading data</option>';
                });
        }
    });
});