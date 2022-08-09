# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 11:30:34 2022

@author: cjoly
"""
import streamlit as st
import pandas as pd
import plotly.express as px 
def app():
    
        st.write("""
             # Prediction
             For each type of scenario (incipient, abrupt or no leak) we have chosen 3 different scenario with various leakage % to see our model's performance .
             
             """)
             
    
    #data not scaled for plotting ( i:i,cipient, a: abrupt, n: no leaked)
        i_1 = pd.read_csv('data/scenario1/df.csv',parse_dates=['timestamp'], index_col='timestamp')
        i_2 = pd.read_csv('data/scenario2/df.csv',parse_dates=['timestamp'], index_col='timestamp')
        i_3 = pd.read_csv('data/scenario3/df.csv',parse_dates=['timestamp'], index_col='timestamp')


        a_5 = pd.read_csv('data/scenario5/df.csv',parse_dates=['timestamp'], index_col='timestamp')
        a_6 = pd.read_csv('data/scenario6/df.csv',parse_dates=['timestamp'], index_col='timestamp')
        a_22 = pd.read_csv('data/scenario22/df.csv',parse_dates=['timestamp'], index_col='timestamp')


        n_4 = pd.read_csv('data/scenario4/df.csv',parse_dates=['timestamp'], index_col='timestamp')
        n_7 = pd.read_csv('data/scenario7/df.csv',parse_dates=['timestamp'], index_col='timestamp')
        n_10 = pd.read_csv('data/scenario10/df.csv',parse_dates=['timestamp'], index_col='timestamp')
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
        
        
        y_1 = l_1.merge(pred_1,how='left', left_index=True, right_index=True)
        y_1.rename(columns={'Label': 'True', '0':'Predicted'},inplace=True)
        
        y_2 = l_2.merge(pred_2,how='left', left_index=True, right_index=True)
        y_2.rename(columns={'Label': 'True', '0':'Predicted'},inplace=True)
        
        y_3 = l_3.merge(pred_3,how='left', left_index=True, right_index=True)
        y_3.rename(columns={'Label': 'True', '0':'Predicted'},inplace=True)
        
        y_4 = l_4.merge(pred_4,how='left', left_index=True, right_index=True)
        y_4.rename(columns={'Label': 'True', '0':'Predicted'},inplace=True)
        
        y_5 = l_5.merge(pred_5,how='left', left_index=True, right_index=True)
        y_5.rename(columns={'Label': 'True', '0':'Predicted'},inplace=True)
        
        y_6 = l_6.merge(pred_6,how='left', left_index=True, right_index=True)
        y_6.rename(columns={'Label': 'True', '0':'Predicted'},inplace=True)
        
        y_7 = l_7.merge(pred_7,how='left', left_index=True, right_index=True)
        y_7.rename(columns={'Label': 'True', '0':'Predicted'},inplace=True)
        
        y_10 = l_10.merge(pred_10,how='left', left_index=True, right_index=True)
        y_10.rename(columns={'Label': 'True', '0':'Predicted'},inplace=True)
        
        y_22 = l_22.merge(pred_22,how='left', left_index=True, right_index=True)
        y_22.rename(columns={'Label': 'True', '0':'Predicted'},inplace=True)
        
        
        
        options = st.multiselect('What type of scenario do you want to see ?',['No Leak','Incipient','Abrupt'])
        
        for i in options :
            if i=='No Leak':
              st.header('No leak scenario')  
                
              st.subheader("Scenario 4")
              st.write("Node 11 Demands")
              plot=px.scatter(x=n_4.index,y='Node 11', data_frame=n_4)
              st.plotly_chart(plot)
              st.write('Anomalies')
              plot=px.scatter(x=y_4.index,y='Predicted', data_frame=y_4,color="True")
              st.plotly_chart(plot)
              
              
              st.subheader("Scenario 7")
              st.write("Node 11 Demands")
              plot=px.scatter(x=n_7.index,y='Node 11', data_frame=n_7)
              st.plotly_chart(plot)
              st.write('Anomalies')
              plot=px.scatter(x=y_7.index,y='Predicted', data_frame=y_7,color="True")
              st.plotly_chart(plot)
              
              st.subheader("Scenario 10")
              st.write("Node 11 Demands")
              plot=px.scatter(x=n_10.index,y='Node 11', data_frame=n_10)
              st.plotly_chart(plot)
              st.write('Anomalies')
              plot=px.scatter(x=y_10.index,y='Predicted', data_frame=y_10,color="True")
              st.plotly_chart(plot) 
               
              st.write("""
                       As you can see, at the exception of a few noise on the first two scenario our prediction is satisfying.
                       
                       These false anomalies happen during the Summer when the water demands varies more which misslead our model, yet it is acceptable.
                       
                       
                       We could also implement a business rule like for instance : we send a technician after 24h of anomaly.
                       """) 


            elif i=='Abrupt':
                st.header('Abrupt scenario')
                
                st.subheader("Scenario 5")
                st.write("Node 11 Demands")
                plot=px.scatter(x=a_5.index,y='Node 11', data_frame=a_5)
                st.plotly_chart(plot)
                st.write('Anomalies')
                plot=px.scatter(x=y_5.index,y='Predicted', data_frame=y_5,color="True")
                st.plotly_chart(plot)
                
                
                st.subheader("Scenario 6")
                st.write("Node 11 Demands")
                plot=px.scatter(x=a_6.index,y='Node 11', data_frame=a_6)
                st.plotly_chart(plot)
                st.write('Anomalies')
                plot=px.scatter(x=y_6.index,y='Predicted', data_frame=y_6,color="True")
                st.plotly_chart(plot)
                
                st.subheader("Scenario 22")
                st.write("Node 11 Demands")
                plot=px.scatter(x=a_22.index,y='Node 11', data_frame=a_22)
                st.plotly_chart(plot)
                st.write('Anomalies')
                plot=px.scatter(x=y_22.index,y='Predicted', data_frame=y_22,color="True")
                st.plotly_chart(plot)
                
                
                
                st.write("""
                         
                         In each scenario, we can predict leaks in less than a day.
                         
                         Therefore our prediction is satisfying.
                         
                         
                         
                         """) 
                
            elif i=='Incipient':
                st.header('Incipient scenario')
                
                st.subheader("Scenario 1")
                st.write("Node 11 Demands")
                plot=px.scatter(x=i_1.index,y='Node 11', data_frame=i_1)
                st.plotly_chart(plot)
                st.write('Anomalies')
                plot=px.scatter(x=y_1.index,y='Predicted', data_frame=y_1,color="True")
                st.plotly_chart(plot)
                
                
                st.subheader("Scenario 2")
                st.write("Node 11 Demands")
                plot=px.scatter(x=i_2.index,y='Node 11', data_frame=i_2)
                st.plotly_chart(plot)
                st.write('Anomalies')
                plot=px.scatter(x=y_2.index,y='Predicted', data_frame=y_2,color="True")
                st.plotly_chart(plot)
                
                st.subheader("Scenario 3")
                st.write("Node 11 Demands")
                plot=px.scatter(x=i_3.index,y='Node 11', data_frame=i_3)
                st.plotly_chart(plot)
                st.write('Anomalies')
                plot=px.scatter(x=y_3.index,y='Predicted', data_frame=y_3,color="True")
                st.plotly_chart(plot)
                
                st.write("""
                         In each scenario, we can predict leaks in less than a day, yet we can see more waste than with the abrupt scenario.
                         
                         The main explanation, is that these scenarios contains a certain % of leakage, in real case we want to detect the leak as soon as possible, which would correspond to a scenario with a few % of leak like the 2nd where we have the best results.
                         
                         Therefore our prediction is satisfying.
                         """) 
                
                
        
                
                
        
