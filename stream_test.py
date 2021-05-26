# -*- coding: utf-8 -*-
"""
Created on Wed May 26 15:01:52 2021

@author: Dion
"""

#https://streamlit.io/

import streamlit as st
import numpy as np

dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)