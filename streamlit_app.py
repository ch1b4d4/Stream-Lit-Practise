
import streamlit as st
import pandas as pd
import numpy as np

st.title('PROFILING GREENHOUSE GAS EMISSIONS IN RELATION TO POLLUTION LEVELS IN EUROPEAN COUNTRIES')
st.write(" This is a comment line")


historical_emissions = ('/Users/la/Downloads/Clean Data/historical_emissions.csv')

def load_data(nrows):
    data = pd.read_csv(historical_emissions, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')

st.subheader('Raw data')
st.write(data)


