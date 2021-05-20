import streamlit as st
import pandas as pd
import numpy as np

from transformers import pipeline

nlp = pipeline("sentiment-analysis")

st.text(nlp("I hate you"))
st.text(nlp("I love you"))

st.title('Writer buddy')
st.subheader('An app which helps you to write better')

st.text_area('Write your text')
st.button('Suggest')
