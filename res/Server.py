from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from joblib import load
import re 

app = Flask(__name__)
CORS(app)


def wordopt(text):
    patterns = [
        r'\[.*?\]', r'https?://\S+|www\.\S+', r'<.*?>+',
        r'[%s]' % re.escape(string.punctuation), r'\n', r'\w*\d\w*'
    ]
    for p in patterns:
        text = re.sub(p, "", text)
    text = re.sub(r'\W', " ", text.lower())
    return text


def label(n):
    if n == 0:
        return "This News is Fake"
    elif n == 1:
        return "This News is True"

def testing(news, model):
    newsTest = {"text": [news]}
    models = {
        'lr': load('LogisticRegression.model'),
        'dt': load('DecisionTree.model'),
        'rf': load('randomforest.model')
    }
    vec = load('vectorizer.jb')

    defTest = pd.DataFrame(newsTest)
    defTest["text"] = defTest["text"].apply(wordopt)
    xTest = defTest["text"]
    xvTest = vec.transform(xTest)

    model = models.get(model)
    predict = model.predict(xvTest)
    
    return label(predict[0])

@app.route('/process', methods=['POST'])
def process_news():
    data = request.json.get('data')
    model = request.json.get('model')
    result = testing(data, model)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
