# app.py
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
    text = text.lower()
    text = re.sub('\[.*?\]', "", text)
    text = re.sub("\\W", " ", text)
    text = re.sub("https?:://\S+|www\.\S+", "", text)
    text = re.sub("<.*?>+", "", text)
    text = re.sub("[%s]" % re.escape(string.punctuation), "", text)
    text = re.sub("\n", "", text)
    text = re.sub("\w*\d\w*", "", text)
    return text

def output_label(n):
    if n == 0:
        return "This News is Fake"
    elif n == 1:
        return "This News is True"

def manual_testing(news, model):
    testing_news = {"text": [news]}
    models = {
        'lr': load('LogisticRegression.model'),
        'dt': load('DecisionTree.model'),
        'rf': load('randomforest.model')
    }
    vectorization = load('vectorizer.jb')

    new_def_test = pd.DataFrame(testing_news)
    new_def_test["text"] = new_def_test["text"].apply(wordopt)
    new_x_test = new_def_test["text"]
    new_xv_test = vectorization.transform(new_x_test)

    model = models.get(model)
    predict = model.predict(new_xv_test)
    
    return output_label(predict[0])

@app.route('/process', methods=['POST'])
def process_news():
    data = request.json.get('data')
    model = request.json.get('model')
    result = manual_testing(data, model)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
