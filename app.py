from flask import Flask, render_template, request, send_file
from Parameters import Parameters
import os
from Image import countDots

app = Flask(__name__)
params = Parameters()


@app.route('/')
def index():
    return render_template('upload.html')


@app.route('/uploader', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        path = params.tmpImg

        f.save(path)
        dot_count = countDots(path)
        os.remove(path)

        return str(dot_count)


@app.route('/debug', methods=['GET'])
def download_file():
    file = params.debugImg
    if os.path.exists(file):
        return send_file(file, as_attachment=True)
    else:
        return 'No download available'


if __name__ == '__main__':
    app.run()
