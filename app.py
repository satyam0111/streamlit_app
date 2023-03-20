import streamlit as st
import pandas as pd
st.write("""First App""")
df = pd.read_csv("data_places.csv") 
city = st.text_input('Where to ')
st.write('You want to go', city)
condition = df['City'] == city
new_data = df[condition]

col1_values = new_data['Place'].tolist()
col2_values = new_data['City'].tolist()
for i in range(len(col1_values)):
  st.write(col1_values[i],"\t\t\t",col2_values[i])

 
from googlesearch import search

query = st.text_input('Enter your query:')
num_results = st.slider('Number of results to display:', value=10, min_value=1, max_value=50)

if st.button('Search'):
    st.write(f'Searching for "{query}"...')
    results = search(query, num_results=num_results)
    for result in results:
        st.write(result)
