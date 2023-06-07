from flask import Flask, render_template, request
import pyqrcode
import png
from pyqrcode import QRCode
from random_filename import random_filename
from qr_model import Data_table

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.form['qrdata']
    qr = pyqrcode.create(data)
    qr.png('static/qr.png', scale=8)
    file_name=random_filename()
    qr.png(file_name[0],scale=8)
    qr_data_model=Data_table()
    qr_data_model.add_data(data,file_name[1])
    qr_data_model.close()
    return render_template('generate.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/qrcodes')
def qrcodes():
    qr_code_model=Data_table()
    result=qr_code_model.get_ten()
    qr_code_model.close()
    if result is None:
        result=[]
    return render_template("qrcodes.html",result=result)

if __name__ == '__main__':
    app.run(debug=True,port=5001)
