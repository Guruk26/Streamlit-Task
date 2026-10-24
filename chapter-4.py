import streamlit as st

st.title("For Elements")

def change():
    st.success("value change")

st.slider("This ia my slider", max_value=200, min_value=100, width=300, value=150,step=2,on_change=change,
          key="slider_value")

st.write(f"value = {st.session_state.slider_value}")

st.text_input("Enter your name", width=300, placeholder="Enter your name",max_chars=10,key="input_name",
              type='password')
st.write(f"My name is {st.session_state.input_name}")

st.text_area("Feedback", placeholder="Enter your feedback", width=300, max_chars=100, disabled=True)

st.date_input("Select date")
st.time_input("Select Time")