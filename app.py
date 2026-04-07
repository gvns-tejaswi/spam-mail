from flask import Flask, request, render_template
import joblib

model = joblib.load('spam_detection_model.pkl')
vectorizer = joblib.load('count_vectorizer.pkl')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict')
def predict():
    text = request.args.get('text')
    data = vectorizer.transform([text])
    result = model.predict(data)

    if result[0] == 1:
        return "Spam 🚨"
    else:
        return "Ham ✅"

app.run(host='0.0.0.0', port=5000)