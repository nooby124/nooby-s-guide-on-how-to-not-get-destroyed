import streamlit as st
from PIL import Image

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.title('A simple guide on how to not get roasted very hard by the entire class chat:')
st.write('1. exist')
st.write('2. touch grass')
st.write('3. dont send this message in the class group chat:')
image = Image.open('ha.png')

st.image(image)

st.title('thats it!')
st.write('---')
st.write("[anyways view the source code here!](https://github.com/nooby124/nooby-s-guide-on-how-to-not-get-destroyed)")
st.write('---')
st.write('this website is just a joke for anyone who is not from my class but seriously dont say that in any group chat. for the guys that are in my class: this is very serious please take these things very personally. (looking at u mr a.a).')
