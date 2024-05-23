import streamlit as st

# Title of the app
st.title('My First Streamlit App')

# Header
st.header('Welcome to my app')

# Text
st.write('This is a simple Streamlit app.')

# Input from the user
name = st.text_input('Enter your name:')
if name:
    st.write(f'Hello, {name}!')

# Slider
age = st.slider('Select your age:', 0, 100, 25)
st.write(f'You are {age} years old.')

# Button
if st.button('Say Hello'):
    st.write('Hello Streamlit!')

# File uploader
uploaded_file = st.file_uploader('Choose a file')
if uploaded_file is not None:
    st.write('File uploaded successfully!')
