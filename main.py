import streamlit as st
import pandas as pd

data = pd.read_csv("data/titanic.csv", sep = ';')

st.title("The titanic dataset")
st.dataframe(data)