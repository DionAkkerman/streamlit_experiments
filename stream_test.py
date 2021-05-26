# -*- coding: utf-8 -*-
"""
Created on Wed May 26 15:01:52 2021

@author: Dion
"""

#https://streamlit.io/

import streamlit as st
import numpy as np
import pandas as pd
import time


# Set init state
st.set_page_config(
    page_title="Look at me",
    page_icon="()",
    layout="wide",
    initial_sidebar_state="expanded",)

# Button
timer_button = st.sidebar.button('Countdown from 10')  

uploaded_file = st.file_uploader("Choose a file", type ="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    # Slider widget (on sidebar)
    selected_cat = st.sidebar.slider('Select a cat', value = 1, min_value = int(df.cat.min()), max_value = int(df.cat.max()))  

    st.success("File uploaded successfully")

    # Interactive table widget
    df = df.loc[df['cat'] == selected_cat]
    st.dataframe(df)
    # Little plot
    if 'value' in df.columns:
        st.line_chart(data=df['value'])
    




# Progress bar
progress_bar = st.progress(0)

# Some nice json:
st.json({'name': 'Dion',
         'goal': 'testing'})

if timer_button:
    i = 0
    with st.spinner(text='In progress...'):
        while i < 10:
            time.sleep(1)
            i += 1
            
            progress_bar.progress(i*10)
        
    st.balloons()


with st.echo():
    # Everything inside this block will be both printed to the screen
    # and executed.
    greeting = "Hi there!"
    st.write(greeting)
