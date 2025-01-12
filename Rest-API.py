from flask import Flask, jsonify

# Instantiate Flask app
app = Flask(__name__)

# Define main route (endpoint)
@app.route('/api/hello', methods=['GET'])
def hola_mundo():
    return jsonify({
        "message": "Hello World",
        "status": "success"
    })

# Entry point to run the app
if __name__ == '__main__':
    # Specify port (example: 8080)
    app.run(debug=True, host='0.0.0.0', port=8080)
