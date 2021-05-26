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

cats = [1,1,2,2,3,3,3]
df = pd.DataFrame({'cat': cats, 'value': np.random.randn(len(cats))})

# Slider widget (on sidebar)
selected_cat = st.sidebar.slider('Select a cat', value = 1, min_value = int(df.cat.min()), max_value = int(df.cat.max()))  
# Button
timer_button = st.sidebar.button('Countdown from 10')  

# Interactive table widget
df = df.loc[df['cat'] == selected_cat]
st.dataframe(df)
# Little plot
st.line_chart(data=df['value'])

# Progress bar
progress_bar = st.progress(0)

# Some nice json:
st.json({'name': 'Dion',
         'goal': 'testing'})

if timer_button:
    i = 0
    while i < 10:
        time.sleep(1)
        i += 1
        progress_bar.progress(i*10)
    
    st.balloons()
