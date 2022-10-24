
from cProfile import label
import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 
import sklearn
import time

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("fake-account-classifier.sav","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(Num_posts,Num_following,Num_followers,Biography_length,Picture_availability,Link_availability,Average_caption_length,Likes,Comments,Hashtag_count,Average_Post_interval):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
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
   
    prediction=classifier.predict([[Num_posts,Num_following,Num_followers,Biography_length,Picture_availability,Link_availability,Average_caption_length,Likes,Comments,Hashtag_count,Average_Post_interval]])
    print(prediction)
    return prediction



def main():
    st.title("Instagram Fake Account Athenticator")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Fake Account Athenticator ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Num_posts = st.text_input("Num_posts")
    Num_following = st.text_input("Num_following","Type Here")
    Num_followers = st.text_input("Num_followers","Type Here")
    Biography_length = st.text_input("Biography_length","Type Here")
    Picture_availability = st.text_input("Picture_availability","Type Here")
    Link_availability = st.text_input("Link_availability","Type Here")
    Average_caption_length = st.text_input("Average_caption_length","Type Here")
    Likes = st.text_input("Likes","Type Here")
    Comments = st.text_input("Comments","Type Here")
    Hashtag_count = st.text_input("Hashtag_count","Type Here")
    Average_Post_interval = st.text_input("Average_Post_interval","Type Here")
    result=""
    if st.button("Predict"):

      with st.spinner(text='In progress'):
        time.sleep(5)
        result=predict_note_authentication(Num_posts,Num_following,Num_followers,Biography_length,Picture_availability,Link_availability,Average_caption_length,Likes,Comments,Hashtag_count,Average_Post_interval)
        
    st.success('The output is {}'.format(result))
    if st.button("About"):
         with st.spinner(text='In progress'):
            time.sleep(5)
            st.success('Done')
            st.text("Lets LEarn")
            st.text("Built with Streamlit")


if __name__=='__main__':
    main()
    
    
    