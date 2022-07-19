# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 10:46:14 2022

@author: cjoly
"""

import streamlit as st
from multiapp import MultiApp
from apps import home, data, pred # import your app modules here

app = MultiApp()

st.markdown("""
# Water leak demo

This multi-page app is a demo of our skills applied to a usecase of predicting leaks in a water system distribution.
         
You can find the research paper at : https://zenodo.org/record/1313116#.YtUuFEZBxPY
          
          
The app is composed of 3 different pages :
- **Home page :** to explain the context and the data of the usecase
    
- **Data page :** to explain our processing of data and the choice of algorithm
    
- **Prediction page** : to highlight the results of our study
""")

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Data", data.app)
app.add_app("Prediction", pred.app)
# The main app
app.run()