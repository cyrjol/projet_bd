# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import streamlit as st
import matplotlib
import pandas as pd
from PIL import Image
import plotly.express as px 
 
def app():
    st.header('Data processing')
      
   
    st.write("""
             After some experimentation, we choose to do the preprocessing and the training on the 505th scenario because it is an abrupt scenario with a total of 20% of leak on the year,
             so the model has a certain amount of leak to detect.
             
             We could use all the dataset, yet some of the variables seems to be very similar, so we could consider to avoid considering multiple features.
             
             We plot the correlation matrix of the features to see which variables have the most similar evolution.
             
             
             """)
    st.write(' *Correlation Matrix Nodes* ')
    corr_1=pd.read_csv('data/scenario1/corr_1.csv')
    st.dataframe(corr_1.style.background_gradient())
    
    st.write("""
             
             As we can see, all the Nodes are higlhy correlated, thus we can keep only **Node 11**.
             
             """)
    
    st.write(' *Correlation Matrix Links* ')
    corr_2=pd.read_csv('data/scenario1/corr_2.csv')
    st.dataframe(corr_2.style.background_gradient())
    
    st.write("""
             
             As we can see, only 3 links have not over 0.9 correlation with **Node 11** :
                 
            - *Link 21*
                 
            - *Link 22*
                 
            - *Link 110*
             
            Yet, *Link 110* has 0.70 correlation with *Link 21* and considering we have already two Links features, we can also eliminate *Link 110*.
             """)
    
    st.write(' *Correlation Matrix Pressures* ')
    corr_3=pd.read_csv('data/scenario1/corr_3.csv')
    st.dataframe(corr_3.style.background_gradient())
    
    st.write("""
            
             As we can see, all the Pressures have 1.00 correlation between each other, thus we can keep only **Pressure 10**.
            
            """)
    
    st.subheader("Final dataset") 
    st.write("""
             We wanted at least 1 feature for each categorie ( Demands, Links, Pressures) and we have reduce the set of features to only **4 features** without loosing most of the information in the original dataset.
             
             Moreover we have **scaled** the data so it would be easier to train our model in the future. 
             
             """)
    st.dataframe(pd.read_csv('/data/scenario1/df_min.csv',parse_dates=['timestamp'], index_col='timestamp'))
    
    st.header('Training')
    st.write("""
             
             We could have used 2 approach:
                 
                - Time Series
                
                - Classification 
            
             We choose the 2nd option because it was the easiest to begin with. 
            
             Eventhough the dataset contains labels, we want to use an **unsupervised** model which would be more accurate of a real use case where we do not have the labels instateniously.
            
             We used the *PYOD* API  dedicated to anomaly detection. Thus, we tried some unsupervised model like *kNN, Isolation Forest and Autoencoder*.
             
             At the end, we had the best results with a **PCA** model.
             
             Principal component analysis (PCA) can be used in detecting outliers. PCA is a linear dimensionality reduction using Singular Value Decomposition of the data to project it to a lower dimensional space.

            In this procedure, covariance matrix of the data can be decomposed to orthogonal vectors, called eigenvectors, associated with eigenvalues. 

            Therefore, a low dimensional hyperplane constructed by k eigenvectors can capture most of the variance in the data. 
            
            However, outliers are different from normal data points, which is more obvious on the hyperplane constructed by the eigenvectors with small eigenvalues.

            Therefore, outlier scores can be obtained as the sum of the projected distance of a sample on all eigenvectors.
             
                          
             Here are the results :
             """)
             
             
    pred = pd.read_csv('data/scenario505/pred_data.csv', parse_dates=['timestamp'], index_col='timestamp')   
    y = pd.read_csv('data/scenario505/y.csv', parse_dates=['timestamp'], index_col='timestamp')      
   
    y = y.merge(pred,how='left', left_index=True, right_index=True)
    
    y.rename(columns={'Label': 'True', '0':'Predicted'},inplace=True)
    
    st.write(' *Anomalies* ')
    
    
    plot=px.scatter(x=y.index,y='Predicted', data_frame=y,color="True")
    st.plotly_chart(plot)
    
    st.write("""
             The color of the points corresponds to the true value of leakage :
            
            - Blue : there is no leak
            
            - Yellow : there is a leak
            
            The position of the points corresponds to the predicted value of leakage :
            
            - Top : predicts a leak
            
            - Bottom : predicts no leak
             
             
             
             """)
   
        
    mat =Image.open("data/scenario505/matrix.png")
    st.image(mat, caption='Training Confusion Matrix ')        
                                 
             
                          

    st.write("""
               
                We can see that our model has pretty good metrics :
                - Negative Predictive Value (the percentage of well-detected anomalies) : **44,33%** , the model is made to detect a maximum of 10% outliers.
                
                Therefore it misses a lot of outliers, however we notice that the beginning of the leak is well detected, this is our main objective.
                
                - Specify Rate (the percentage of true outliers that are detected) : **98,00 %**, the model makes few mistakes.
                
                The model is not perfect, yet it has good insights, so it's a good start to work on.
               
               
               """)
    
    
    st.header('Test')
    st.write("""
             
              We test the model on the 2nd scenario : incipient with 5% of leak over the year, to see how the model is doing on a more subtle leak.
             
             """)
             
    pred_2 = pd.read_csv('data/scenario2/pred.csv', parse_dates=['timestamp'], index_col='timestamp')   
    y_2 = pd.read_csv('data/scenario2/y.csv', parse_dates=['timestamp'], index_col='timestamp')      
    
    y = y_2.merge(pred_2,how='left', left_index=True, right_index=True)
    
    y.rename(columns={'Label': 'True', '0':'Predicted'},inplace=True)
    
    st.write(' *Anomalies* ')
    plot=px.scatter(x=y.index,y='Predicted', data_frame=y,color="True")
    st.plotly_chart(plot)
     
    mat =Image.open("data/scenario2/matrix1.png")
    st.image(mat, caption='Test Confusion Matrix')        
    
    st.write("""
             
             We can see that our model has pretty good metrics :
                - Negative Predictive Value : **84,11%** , much better than before, the leak is predicted very soon (4h). 
                - Specify Rate : **68,77 %**, there is a lot of noise ( blue points on top), but if we zoom in, we can see that these points are isolated, to avoid that we will try to **smooth** the data. 
              
             
             """)
    st.subheader('Smoothing')         
    st.write("""                                       
            We have noticed that most false anomalies are isolated (1 or 2 per day), but if there is a leak it lasts several days.
            
            Thus, we have consider different smoothing method : average over the last X hours > Y%.
            
            We have kept the method which consider that there is an anomaly if the average over the last 24 hours >50%, because it had good results and this is consistent, it means that we can detect the leak at least 12 hours after it starts which is acceptable.     
            
            Let's look at that!
                                     """)
             
    data_2 = pd.read_csv('data/scenario2/pred_data.csv', parse_dates=['timestamp'], index_col='timestamp')   
    y = y_2.merge(data_2,how='left', left_index=True, right_index=True)
    
    y.rename(columns={'Label': 'True', '0':'Predicted'},inplace=True)
    
    st.caption(' *Anomalies* ')
    plot=px.scatter(x=y.index,y='Predicted', data_frame=y,color="True")
    st.plotly_chart(plot)
     
    mat =Image.open("data/scenario2/matrix2.png")
    st.image(mat, caption='Test Confusion Matrix') 
    
    
    
    st.write("""
             
             Now the metrics are impressive :
                - Negative Predictive Value : **84%**, we have lost only 0.11%, now we predict the leak after *15h*. 
                - Specify Rate : **100 %**, we have eliminated all the noise.
                
                         
             Therefore, we lost a little speed of detection in favor of cleaning the results.
             
             Yet, when we apply this filter to more scenario, this is also very efficient as we will see on the **PREDICTION** page.
               
             
             """)






