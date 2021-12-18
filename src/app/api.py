from flask import Flask, request, jsonify
from flask_basicauth import BasicAuth

# import pandas as pd

import numpy as np
import pickle
import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = os.getenv("BASIC_AUTH_USERNAME")
app.config['BASIC_AUTH_PASSWORD'] = os.getenv("BASIC_AUTH_PASSWORD")

basic_auth = BasicAuth(app)

columns = ["Gender", "Married", "ApplicantIncome", "LoanAmount", "Credit_History"]

def load_model(filename = "classifier.pkl"):
    pickle_in = open(filename, 'rb')
    return pickle.load(pickle_in) 

classifier = load_model("../../models/classifier.pkl")

@app.route("/score", methods=['POST'])
@basic_auth.required
def get_score():
    data = request.get_json()

    payload = np.array(data[col] for col in columns)

    return data

# Rota padrão
@app.route('/')
def home():
    return 'API de Consulta de Crédito'

# Subir a API
app.run(debug=True)
