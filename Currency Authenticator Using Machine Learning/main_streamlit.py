# -*- coding: utf-8 -*-
"""
Created on Mon Jan 4, 20:42:56, 2021

@author: Abhishek Gaurav
"""

import pickle
import streamlit as st 

pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

def welcome():
    return "Hello, Welcome"

def predict_note_authentication(variance,skewness,curtosis,entropy):
    
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
            description: The output values
        
    """
   
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    print(prediction)
    return prediction



def main():
    st.title("PAPER CURRENCY AUTHENTICATOR")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Currency Authenticator ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    variance = st.text_input("Variance","")
    skewness = st.text_input("Skewness","")
    curtosis = st.text_input("Curtosis","")
    entropy = st.text_input("Entropy","")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(variance,skewness,curtosis,entropy)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Built with Streamlit")
        st.text("Built by Abhishek Gaurav")

if __name__=='__main__':
    main()
    