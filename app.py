import streamlit as st
import pandas as pd
st.write("""First App""")
df = pd.read_csv("data_places.csv") 
st.write(df)
city = st.text_input('Where to ', 'City')
st.write('You want to go', city)
