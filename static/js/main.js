document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('requirementsForm');
    const resultCard = document.getElementById('resultCard');
    const progressBar = document.querySelector('.progress-bar');
    const outputContainer = document.getElementById('outputContainer');
    const requirementsOutput = document.getElementById('requirementsOutput');
    const architectureOutput = document.getElementById('architectureOutput');
    const successMessage = document.getElementById('successMessage');
    const generateBtn = document.getElementById('generateBtn');

    function showError(message) {
        // Create or update error alert
        let errorAlert = document.getElementById('errorAlert');
        if (!errorAlert) {
            errorAlert = document.createElement('div');
            errorAlert.id = 'errorAlert';
            errorAlert.className = 'alert alert-danger alert-dismissible fade show';
            errorAlert.innerHTML = `
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                <strong>Error:</strong> <span id="errorMessage"></span>
            `;
            resultCard.querySelector('.card-body').insertBefore(errorAlert, resultCard.querySelector('.card-body').firstChild);
        }
        errorAlert.querySelector('#errorMessage').textContent = message;
        errorAlert.style.display = 'block';
    }

    function hideError() {
        const errorAlert = document.getElementById('errorAlert');
        if (errorAlert) {
            errorAlert.style.display = 'none';
        }
    }

    function updateProgress(percent) {
        progressBar.style.width = `${percent}%`;
        progressBar.setAttribute('aria-valuenow', percent);
    }

    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        // Reset UI state
        resultCard.style.display = 'block';
        outputContainer.style.display = 'none';
        successMessage.style.display = 'none';
        hideError();
        updateProgress(0);
        generateBtn.disabled = true;

        try {
            // Validate input
            const formData = new FormData(form);
            const requirements = formData.get('requirements').trim();
            if (!requirements) {
                throw new Error('Please enter your requirements');
            }

            updateProgress(20);

            // Send request
            const response = await fetch('/generate', {
                method: 'POST',
                body: formData
            });

            updateProgress(70);

            // Handle response
            const data = await response.json();
            
            if (!response.ok) {
                throw new Error(data.error || 'An unexpected error occurred');
            }

            updateProgress(100);

            // Display results
            requirementsOutput.textContent = data.requirements;
            architectureOutput.textContent = JSON.stringify(JSON.parse(data.architecture), null, 2);
            successMessage.style.display = 'block';
            outputContainer.style.display = 'block';

        } catch (error) {
            console.error('Error:', error);
            showError(error.message);
            updateProgress(0);
        } finally {
            generateBtn.disabled = false;
        }
    });
});
