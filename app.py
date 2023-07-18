#flask_app
from flask import Flask, render_template, request
import joblib
import pickle

app = Flask(__name__)

# load the model
with open('model.pkl','rb') as f:
    model = pickle.load(f)
with open('vectorizer.pkl','rb') as f:
    vectorizer = pickle.load(f)
with open('mlb.pkl','rb') as f:
    mlb = pickle.load(f)

@app.route('/ping', methods=['GET'])
def ping():
    return {"message":"Hi! I'm working"}

@app.route('/predict', methods=['POST'])
def predict():
    print(request)
    data = request.get_json()
    print('Data', data)
    question = data['question']
    print('Question',question)
    features = vectorizer.transform([question])
    tags = model.predict(features)
    tags = mlb.inverse_transform(tags)
    return tags

if __name__ == '__main__':
    app.run(debug=True)
