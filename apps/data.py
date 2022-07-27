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
    
    st.write("""
             
             After some experimentation, we choose to do the preprocessing and the training on the 505th scenario because it is an abrupt scenario with a total of 20% of leak on the year,
             so the model has a certain amount of leak to detect. 
             
             
             """)

    st.subheader("Correlation Matrix")
    st.write("""
             
             We could use all the dataset, yet some of the variables seems to be very similar, so we could consider to avoid considering multiple features.
             
             We plot the correlation matrix of the features to see which variables have the most similar evolution.
             
             
             """)
    st.caption('Correlation Matrix')
    st.dataframe(pd.read_csv('data/scenario1/corr.csv'))
    
   
             
    st.subheader("Final dataset") 
    st.write("""
             We wanted at least 1 feature for each categorie ( Demands, Links, Pressures) and we eliminate the others features with more than **0.9** correlation.
             
             Thus we can reduce the set of features to only **4 features** without loosing most of the information in the original dataset.
             
             Moreover we are now indexing the dataframe by timestamp, and we have **scaled** the data so it would be easier to train our model in the future. 
             
             """)
    st.dataframe(pd.read_csv('data/scenario1/df_min.csv',parse_dates=['timestamp'], index_col='timestamp'))
    
    st.header('Training')
    st.write("""
             
             We could have used 2 approach:
                - Time Series
                - Unsupervised Classification 
            
            We choose the 2nd option because it had better results.             
             Eventhough the dataset contains labels, we want to use an **unsupervised** model which would be more accurate of a real use case where we do not have the labels instateniously.
            
             We consider different unsupervised model especially effective on anomaly detection case like *kNN, Isolation Forest, (Variational) Autoencoder* and *GAN*.
             
             At the end, we had the best results with a **PCA** model.
             
                          
             Here are the results :
             """)
             
             
    pred = pd.read_csv('data/scenario505/pred_data.csv', parse_dates=['timestamp'], index_col='timestamp')   
    y = pd.read_csv('data/scenario505/y.csv', parse_dates=['timestamp'], index_col='timestamp')      
    y = y.merge(pred,how='left', left_index=True, right_index=True)
    y.rename(columns={'Label': 'True', '0':'Predicted'},inplace=True)
    st.caption('Anomalies')
    st.line_chart(y[['True','Predicted']])
    
    mat =Image.open("data/scenario505/matrix.png")
    st.image(mat, caption='Training Confusion Matrix')
    
    st.write("""           
             Our model is not perfect, yet we witness two interesting points to begin :
                - Our model has a few false anomalies ( 2% of the predicted anomalies )
                - The beginning of the leak is well predicted
             
             Let's test this model on other scenario to see how it is doing.
             
             """)
    
    st.header('Test')
    st.write("""
             
             We test the model on the 2nd scenario : incipient with 5% of leak over the year, to see how the model is doing on a more subtle leak.
             
             """)
             
    pred_2 = pd.read_csv('data/scenario2/pred.csv', parse_dates=['timestamp'], index_col='timestamp')   
    y_2 = pd.read_csv('data/scenario2/y.csv', parse_dates=['timestamp'], index_col='timestamp')      
    y = y_2.merge(pred_2,how='left', left_index=True, right_index=True)
    y.rename(columns={'Label': 'True', '0':'Predicted'},inplace=True)
    st.caption('Anomalies')
    st.line_chart(y[['True','Predicted']])
     
    mat =Image.open("data/scenario2/matrix1.png")
    st.image(mat, caption='Test Confusion Matrix')        
    
    st.write("""
             
             We can see that our model has a pretty good metrics :
                - Negative Predictive Value : 84,11%
                - Specify Rate : 68,77 %
             
             Yet, it is far from perfect because there is a lot of noise.
             
             To avoid that we will try to **smooth** the data. 
             
             """)
    st.subheader('Smoothing')         
    st.write("""                                       
            We have noticed that most false anomalies are isolated (1 or 2 per day), but if there is a leak it lasts several days.
            Thus, our smoothing method is to consider that there is an anomaly if the average over the last 24 hours >50%.     
            
            Let's look at that!
                                     """)
             
    data_2 = pd.read_csv('data/scenario2/pred_data.csv', parse_dates=['timestamp'], index_col='timestamp')   
    y = y_2.merge(data_2,how='left', left_index=True, right_index=True)
    y.rename(columns={'Label': 'True', '0':'Predicted'},inplace=True)
    st.caption('Anomalies')
    st.line_chart(y[['True','Predicted']])
     
    mat =Image.open("data/scenario2/matrix2.png")
    st.image(mat, caption='Test Confusion Matrix') 
    
    
    
    st.write("""
             
             Now the metrics are impressive :
                - Negative Predictive Value : 84%
                - Specify Rate : 100 %
                
             We have eliminated all the false anomalies and with our smoothing filter we can detect a leak 12h after its beginning.
             
             Our model looks ready, we will apply it to 3 scenario of each type in the **PREDICTION** page.
                
             
             """)






