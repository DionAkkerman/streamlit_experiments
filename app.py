# -*- coding: utf-8 -*-
"""
Created on Wed May 26 15:01:52 2021

@author: Dion
"""

#https://streamlit.io/

import streamlit as st
from process_pcap import get_ips_simple
#import pandas as pd
import time
from generate_graph import generate_graph

# Set init state
st.set_page_config(
    page_title="PCAP grapher",
    page_icon="()",
    layout="wide",
    initial_sidebar_state="expanded",)

st.title('PCAP grapher')

### Sidebare
# Button
uploaded_file = st.sidebar.file_uploader("Upload a PCAP", type ="pcap")
if uploaded_file:
    layout = st.sidebar.selectbox('layout',['dot',
                                            'neato', 
                                            'circo', 
                                            'fdp', 
                                            'sfdp'])
    rankdir = st.sidebar.selectbox("rankdir", ['BT', 'TB', 'LR', 'RL'])
    ranksep = st.sidebar.slider("ranksep",min_value=0, max_value=10)
    nodesep = st.sidebar.slider("nodesep",min_value=0, max_value=10)
timer_button = st.sidebar.button('Countdown from 10 for some fun')  

# For alerts and # Progress bar
status_updates = st.empty()
progress_bar = st.empty()


if uploaded_file:
    
    start = time.time()
    
    with st.spinner("Processing PCAP"):
        nodes, edges = get_ips_simple(uploaded_file)


    with st.spinner("Generating Graph"):
        generate_graph(nodes, edges, layout, rankdir, ranksep, nodesep)
    

    # Some nice json:
    st.json({'number of unique IPs': len(nodes), 'processing time (s)': round(time.time() - start, 2)})
    
    #df = pd.read_csv(uploaded_file)
    # Slider widget (on sidebar)
    #selected_cat = st.sidebar.slider('Select a cat', value = 1, min_value = int(df.cat.min()), max_value = int(df.cat.max()))  

    #st.success("File uploaded successfully")

    # Interactive table widget
    #df = df.loc[df['cat'] == selected_cat]
    #st.dataframe(df)
    # Little plot
    #if 'value' in df.columns:
    #    st.line_chart(data=df['value'])
    
if timer_button:
    progress_bar.progress(0)

    i = 0
    with st.spinner(text='In progress...'):
        while i < 10:
            time.sleep(1)
            i += 1
            
            progress_bar.progress(i*10)
        
    st.balloons()


