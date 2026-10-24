import streamlit as st

st.subheader("Chapter 2")

button = st.button("CLick Me")
print(button)

if button:
    st.write("Clicked")
else:
    st.write("Please Click the Button")

name = st.text_input("Enter Your Name: ")
st.write("Your name is ", name)

number = st.number_input("Enter some number",min_value=0, max_value=10, value=5)
st.write(number)

gender = st.radio("Select your gender", ["Male", "Female"])
st.write(gender)