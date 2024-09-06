from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    data = request.json
    print("Received data:", data)
    return jsonify(status="success"), 200

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000)