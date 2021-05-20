import streamlit as st
import pandas as pd
import numpy as np

from aitextgen import aitextgen

st.title('Writer buddy')
st.subheader('An app which helps you to write better or some inspiration')
st.text('This app is just for educational purpose')
st.button('Suggest')

# Without any parameters, aitextgen() will download, cache, and load the 124M GPT-2 "small" model
# Without any parameters, aitextgen() will download, cache, and load the 124M GPT-2 "small" model

# create a prompt text for the text generation 
prompt_text = st.text_input(label = "Enter your prompt text...",
            value = "Computer is beautiful")

with st.spinner("AI is at Work........"):
    # text generation
    gpt_text = ai.generate_one(prompt=prompt_text,
            max_length = 100 )
st.success("AI Successfully generated the below text ")
st.balloons()
# print ai generated text
print(gpt_text)

st.text(gpt_text)
