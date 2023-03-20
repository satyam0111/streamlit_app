import streamlit as st
import pandas as pd
st.write("""First App""")
df = pd.read_csv("data_places.csv") 
st.write(df.head())
city = st.text_input('Where to ')
st.write('You want to go', city)
condition = df['City'] == city
new_data = df[condition]
place=new_data['Place']
col_values = new_data['Place'].tolist()
for values in col_values:
  st.write(values)
