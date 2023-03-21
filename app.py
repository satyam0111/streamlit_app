import streamlit as st
import pandas as pd
st.write("""Travify - Place Recommendation Sytem""")
st.write("""\tExplore the beauty with us """)
df = pd.read_csv("data_places.csv") 
city = st.text_input('Where to ')
# st.write('You want to go', city)
condition = df['City'] == city
new_data = df[condition]

# reading the data and displaying the corresponding
col1_values = new_data['Place'].tolist()
col2_values = new_data['City'].tolist()
st.write("""Places you can visit in """,city)
for i in range(len(col1_values)):
  st.write(col1_values[i])
