import streamlit as st
import requests
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


url = 'https://jsonplaceholder.typicode.com/posts/1'
adtasukaru = 'https://tools.adtasukaru.com/'

page = st.sidebar.selectbox('Choose your app',['Scraiping','Adtasukaru'])
if page == 'Scraiping':
    st.title('Scraiping Page')

elif page == 'Adtasukaru':
    st.title('Adatasukaru Page')

    system = st.button('アドタスカルのシステム開始')

    if system:
        st.write('アドタスカルのシステムを開始します。')
        st.write(datetime.datetime.now())

        browser = webdriver.Chrome()
        browser.get(adtasukaru)

        elem_class =  browser.find_elements(By.CLASS_NAME , 'el-input__inner')
        elem_btn = browser.find_element(By.CLASS_NAME,'el-button')
        elem_class[0].send_keys('listing@suprieve.com')
        elem_class[1].send_keys('I1JslzZM9j')
        # 1秒待つ
        time.sleep(1)
        # ログインボタンをクリック
        elem_btn.click()

st.write('opened')
start = st.button('start','start')

if start:
    res = requests.get(url)
    st.write(res.json())