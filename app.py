from flask import Flask, render_template, request
import pickle
import numpy as np
import os
from src.datascience.pipelines.prediction_piplline import predictionPipline


app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/train", methods=["GET"])
def training():
    os.system("python main.py")
    return "Training done"

@app.route("/predict", methods=["POST", "GET"])
def predict():

    if request.method == "GET":
        try:
            fixed_acidity = float(request.args.get("fixed_acidity"))
            volatile_acidity = float(request.args.get("volatile_acidity"))
            citric_acid = float(request.args.get("citric_acid"))
            residual_sugar = float(request.args.get("residual_sugar"))
            chlorides = float(request.args.get("chlorides"))
            free_sulfur_dioxide = float(request.args.get("free_sulfur_dioxide"))
            total_sulfur_dioxide = float(request.args.get("total_sulfur_dioxide"))
            density = float(request.args.get("density"))
            pH = float(request.args.get("pH"))
            sulphates = float(request.args.get("sulphates"))
            alcohol = float(request.args.get("alcohol"))


            data=[
                fixed_acidity,
                volatile_acidity,
                citric_acid,
                residual_sugar,
                chlorides,
                free_sulfur_dioxide,
                total_sulfur_dioxide,
                density,
                pH,
                sulphates,
                alcohol
            ]
            data = np.array(data).reshape(1, 11)
            obj=predictionPipline()
            pred=obj.predict(data)
            return render_template("result.html", prediction=str(pred))
        except Exception as e:
            return "some thing went wrong, please try again later"
        
    else:
        return render_template("index.html", message="Please provide input values for prediction.")


if __name__ == "__main__":
    app.run( host="0.0.0.0", port=5000)

