import streamlit as st
import pandas as pd

data = pd.read_csv("data/titanic.csv", sep = ';')

st.title("The titanic dataset")

rows_to_show = st.slider("How many rows of data do you want to show?", 0, 100, 10)
st.dataframe(data.head(rows_to_show))