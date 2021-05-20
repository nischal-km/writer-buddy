import streamlit as st
import pandas as pd
import numpy as np

from aitextgen import aitextgen

# Without any parameters, aitextgen() will download, cache, and load the 124M GPT-2 "small" model
ai = aitextgen()

ai.generate()
ai.generate(n=3, max_length=100)
output = ai.generate(n=3, prompt="I believe in unicorns because", max_length=100)

st.title('Writer buddy')
st.subheader('An app which helps you to write better or some inspiration')

st.button('Suggest')

st.text(output)
