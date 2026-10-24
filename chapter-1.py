import streamlit as st

st.title("Hello Programmers")
st.subheader("Welcome to Streamlit")
st.text("Welcome to our first streamlit app")
st.write("Choose a propramming language")

selected_elements = st.selectbox("Choose a language", ["Marathi", "Hindi", "English"])

if selected_elements:
    st.write(f"You choose {selected_elements} Language")
    st.success(f"{selected_elements} Language Selected")