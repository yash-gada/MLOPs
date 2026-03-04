import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import streamlit as st

from flask import Flask

print("Hello, this is a new file for testing purposes!")

st.title("Basic Streamlit Button Example")

if st.button("Click me"):
    st.write("Button was clicked!")
else:
    st.write("Waiting for you to click the button...")
