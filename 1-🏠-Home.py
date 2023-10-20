import streamlit as st
from PIL import Image

image = Image.open("./media/img3.jpeg")
st.set_page_config(
         page_title="Treinamento Funcional", #1
         page_icon="🏋️‍♀️", #2
         initial_sidebar_state="expanded", #4

     )
st.title("Treinamento funcional para uma vida sem sedentarismo :woman-running:")

st.image(image)

st.write("""
O Projeto Treinamento funcional Para Uma Vida Sem Sedentarismo foi desenvolvido com o pensamento voltado para as senhoras e jovens da comunidade da Vila De Fogareiro, distrito de Passagem, que viviam uma vida sedentária, sem nenhuma prática de exercício físico/atividade física. O projeto tem o intuito de fazer com que as mulheres da comunidade pudessem manter e aderir um estilo de vida saudável com a realização de determinadas atividades dentro da condição corporal de cada mulher, auxiliando assim para a prevenção de doenças.
         """)