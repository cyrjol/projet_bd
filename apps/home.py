# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 10:50:41 2022

@author: cjoly
"""
import streamlit as st
import pandas as pd
from PIL import Image
def app():
    st.header(" Benchmark description")       
    st.write("""
    Currently, there is not a widely accessible dataset of real or realistic leakage scenarios, which could be used as a common benchmark, such a dataset should contain multiple scenarios under varying conditions.
    
    Thus, we need to work on a simulated benchmark which consists of a large number of realistic leakage scenarios which occur randomly, of different size and intensity.
    
    For each leakage scenario (1000 in total), the leakage parameters (e.g., number of leaks, locations,size), the structural parameters (e.g., length, pipe roughness) and realistic consumer pressure-driven demands are varied.
    
    The dataset comprises all leakage scenario parameters, hydraulic dynamics(flows, pressures), node demands and the network model.
    
    Each leakage is also assigned a time profile :
    
    -**No leak**
    
    -**Abrupt** : the leak is of constant intensity
    
    -**Incipient** : the leak increases gradually which makes it more difficult to detect.
    
    Moreover, each leakage may remain for a longer or shorter period of time depending on whether the leak is found and repaired, corresponding to a % of leak. Thus we will present the different scenario as : scenario X with Y% of leak

                  """)
    network =Image.open("network.PNG")
    st.image(network, caption='Water Distribution Network')
    
    st.header( "Dataset description") 
    
    st.write("""
             
             Our dataset is composed of **17520 rows** which corresponds to 1 measure every 30min during a year, and **29 features** distribute in 3 categories :
            - **Nodes X :** values of the demand of water at each node 
                     
            - **Links X :** values of flows between the nodes 
                     
            - **Pressure X :** values of pressure on different nodes
             
             
             """)   
      
     
    st.subheader("Full dataset")   
    st.write("""
             
             As this point, our data is ready to be manipulated, here is an example of the raw data of the 1st scenario 
             
             """)
    st.dataframe(pd.read_csv('data/scenario1/df_full.csv'))
    
    
    
