document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('requirementsForm');
    const resultCard = document.getElementById('resultCard');
    const progressBar = document.querySelector('.progress-bar');
    const outputContainer = document.getElementById('outputContainer');
    const requirementsOutput = document.getElementById('requirementsOutput');
    const architectureOutput = document.getElementById('architectureOutput');
    const successMessage = document.getElementById('successMessage');
    const generateBtn = document.getElementById('generateBtn');

    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        // Reset and show progress
        resultCard.style.display = 'block';
        outputContainer.style.display = 'none';
        progressBar.style.width = '0%';
        generateBtn.disabled = true;

        try {
            const formData = new FormData(form);
            progressBar.style.width = '20%';

            const response = await fetch('/generate', {
                method: 'POST',
                body: formData
            });

            progressBar.style.width = '70%';

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            progressBar.style.width = '100%';

            // Display results
            requirementsOutput.textContent = data.requirements;
            architectureOutput.textContent = JSON.stringify(JSON.parse(data.architecture), null, 2);
            successMessage.style.display = 'block';
            outputContainer.style.display = 'block';

        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred while generating code. Please try again.');
        } finally {
            generateBtn.disabled = false;
        }
    });
});
