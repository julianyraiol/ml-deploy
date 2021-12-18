from flask import Flask, request, jsonify
from flask_basicauth import BasicAuth

# import pandas as pd
import numpy as np
from predict_model import prediction
import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = os.getenv("BASIC_AUTH_USERNAME")
app.config['BASIC_AUTH_PASSWORD'] = os.getenv("BASIC_AUTH_PASSWORD")

basic_auth = BasicAuth(app)

columns = ["Gender", "Married", "ApplicantIncome", "LoanAmount", "Credit_History"]

@app.route("/score", methods=['POST'])
@basic_auth.required
def get_score():
    data = request.get_json()

    payload = np.array(data[col] for col in columns)

    result = prediction(data["Gender"], data["Married"], data["ApplicantIncome"], data["LoanAmount"], data["Credit_History"]) 

    return result

# Rota padrão
@app.route('/')
def home():
    return 'API de Consulta de Crédito'

# Subir a API
app.run(debug=True)
