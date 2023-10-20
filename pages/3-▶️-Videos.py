import streamlit as st

st.set_page_config(
         page_title="Treinamento Funcional - Videos", #1
         page_icon="🏋️‍♀️", #2
         initial_sidebar_state="expanded", #4
     )

video_file1 = open('./media/video1.mp4', 'rb')
video_file2 = open('./media/video2.mp4', 'rb')
video_bytes1 = video_file1.read()
video_bytes2 = video_file2.read()


st.header("Treinamento funcional para uma vida sem sedentarismo :woman-running:")

st.video(video_bytes1)
st.video(video_bytes2)