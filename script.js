document.getElementById('submit-btn').addEventListener('click', async () => {
    const jsonInput = document.getElementById('json-input').value;
    const errorMessage = document.getElementById('error-message');
    const responseContainer = document.getElementById('response-container');
    const filteredResponse = document.getElementById('filtered-response');

    errorMessage.textContent = ''; // Clear previous error message
    filteredResponse.innerHTML = ''; // Clear previous response

    let requestData;

    try {
        // Parse the JSON input
        requestData = JSON.parse(jsonInput);
    } catch (error) {
        errorMessage.textContent = 'Invalid JSON format.';
        return;
    }

    try {
        const response = await fetch('http://127.0.0.1:5000/bfhl', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(requestData),
        });

        const responseData = await response.json();

        // Display the response based on checkboxes
        const showAlphabets = document.getElementById('show-alphabets').checked;
        const showNumbers = document.getElementById('show-numbers').checked;
        const showHighestLower = document.getElementById('show-highest-lower').checked;

        filteredResponse.innerHTML += '<h3>Filtered Response:</h3>';

        if (showAlphabets) {
            filteredResponse.innerHTML += '<p><strong>Alphabets:</strong> ' + JSON.stringify(responseData.alphabets) + '</p>';
        }
        if (showNumbers) {
            filteredResponse.innerHTML += '<p><strong>Numbers:</strong> ' + JSON.stringify(responseData.numbers) + '</p>';
        }
        if (showHighestLower) {
            filteredResponse.innerHTML += '<p><strong>Highest Lowercase Alphabet:</strong> ' + JSON.stringify(responseData.highest_lowercase_alphabet) + '</p>';
        }
    } catch (error) {
        errorMessage.textContent = 'Error: ' + error.message;
    }
});
