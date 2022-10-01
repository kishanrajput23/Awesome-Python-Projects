# -*- coding: utf-8 -*-
"""
Created on Sun Jan 3, 14:59:31 2021

@author: Abhishek Gaurav
"""

from flask import Flask, request
import pickle
import pandas as pd
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

pickle_in = open('classifier.pkl','rb')
classifier = pickle.load(pickle_in)

@app.route('/')
def Welcome():
    return 'Welcome Everyone'

@app.route('/predict', methods=["GET"])
def predict_note_authentication():
    
    """Let's Authenticate the Paper Currency
    Built by ABHISHEK GAURAV.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output value is displayed in Response Body.
        
    """
    
    variance = request.args.get('variance')
    skewness = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy = request.args.get('entropy')
    prediction = classifier.predict([[variance,skewness,curtosis,entropy]])
    return "The Predicted Value is "+str(prediction)

@app.route('/predict_file',methods=['POST'])
def predict_note_file():
    
    """Let's Authenticate the Paper Currency
    Built by ABHISHEK GAURAV.
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true
      
    responses:
        200:
            description: The output values is displayed in Response Body.
        
    """
    
    df_test = pd.read_csv(request.files.get("file"))
    prediction = classifier.predict(df_test)
    return "The Predicted values for the test data is "+str(list(prediction))




if __name__=='__main__':
    app.run()