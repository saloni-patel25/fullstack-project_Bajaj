from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS  # Import CORS
import base64

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/bfhl', methods=['POST'])
def handle_post():
    data = request.json
    if not data:
        return jsonify({"is_success": False, "error": "Invalid JSON"}), 400

    # Process data
    user_id = "saloni_patel_12102003"  # Replace with actual logic
    email = "sp8655@srmist.edu.in"  # Example email
    roll_number = "RA2111003011422"  # Example roll number

    # Separate numbers and alphabets
    numbers = [item for item in data.get("data", []) if item.isdigit()]
    alphabets = [item for item in data.get("data", []) if item.isalpha()]

    # Find the highest lowercase alphabet
    highest_lowercase_alphabet = [max(filter(str.islower, alphabets), default=None)]

    # File handling
    file_valid = False
    file_mime_type = None
    file_size_kb = None

    if 'file_b64' in data:
        try:
            file_data = base64.b64decode(data['file_b64'])
            file_valid = True
            file_size_kb = len(file_data) / 1024  # Convert bytes to KB
            file_mime_type = "image/png"  # Replace with actual MIME type
        except Exception as e:
            file_valid = False

    response = {
        "is_success": True,
        "user_id": user_id,
        "email": email,
        "roll_number": roll_number,
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": highest_lowercase_alphabet if highest_lowercase_alphabet[0] else [],
        "file_valid": file_valid,
        "file_mime_type": file_mime_type,
        "file_size_kb": file_size_kb
    }
    
    return jsonify(response)

@app.route('/bfhl', methods=['GET'])
def handle_get():
    return jsonify({"operation_code": 1}), 200

@app.route('/', methods=['GET'])
def serve_index():
    return send_from_directory('static', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
