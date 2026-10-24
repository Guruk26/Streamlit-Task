import streamlit as st
import pandas as pd

st.title("CSV Data Viewer")

data=pd.read_csv("Housing.csv")

st.subheader("Dataframe View")

st.dataframe(data)

st.subheader("Table View")

st.table(data)