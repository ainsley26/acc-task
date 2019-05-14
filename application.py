from flask import Flask, jsonify, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
from classifier import *

# app settings
UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['csv'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# not actually very secret... from online cause can't copy paste from terminal on laptop
app.config['SECRET_KEY'] = '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'

# load default classifier
clf = Classifier('name_gender.csv', 8)


#
## Routes
#

@app.route('/')
def root():
    return '''
    <!doctype html>
    <p>go to 'predict/<name>' for a gender prediction result as JSON</p>
    <p>go to 'update' to load new CSV</p>
    '''

# from http://flask.pocoo.org/docs/1.0/patterns/fileuploads/ with changes
@app.route('/update', methods=['GET', 'POST'])
def upload_file():
    res = {"updated": "false"}

    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return jsonify(res)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return jsonify(res)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print(' * Updating classifier with new CSV')
            clf = Classifier(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            res['updated'] = 'true'
            res['trn_score'] = clf.trn_score
            res['tst_score'] = clf.tst_score
            return jsonify(res)
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    <p>go to 'predict/<name>' for a gender prediction result as JSON</p>
    '''

# from http://flask.pocoo.org/docs/1.0/patterns/fileuploads/
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/predict/<name>')
def predict_gender(name):
    res = 'M' if clf.predict_name(name) == 0 else 'F'
    #return f'{name} {res[0]}'
    json = {'name': name, 'gender': res}
    return jsonify(json)

if __name__ == '__main__':
    if os.getenv('CLF_DOCKER', False):
        app.run(host='0.0.0.0', port=80, debug=False)
    else:
        app.run(host='0.0.0.0', debug=False)
