import pickle
import requests
import streamlit as st
from requests.auth import HTTPBasicAuth
import os
import json

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
 
API_URL = "https://ml-api-phn4j6lmdq-uc.a.run.app"
BASIC_AUTH_USERNAME = os.getenv("BASIC_AUTH_USERNAME")
BASIC_AUTH_PASSWORD = os.getenv("BASIC_AUTH_PASSWORD")

# defining the function which will make the prediction using the data which the user inputs 
def prediction(Gender, Married, ApplicantIncome, LoanAmount, Credit_History):   
 
    # Pre-processing user input    
    if Gender == "Masculino":
        Gender = 0
    else:
        Gender = 1
 
    if Married == "Solteiro":
        Married = 0
    else:
        Married = 1
 
    if Credit_History == "Com dividas":
        Credit_History = 0
    else:
        Credit_History = 1  
 
    LoanAmount = LoanAmount / 1000

    data = {
        "Gender": Gender,
        "Married": Married,
        "ApplicantIncome": ApplicantIncome,
        "LoanAmount": LoanAmount,
        "Credit_History": Credit_History
    }

    prediction = requests.post(API_URL + '/score', json=data)
     
    if prediction == 0:
        pred = 'Rejected'
    else:
        pred = 'Approved'
    return pred
      
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Consulta de emprestimo</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    Gender = st.selectbox('Gender',("Masculino","Feminino"))
    Married = st.selectbox('Marital Status',("Solteiro","Casado")) 
    ApplicantIncome = st.number_input("Renda Mensal") 
    LoanAmount = st.number_input("Valor Emprestimo")
    Credit_History = st.selectbox('Credit_History',("Com dividas","Sem dividas"))
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        
        result = prediction(Gender, Married, ApplicantIncome, LoanAmount, Credit_History) 
        st.success('Your loan is {}'.format(result))
     
if __name__=='__main__': 
    main()