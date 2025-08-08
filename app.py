from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This allows React frontend to access this API

# Optional: This route is just for testing in browser
@app.route('/')
def home():
    return "Fake News Detector API Running"

# This is your main prediction route
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    news = data.get('news', '')

    # Your ML model prediction logic here
    # For now, let's return a dummy result
    if "fake" in news.lower():
        result = "Fake"
    else:
        result = "Real"

    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(debug=True)
