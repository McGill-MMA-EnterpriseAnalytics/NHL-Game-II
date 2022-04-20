# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 15:48:22 2022

@author: vvaib
"""

import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(shots,shots_against,goals,goals_against,takeaways,takeaways_against,hits,
                                hits_against,blocked_shots,blocked_shots_against,giveaways,giveaways_against,
                                missed_shots,missed_shots_against,penalities,penalities_against,won_faceoffs,
                                lost_faceoffs,hoa_away,hoa_home):
    
    """Let's Authenticate the NHL prediction 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: shots
        in: query
        type: number
        required: true
      - name: shots_against
        in: query
        type: number
        required: true
      - name: goals
        in: query
        type: number
        required: true
      - name: goals_against
        in: query
        type: number
        required: true
      - name: takeaways
        in: query
        type: number
        required: true
      - name: takeaways_against
        in: query
        type: number
        required: true
      - name: hits
        in: query
        type: number
        required: true
      - name: hits_against
        in: query
        type: number
        required: true
      - name: blocked_shots
        in: query
        type: number
        required: true
      - name: blocked_shots_against
        in: query
        type: number
        required: true
      - name: giveaways
        in: query
        type: number
        required: true
      - name: giveaways_against
        in: query
        type: number
        required: true
      - name: missed_shots
        in: query
        type: number
        required: true
      - name: missed_shots_against
        in: query
        type: number
        required: true
      - name: penalities
        in: query
        type: number
        required: true
      - name: penalities_against
        in: query
        type: number
        required: true
      - name: won_faceoffs
        in: query
        type: number
        required: true
      - name: lost_faceoffs
        in: query
        type: number
        required: true
      - name: hoa_away
        in: query
        type: number
        required: true
      - name: hoa_home
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
   
    prediction=classifier.predict([[shots,shots_against,goals,goals_against,takeaways,takeaways_against,hits,
                                    hits_against,blocked_shots,blocked_shots_against,giveaways,giveaways_against,
                                    missed_shots,missed_shots_against,penalities,penalities_against,won_faceoffs,
                                    lost_faceoffs,hoa_away,hoa_home]])
    print(prediction)
    return prediction



def main():
    st.title("NHL Prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit NHL prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    shots = st.text_input("shots","Type Here")
    shots_against = st.text_input("shots_against","Type Here")
    goals = st.text_input("goals","Type Here")
    goals_against = st.text_input("goals_against","Type Here")
    takeaways = st.text_input("takeaways","Type Here")
    takeaways_against = st.text_input("takeaways_against","Type Here")
    hits = st.text_input("hits","Type Here")
    hits_against = st.text_input("hits_against","Type Here")
    blocked_shots = st.text_input("blocked_shots","Type Here")
    blocked_shots_against = st.text_input("blocked_shots_against","Type Here")
    giveaways = st.text_input("giveaways","Type Here")
    giveaways_against = st.text_input("giveaways_against","Type Here")
    missed_shots = st.text_input("missed_shots","Type Here")
    missed_shots_against = st.text_input("missed_shots_against","Type Here")
    penalities = st.text_input("penalities","Type Here")
    penalities_against = st.text_input("penalities_against","Type Here")
    won_faceoffs = st.text_input("won_faceoffs","Type Here")
    lost_faceoffs = st.text_input("lost_faceoffs","Type Here")
    hoa_away = st.text_input("hoa_away","Type Here")
    hoa_home = st.text_input("hoa_home","Type Here")
    
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(shots,shots_against,goals,goals_against,takeaways,takeaways_against,hits,
                                        hits_against,blocked_shots,blocked_shots_against,giveaways,giveaways_against,
                                        missed_shots,missed_shots_against,penalities,penalities_against,won_faceoffs,
                                        lost_faceoffs,hoa_away,hoa_home)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets Play")
        st.text("Built with Streamlit by Vaibhav")

if __name__=='__main__':
    main()