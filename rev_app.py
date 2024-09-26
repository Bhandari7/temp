# from flask import Flask, render_template

# from pprint import pprint
# import json

# with open('config.json', 'r') as f:
#     params = json.load(f)['params']

# pprint(params)



# app = Flask(__name__)


# ### Fetch data from folder, all file name
# @app.route("")





### Post data on contact

from flask import Flask, render_template, redirect, request
import os

app = Flask(__name__)

# Configure the upload folder and allowed extensions
UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Function to check if a file is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    data = ['Option 1', 'Option 2', 'Option 3', 'Option 4']
    selected_option = None
    uploaded_file_name = None

    if request.method == 'POST':
        selected_option = request.form.get('optionsss')

    return render_template('test.html', data=data, selected_option=selected_option)

@app.route('/1', methods=['GET', 'POST'])
def index2():
    uploaded_file_name = None

    if request.method == 'POST':

        # Check if the POST request has a file
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']

        # If no file is selected, return without uploading
        if file.filename == '':
            return 'No selected file'
        
        # If file is allowed, save it and store its name to display
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            uploaded_file_name = filename
        
    return render_template('test.html', uploaded_file_name=uploaded_file_name)


if __name__ == '__main__':
    app.run(debug=True)
