import numpy as np
import pickle

def load_model(filename = "classifier.pkl"):
    pickle_in = open(filename, 'rb')
    return pickle.load(pickle_in) 

classifier = load_model("../../models/classifier.pkl")

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
    
    if ApplicantIncome == "":
        ApplicantIncome = 0
        
    if LoanAmount == "":
        LoanAmount = 0    
    
    LoanAmount = LoanAmount / 1000
    
    # Making predictions 
    prediction = classifier.predict( 
        [[Gender, Married, ApplicantIncome, LoanAmount, Credit_History]])
     
    if prediction == 0:
        pred = 'Rejected'
    else:
        pred = 'Approved'
    return pred