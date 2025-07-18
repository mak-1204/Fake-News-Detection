from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests from Chrome extension

# Load model and vectorizer
with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)
with open('svm_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return "Fake News Detector Backend is Running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        text = data['text']

        # Vectorize input
        text_vector = vectorizer.transform([text])
        prediction = model.predict(text_vector)[0]

        # Return JSON response
        return jsonify({'prediction': int(prediction)})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
