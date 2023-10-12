from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from cnnClassifier.utils.comman import decodeImage
from cnnClassifier.pipeline.prediction import PredictionPipeline

os.putenv('LANG','en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UFT-8')

app = Flask(__name__)
CORS(app)


class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifire = PredictionPipeline(self.filename)
        

@app.route("/", methods=['GET'])
def home():
    return render_template('index.html')


@app.route("/train", methods = ['GET','POST'])
def trainRoute():
    os.system("python main.py")
    #os.system("dvc repro")
    return "Training done successfully !!"

@app.route("/predict", methods = ['POST'])
def predictRoute():
    image = request.json['image']
    decodeImage(image, clApp.filename)
    result = clApp.classifire.predict()
    return jsonify(result)


if __name__ == "__main__":
    clApp = ClientApp()
    
    app.run(host='0.0.0.0', port=8080) #for aws
           
            
    