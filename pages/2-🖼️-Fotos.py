import streamlit as st
from PIL import Image

image1 = Image.open("./media/img1.jpeg")
image2 = Image.open("./media/img2.jpeg")
image3 = Image.open("./media/img3.jpeg")

st.set_page_config(
         page_title="Treinamento Funcional - Fotos", #1
         page_icon="🏋️‍♀️", #2
         initial_sidebar_state="expanded", #4

     )
st.header("Treinamento funcional para uma vida sem sedentarismo :woman-running:")

st.image(image1)
st.image(image2)
st.image(image3)