"""
BACKEND for ft.huhncares.de
"""
from flask import Flask, render_template, send_from_directory, request
from werkzeug.utils import secure_filename
import os
import random

app = Flask(__name__)

app.config['MAX_CONTENT_LENGTH'] = 2000 * 1000 * 1000
app.config['UPLOAD_FOLDER'] = "uploads"

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

def format_filename(filename):
    if "." in filename:
        return f"{filename.split('.')[0]}-{random.randint(0, 10000000000)}.{filename.split('.')[-1]}"
    else:
        return f"{filename}-{random.randint(0, 10000000000)}"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.html', error="No file selected")
        file = request.files['file']
        if file.filename == '':
            return render_template('index.html', error="No file selected")
        try:
            filename = secure_filename(format_filename(file.filename))
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template('upload.html', link=f"https://ft.huhncares.de/download?file={filename}")
        except Exception as e:
            return render_template('index.html', error="Task failed successfully.")
    return render_template('index.html')
    
@app.route('/download', methods=['GET', "POST"])
def download():
    file = None
    if request.method == 'GET':
        file = request.args.get('file')
    return render_template('download.html', file=file)

@app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download_file(filename):    
    full_path = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'])
    return send_from_directory(full_path, filename, as_attachment=True)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(413)
def request_entity_too_large(e):
    return render_template('413.html'), 413

if __name__ == '__main__':
    app.run(debug=True, port=1337)