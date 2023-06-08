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
        now = datetime.datetime.now()
        year = now.year
        month = now.month
        day = now.day
        hour = now.hour
        minute = now.minute
        second = now.second
        if month < 10:
            month = '0' + str(month)
        if day < 10:
            day = '0' + str(day)
        today_now = str(year) + '/' + str(month) + '/' + str(day) + ' ' + str(hour) + '：' + str(minute) + '：' + str(second)

        st.write(today_now)

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