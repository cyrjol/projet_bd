# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import streamlit as st
import pandas as pd
from PIL import Image
def app():
    st.header('Data processing')

    st.subheader("Correlation Matrix")
    st.write("""
             
             We could use all the dataset, yet some of the variables seems to be very similar, so we could consider to avoid considering multiple features.
             
             We plot the correlation matrix of the features to see which variables have the most similar evolution.
             
             
             """)
    st.caption('Correlation Matrix')
    st.dataframe(pd.read_csv('data/scenario1/corr.csv'))
    
   
             
    st.subheader("Final dataset") 
    st.write("""
             
             At this point we can reduce the set of features to only 4 features without loosing most of the information in the original dataset.
             
             Moreover we are now indexing the dataframe by timestamp, and we have **scaled** the data so it would be easier to train our model in the future. 
             
             """)
    st.dataframe(pd.read_csv('data/scenario1/df_min.csv',parse_dates=['timestamp'], index_col='timestamp'))
    
    st.header('Training')
    st.write("""
             
             Eventhough the dataset contains labels, we want to use an **unsupervised** model which would be more accurate of a real use case where we do not have the labels instateniously.
            
             After considering different model, we choose to use a **PCA unsupervised model**, which is particularly efficient in case of anomaly detection.
             
             We train our model on the 505th scenario (abrupt with 15% of leak), so the model could detect a certain amount of anomalies.
             
             Here are the results :
             """)
             
             
    pred = pd.read_csv('data/scenario505/pred_data.csv', parse_dates=['timestamp'], index_col='timestamp')   
    y = pd.read_csv('data/scenario505/y.csv', parse_dates=['timestamp'], index_col='timestamp')      
    
    st.caption('True Anomalies')
    st.line_chart(y['Label'])
    st.caption('Predicted Anomalies')
    st.line_chart(pred['0'])
    
    mat =Image.open("data/scenario505/matrix.PNG")
    st.image(mat, caption='Training Confusion Matrix')
    
    st.write("""
             
             Our model is not the best, yet, it has predicted most of the anomalies at the beginning, which is a good beginning.
             
             Let's test this model on other scenario to see how it is doing.
             
             """)
    
    st.header('Test')
    st.write("""
             
             We test the model on the 2nd scenario (incipient with 5% of leak) :
             
             """)
             
    pred_2 = pd.read_csv('data/scenario2/pred.csv', parse_dates=['timestamp'], index_col='timestamp')   
    y_2 = pd.read_csv('data/scenario2/y.csv', parse_dates=['timestamp'], index_col='timestamp')      
    st.caption('True Anomalies') 
    st.line_chart(y_2['Label'])
    st.caption('Predicted Anomalies')
    st.line_chart(pred_2['0'])
     
    mat =Image.open("data/scenario2/matrix1.PNG")
    st.image(mat, caption='Test Confusion Matrix')        
    
    st.write("""
             
             We can see that our model has a pretty good accurracy but it is far from perfect, indeed there is a lot of noise.
             
             To avoid that we will try to **smooth** the data. 
             
             """)
    st.subheader('Smoothing')         
    st.write("""
             
                            
            For each prediction : *we round the mean of the prediction on the last day*
                 
            Let's look at that!
                
             
             """)
             
    data_2 = pd.read_csv('data/scenario2/pred_data.csv', parse_dates=['timestamp'], index_col='timestamp')   
    st.caption('True Anomalies')
    st.line_chart(y_2['Label'])
    st.caption('Predicted Anomalies')
    st.line_chart(data_2['0'])
     
    mat =Image.open("data/scenario2/matrix2.PNG")
    st.image(mat, caption='Test Confusion Matrix') 
    
    
    
    st.write("""
             
             We have a satisfying accuraccy.
             
             Our model looks ready, we will apply it to 3 scenario of each type in the **PREDICTION** page.
                
             
             """)






