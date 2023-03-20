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


import requests

search_item = st.text_input("Enter search query")

# Fetch search results page
url = f"https://www.google.com/search?q={search_item}"
page = requests.get(url)


# Find all search result links and print them
results = soup.find_all("div", class_="BNeawe vvjwJb AP7Wnd")
for result in results:
    st.write(result.get_text())
