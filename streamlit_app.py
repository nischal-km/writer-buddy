import streamlit as st
import pandas as pd
import numpy as np

from aitextgen import aitextgen

st.title('Writer buddy')

st.subheader('An app which helps you to write better')

st.text('This app is just for educational purpose')

# instantiate the model / download
ai = aitextgen()

# create a prompt text for the text generation 

#prompt_text = "Python is awesome"

prompt_text = st.text_input(label = "Enter your story",
 value ="once upon a time")

with st.spinner("Generating suggestions for you"):
    # text generation
    gpt_text = ai.generate_one(prompt=prompt_text,
            max_length = 1000)
            
st.success("Suggestions has been created")

st.balloons()

st.text(gpt_text)

