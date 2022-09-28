import streamlit as st
#写真用
from PIL import Image
# #お天気APIを取得
import requests
# #GUIアプリの作成
# import tkinter as tk
from time import sleep
from datetime import datetime
bi = 0
st.title('Brain training m2')

text = st.text_input('あなたの名前を教えて下さい')
condition = st.slider('難易度を選んでください', 1, 5, 1)

button1 = st.button('ルールについて')

readychk = False

st.write('Are you ready to start Level', condition, 'training?')

a = ("Arial black", 20, "bold")

class gen_f:
    def __init__(self):
        self.flag = False
    def __call__(self):
        if self.flag:
            self.flag = True
            return False
        else:
            return True
 
f = gen_f()
if button1 == True:
    button1 = print(f()) # => True
    if condition == 1:
        st.write('rule1')
    elif condition == 2:
        st.write('rule2')
    elif condition == 3:
        st.write('rule3')
    elif condition == 4:
        st.write('rule4')
    else:
        st.write('rule5')   

