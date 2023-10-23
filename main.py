import streamlit as st
import requests

api_key = '54NWkU17GwLzxNUfs0cRaADljkyt3ySBBmPiiyV5'
url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}'

response = requests.get(url)
data = response.json()

title = data["title"]
image_url = data['hdurl']
date = data["date"]
content = data['explanation']


st.title(title)
st.image(image_url)
st.subheader(date)
st.write(content)