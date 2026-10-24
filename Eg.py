import streamlit as st

st.write("Hello World")

st.title("Hello Streamlit")
st.write("This is my First Streamlit App")
st.header("Welcome to Streamlit")
st.subheader("This is a Subheader")
st.text("This is plain text")

## Buttons, Checkboxes and Sliders

if st.button("Click me"):
    st.write("Button clicked")

agree=st.checkbox("I agree")
if agree:
    st.write("You agreed")

level=st.slider("Select a level:", 1, 10, 5)
st.write(f"Selected Level: {level}")


uploaded_file=st.file_uploader("Upload a File",type=['csv','txt'])

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df.head())