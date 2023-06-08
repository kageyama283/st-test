import streamlit as st
import requests

url = 'https://jsonplaceholder.typicode.com/posts/1'

page = st.sidebar.selectbox('Choose your app',['Scraiping','Adtasukaru'])
if page == 'Scraiping':
    st.title('Scraiping Page')
    scraiping = st.button('スクレイピング開始')

    if scraiping:
        st.write('スクレイピングを開始します。')

elif page == 'Adtasukaru':
    st.title('Adatasukaru Page')

st.write('opened')
start = st.button('start','start')

if start:
    res = requests.get(url)
    st.write(res.json())