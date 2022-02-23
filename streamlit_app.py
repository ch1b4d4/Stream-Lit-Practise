import streamlit as st
import pandas as pd
import numpy as np


st.title('PROFILING GREENHOUSE GAS EMISSIONS IN RELATION TO POLLUTION LEVELS IN EUROPEAN COUNTRIES')
st.write(" This is a comment line")


historical_emissions = ('https://github.com/ch1b4d4/Stream-Lit-Practise/blob/main/historical_emissions.csv')

df = pd.DataFrame(historical_emissions)

st.dataframe(df)




