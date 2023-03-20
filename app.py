import streamlit as st
import pandas as pd
st.write("""First App""")
data = pd.read_csv("data_places.csv") 
st.write(data.head())
city = st.text_input('Where to ')
st.write('You want to go', city)
condition = data['City'] == city
new_data = data[condition]

column_names = df.columns.tolist()
selected_column = st.selectbox("Select column to display", columns_names)
st.write(df[selected_column])
