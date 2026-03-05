import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import streamlit as st

from flask import Flask
app = Flask(__name__)

#print("Hello, this is a new file for testing purposes!")

st.title("Basic Streamlit Button Example")

if st.button("Click me"):
    st.success("Button was clicked!")
else:
    st.write("Waiting for you to click the button...")



@app.route('/')
def home():
    return "Welcome to the Flask app! This is the home page."


st.link_button("What is pizza??", "http://127.0.0.1:5000//pizza")


@app.route('/pizza')
def pizza():
    return "Pizza is the best food item in the food world!"



if __name__ == '__main__':
    app.run(debug=True)