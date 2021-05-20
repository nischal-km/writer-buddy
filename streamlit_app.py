import streamlit as st
import pandas as pd
import numpy as np
from transformers import GPT2Tokenizer, GPT2LMHeadModel

tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained("gpt2", pad_token_id=tokenizer.eos_token_id)

inputs = tokenizer("I am a full stack developer and also interested in machine learning ", return_tensors="pt")
generation_output = model.generate(**inputs, max_length=50)
ot = tokenizer.decode(generation_output[0], skip_special_tokens=True)

st.title('Writer buddy')
st.subheader('An app which helps you to write better')

st.text_area('Write your text')
st.button('Suggest')

st.text(ot)
