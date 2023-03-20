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
new_list=place.rows.tolist()
for values in new_list:
  st.write(values)
