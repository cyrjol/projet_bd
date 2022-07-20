# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 11:30:34 2022

@author: cjoly
"""
import streamlit as st
import pandas as pd
def app():
    
        st.write("""
             # Prediction
             For each type of scenario (incipient, abrupt or no leak) we choose 3 different scenario with various % of leakage to see the accuraccy of the prediction of our model.
             
             """)
             
    
    #data not scaled for plotting ( i:i,cipient, a: abrupt, n: no leaked)
        i_1 = pd.read_csv('data/scenario1/df_full.csv',parse_dates=['timestamp'], index_col='timestamp')
        i_2 = pd.read_csv('data/scenario2/df_full.csv',parse_dates=['timestamp'], index_col='timestamp')
        i_3 = pd.read_csv('data/scenario3/df_full.csv',parse_dates=['timestamp'], index_col='timestamp')


        a_5 = pd.read_csv('data/scenario5/df_full.csv',parse_dates=['timestamp'], index_col='timestamp')
        a_6 = pd.read_csv('data/scenario6/df_full.csv',parse_dates=['timestamp'], index_col='timestamp')
        a_22 = pd.read_csv('data/scenario22/df_full.csv',parse_dates=['timestamp'], index_col='timestamp')


        n_4 = pd.read_csv('data/scenario4/df_full.csv',parse_dates=['timestamp'], index_col='timestamp')
        n_7 = pd.read_csv('data/scenario7/df_full.csv',parse_dates=['timestamp'], index_col='timestamp')
        n_10 = pd.read_csv('data/scenario10/df_full.csv',parse_dates=['timestamp'], index_col='timestamp')
    #data not scaled for plotting
    
    #true labels
    
        l_1 = pd.read_csv('data/scenario1/y.csv', parse_dates=['timestamp'], index_col='timestamp')
        l_2 = pd.read_csv('data/scenario2/y.csv', parse_dates=['timestamp'], index_col='timestamp')
        l_3 = pd.read_csv('data/scenario3/y.csv', parse_dates=['timestamp'], index_col='timestamp')
        l_4 = pd.read_csv('data/scenario4/y.csv', parse_dates=['timestamp'], index_col='timestamp')
        l_5 = pd.read_csv('data/scenario5/y.csv', parse_dates=['timestamp'], index_col='timestamp')
        l_6 = pd.read_csv('data/scenario6/y.csv', parse_dates=['timestamp'], index_col='timestamp')
        l_7 = pd.read_csv('data/scenario7/y.csv', parse_dates=['timestamp'], index_col='timestamp')
        l_10 = pd.read_csv('data/scenario10/y.csv', parse_dates=['timestamp'], index_col='timestamp')
        l_22 = pd.read_csv('data/scenario22/y.csv', parse_dates=['timestamp'], index_col='timestamp')
    
    
    #labels predicted
        pred_1 = pd.read_csv('data/scenario1/pred_data.csv', parse_dates=['timestamp'], index_col='timestamp')
        pred_2 = pd.read_csv('data/scenario2/pred_data.csv', parse_dates=['timestamp'], index_col='timestamp')
        pred_3 = pd.read_csv('data/scenario3/pred_data.csv', parse_dates=['timestamp'], index_col='timestamp')
        pred_4 = pd.read_csv('data/scenario4/pred_data.csv', parse_dates=['timestamp'], index_col='timestamp')
        pred_5 = pd.read_csv('data/scenario5/pred_data.csv', parse_dates=['timestamp'], index_col='timestamp')
        pred_6 = pd.read_csv('data/scenario6/pred_data.csv', parse_dates=['timestamp'], index_col='timestamp')
        pred_7 = pd.read_csv('data/scenario7/pred_data.csv', parse_dates=['timestamp'], index_col='timestamp')
        pred_10 = pd.read_csv('data/scenario10/pred_data.csv', parse_dates=['timestamp'], index_col='timestamp')
        pred_22 = pd.read_csv('data/scenario22/pred_data.csv', parse_dates=['timestamp'], index_col='timestamp')
        
        options = st.multiselect('What type of scenario do you want to see ?',['No Leak','Incipient','Abrupt'])
        
        for i in options :
            if i=='No Leak':
              st.header('No leak scenario')  
                
              st.subheader("Scenario 4")
              st.caption("Link 21 flow")
              st.line_chart(n_4['Link 21'])
              st.caption('True anomalies')
              st.line_chart(l_4['Label'])
              st.caption('Predicted Anomalies')
              st.line_chart(pred_4['0'])
              
              
              st.subheader("Scenario 7")
              st.caption("Link 21 flow")
              st.line_chart(n_7['Link 21'])
              st.caption('True anomalies')
              st.line_chart(l_7['Label'])
              st.caption('Predicted Anomalies')
              st.line_chart(pred_7['0'])
              
              st.subheader("Scenario 10")
              st.caption("Link 21 flow")
              st.line_chart(n_10['Link 21'])
              st.caption('True anomalies')
              st.line_chart(l_10['Label'])
              st.caption('Predicted Anomalies')
              st.line_chart(pred_10['0']) 
               
              st.write("""
                       As you can see, at the exception of a few noise on the first two scenario our prediction is satisfying.
                       
                       These false anomalies happen during the Summer when the water demands varies more which misslead our model, yet it is acceptable.
                       
                       
                       """) 


            elif i=='Abrupt':
                st.header('Abrupt scenario')
                
                st.subheader("Scenario 5")
                st.caption("Link 21 flow")
                st.line_chart(a_5['Link 21'])
                st.caption('True anomalies')
                st.line_chart(l_5['Label'])
                st.caption('Predicted Anomalies')
                st.line_chart(pred_5['0'])
                
                
                st.subheader("Scenario 6")
                st.caption("Link 21 flow")
                st.line_chart(a_6['Link 21'])
                st.caption('True anomalies')
                st.line_chart(l_6['Label'])
                st.caption('Predicted Anomalies')
                st.line_chart(pred_6['0'])
                
                st.subheader("Scenario 22")
                st.caption("Link 21 flow")
                st.line_chart(a_22['Link 21'])
                st.caption('True anomalies')
                st.line_chart(l_22['Label'])
                st.caption('Predicted Anomalies')
                st.line_chart(pred_22['0']) 
                
                
                
                st.write("""
                         As you can see, at the exception of a few noise on the 5th scenario (like with the 'no leak' scenarios) our prediction is satisfying.
                         
                         
                         
                         
                         """) 
                
            elif i=='Incipient':
                st.header('Incipient scenario')
                
                st.subheader("Scenario 1")
                st.caption("Link 21 flow")
                st.line_chart(i_1['Link 21'])
                st.caption('True anomalies')
                st.line_chart(l_1['Label'])
                st.caption('Predicted Anomalies')
                st.line_chart(pred_1['0'])
                
                
                st.subheader("Scenario 2")
                st.caption("Link 21 flow")
                st.line_chart(i_2['Link 21'])
                st.caption('True anomalies')
                st.line_chart(l_2['Label'])
                st.caption('Predicted Anomalies')
                st.line_chart(pred_2['0'])
                
                st.subheader("Scenario 3")
                st.caption("Link 21 flow")
                st.line_chart(i_3['Link 21'])
                st.caption('True anomalies')
                st.line_chart(l_3['Label'])
                st.caption('Predicted Anomalies')
                st.line_chart(pred_3['0']) 
                
                st.write("""
                         As you can see, in every scenario our model succeed to predict the beginning of the anomaly which is our goal.
                         For the 1st scenario, the model succesfully predict the first anomalies but at some point it does no longer consider them as anomalies when the flow reduces.
                         For the 2nd scenario, the prediction is almost perfect.
                         For the 3rd scenario, we have the same results as with the 1st scenario.
                         Thus our prediction is satisfying.
                         """) 
                
                
        
