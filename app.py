import streamlit as st
import pandas as pd
st.write("""First App""")
df = pd.read_csv("data_places.csv") 
st.write(df.head())
city = st.text_input('Where to ')
st.write('You want to go', city)
condition = df['City'] == city
new_data= df[condition]

column_names = df.columns.tolist()
selected_column = st.selectbox("Select column to display", column_names)
st.write(df[selected_column])
