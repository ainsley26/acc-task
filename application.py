from flask import Flask, jsonify
import classifier as cs

app = Flask(__name__)

@app.route('/')
def root():
    return f'Hello world!'

@app.route('/predict/<name>')
def predict_gender(name):
    res = 'M' if cs.predict_name(name) == 0 else 'F'
    #return f'{name} {res[0]}'
    json = {'name': name, 'gender': res}
    return jsonify(json)

if __name__ == '__main__':
    app.run(debug=False)
