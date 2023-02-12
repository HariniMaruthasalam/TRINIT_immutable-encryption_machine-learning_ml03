# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 18:31:23 2023

@author: harin
"""

import numpy as np
import pickle
import streamlit as st
import pandas as pd

loading_model = pickle.load(open("C:/Users/harin/Downloads/crop_model.sav", 'rb'))

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://www.shutterstock.com/image-photo/blurred-mountain-background-260nw-269981756.jpg");
             background-attachment: fixed;
             background-size: cover;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
add_bg_from_url()


dict1={0: 'apple',
 1: 'banana',
 2: 'blackgram',
 3: 'chickpea',
 4: 'coconut',
 5: 'coffee',
 6: 'grapes',
 7: 'jute',
 8: 'kidneybeans',
 9: 'lentil',
 10: 'maize',
 11: 'mango',
 12: 'mothbeans',
 13: 'mungbean',
 14: 'muskmelon',
 15: 'orange',
 16: 'papaya',
 17: 'pigeonpeas',
 18: 'pomegrante',
 19: 'rice',
 20: 'watermelon',
 21: 'yellowbean',
 22: 'yellowbean'}

df = pd.DataFrame({'state': ['Andaman and Nicobar', 'Andhra Pradesh', 'Assam', 'Chattisgarh', 'Goa',
 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu and Kashmir', 'Karnataka',
 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Nagaland',
 'Odisha', 'Pondicherry', 'Punjab', 'Rajasthan', 'Tamil Nadu', 'Telangana',
 'Tripura', 'Uttar Pradesh', 'Uttrakhand', 'West Bengal']})
df['state'] = df['state'].astype('category')

def crop_prediction(state, modal_price, N, P, K, temperature, humidity, ph, rainfall):
    input_data = [state, modal_price, N, P, K, temperature, humidity, ph, rainfall]
    id_np_array = np.asarray(input_data)
    id_reshaped = id_np_array.reshape(1,-1)

    prediction = loading_model.predict(id_reshaped)
    var = prediction[0]
    return dict1[var]
 
def main():
    
    st.title('𝐂𝐑𝐎𝐏 𝐏𝐑𝐄𝐃𝐈𝐂𝐓𝐈𝐎𝐍')
    state = df['state'].cat.categories.get_loc(st.selectbox('𝐒𝐓𝐀𝐓𝐄 𝐎𝐅 𝐓𝐇𝐄 𝐒𝐎𝐈𝐋', df['state'].cat.categories))
    modal_price = st.text_input('𝐏𝐑𝐈𝐂𝐄')	
    N = st.text_input('𝐍𝐈𝐓𝐑𝐎𝐆𝐄𝐍')
    P = st.text_input('𝐏𝐎𝐓𝐀𝐒𝐒𝐈𝐔𝐌')
    K = st.text_input('𝐏𝐇𝐎𝐒𝐏𝐇𝐎𝐑𝐎𝐔𝐒')
    temperature = st.slider('𝐓𝐄𝐌𝐏𝐄𝐑𝐀𝐓𝐔𝐑𝐄', min_value=10, max_value=50, value=25, step=1)	
    humidity = st.slider('𝐇𝐔𝐌𝐈𝐃𝐈𝐓𝐘', min_value=0, max_value=100, value=13, step=1)
    ph = st.slider('𝐏𝐇', min_value=0, max_value=50, value=25, step=1)
    rainfall = st.slider('𝐑𝐀𝐈𝐍𝐅𝐀𝐋𝐋', min_value=0, max_value=300, value=105, step=1)	
    
    # Prediction code
    prediction = ''
    
    if st.button('Predict'):
        prediction = crop_prediction(state, modal_price, N, P, K, temperature, humidity, ph, rainfall)
        
    st.success(prediction)
    
if __name__=='__main__':
    main()
