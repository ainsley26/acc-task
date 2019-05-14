from flask import Flask, jsonify
from classifier import *

app = Flask(__name__)

# load default classifier
clf = Classifier('name_gender.csv', 8)


@app.route('/')
def root():
    return f'Hello world!'

@app.route('/predict/<name>')
def predict_gender(name):
    res = 'M' if clf.predict_name(name) == 0 else 'F'
    #return f'{name} {res[0]}'
    json = {'name': name, 'gender': res}
    return jsonify(json)

@app.route('/update', methods=["POST"])
def update_training_data():
    pass

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=80, debug=False)
    app.run(host='0.0.0.0', debug=False)
