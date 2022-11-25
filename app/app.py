import streamlit as st

import numpy as np
import pandas as pd


st.write('Welcome to my app')

df = pd.DataFrame({
    'first column': list(range(1, 11)),
    'second column': np.arange(10, 101, 10)
})

# this slider allows the user to select a number of lines
# to display in the dataframe
# the selected value is returned by st.slider
st.echo("below")
line_count = st.slider('Select how many rows', 1, 10, 3)

# and used to select the displayed lines
head_df = df.head(line_count)

head_df
