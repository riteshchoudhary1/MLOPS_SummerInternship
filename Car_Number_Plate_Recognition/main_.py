from flask import Flask,render_template,flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from logic import detectNumberPlate,get_vehicle_info
from flask import jsonify
import json, os
from os.path import join, dirname, realpath

app = Flask(__name__)

d1={'Description': 'MERCEDES-BENZ CLA CLASS CLA 45 AMG COUPE',
 'RegistrationYear': '2014',
 'CarMake': {'CurrentTextValue': 'MERCEDES-BENZ'},
 'CarModel': {'CurrentTextValue': 'CLA CLASS'},
 'Variant': 'CLA 45 AMG COUPE',
 'EngineSize': {'CurrentTextValue': '1991'},
 'MakeDescription': {'CurrentTextValue': 'MERCEDES-BENZ'},
 'ModelDescription': {'CurrentTextValue': 'CLA CLASS'},
 'NumberOfSeats': {'CurrentTextValue': '5'},
 'VechileIdentificationNumber': 'WDD1173522N056045',
 'EngineNumber': '13398080004697',
 'FuelType': {'CurrentTextValue': 'Petrol'},
 'RegistrationDate': '13/06/2014',
 'Owner': '',
 'Fitness': '',
 'Insurance': '',
 'PUCC': '',
 'VehicleType': 'MOTOR CAR(LMV)',
 'Location': 'DY.DIR.ZONAL OFFICE,DELHI NORTH WEST,WAZIRPUR',
 'ImageUrl': 'http://www.carregistrationapi.in/image.aspx/@TUVSQ0VERVMtQkVOWiBDTEEgQ0xBU1MgQ0xBIDQ1IEFNRyBDT1VQRQ=='}

#print(app.config['UPLOAD_FOLDER'])
UPLOAD_FOLDER = join(dirname(realpath(__file__)), 'static/upimage/')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    print(request.method)
    try:
        print("1")
        file = request.files['image_file']
        print("2")
        if file.filename == '':
            return redirect(url_for("up"))
        print("3")
        if file and allowed_file(file.filename):
            print(file.filename+"  hii")
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('fecthdetails',filename1=filename))
    except Exception as e :
        print(e)
    return "Error"

@app.route("/")
def up():
    return render_template("index.html")


@app.route("/result/<filename1>")
def fecthdetails(filename1):
  res= detectNumberPlate(filename1)
  final1=get_vehicle_info(res[0])
  return render_template("result.html",resultDict=final1, photo2=res[1])

if __name__ == "__main__":
  app.run(debug=True)