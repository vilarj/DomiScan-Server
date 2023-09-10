from flask import Flask, render_template, request, send_file
from Parameters import *
import os
import Image

app = Flask(__name__)
params = Parameters()

@app.route('/')
def index():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['POST'])
def uploadFile():
   if request.method == 'POST':
      f = request.files['file']
      path = params.tmpImg
      
      f.save(path)
      dotCount = Image.countDots(path)
      os.remove(path)

      return str(dotCount)

@app.route('/debug', methods = ['GET'])
def downloadFile():
   file = params.debugImg
   if os.path.exists(file):
      return send_file(file, as_attachment=True)
   else:
      return 'No download available'
   
if __name__ == '__main__':
   app.run()