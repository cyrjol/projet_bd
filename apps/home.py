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
     Currently, there is not a widely accessible dataset of real or realistic leakage scenarios, which could be used as a common benchmark. 
     
     Such a dataset should contain multiple scenarios and networks under varying conditions, to provide an objective assessment of the fault diagnosis algoritm.
          
     Thus, we need to work on a simulated benchmark which is comprised of a large number of realistic leakage scenarios which occur randomly at different water distribution benchmark networks, of different size and topology. 
     
     For each benchmark network  and  for  each  leakage  scenario *(1000 in total)*,  the  leakage  parameters  (e.g.,  number  of  leaks,  locations,size), the structural parameters (e.g., length, pipe roughness) and realistic consumer pressure-drivendemands are varied. 
     
     The dataset is comprised of all leakage scenario parameters, hydraulic dynamics(flows, pressures), node demands and the network model.
     
     Each leakage is also assigned a time profile, categorizing them as abrupt leakages, or incipient leakages which increase gradually.
     
     The simulated network model looks like the following picture :
                  """)
    network =Image.open("network.PNG")
    st.image(network, caption='Water Distribution Network')
    
    st.header( "Dataset description") 
    
    st.write("""
             
             Our dataset is composed of **17520 rows** which corresponds to 1 measure every 30min during a year, and **33 features** distribute in 3 categories :
            - **Nodes X :** values of the demand of water at each node 
                     
            - **Links X :** values of flows between the nodes 
                     
            - **Pressure X :** values of pressure on different nodes
             
             
             """)   
      
     
    st.subheader("Full dataset")   
    st.write("""
             
             As this point, our data is ready to be manipulated, here is an example of the raw data of the 1st scenario 
             
             """)
    st.dataframe(pd.read_csv('data/scenario1/df_full.csv'))
    
    
    
