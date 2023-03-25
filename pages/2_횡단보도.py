import plotly.graph_objects as go
import streamlit as st
import pandas as pd
import plotly
import altair as alt
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image



left_column,right_column = st.columns(2)
with left_column:
    st.title('횡단보도')
    st.text('')
    image = Image.open('datas\image\횡단보도.png')

    st.image(image)

with right_column:
    file_name = '횡단보도_차트용.csv'
    path = "datas\\" + file_name
    df = pd.read_csv(path, encoding='cp949')

    df.set_index('시도명', drop=True, inplace=True)
    st.markdown("<h6>지역별 횡단보도 현황 데이터</h6>", unsafe_allow_html=True)
    st.dataframe(df)

st.markdown("<h4 style='text-align: center;'>지역별 횡단보도 현황</h4>", unsafe_allow_html=True)
st.caption('전국 횡단보도 및 장애인이동보조수단을 지역별로 분석하여 **bar_chart**로 나타내었습니다.')
st.bar_chart(df[['보행자신호등유무','보도턱낮춤여부','점자블록유무']])

st.text('')
st.markdown("<h4 style='text-align: center;'>지역별 횡단보도 및 이동보조수단 위치 현황</h4>", unsafe_allow_html=True)
st.caption('전국 횡단보도 및 장애인이동보조수단의 위도,경도 좌표를 **st.map**을 활용하여 지도로 나타내었습니다.')
tab1, tab2, tab3, tab4 = st.tabs(["전체", "보행자신호등", "보도턱낮춤", "점자블록"])

with tab1:
    file_name = '횡단보도.csv'
    path = "datas\\" + file_name
    data = pd.read_csv(path, encoding='cp949')

    df = pd.DataFrame({
        'lat': data.위도,
        'lon': data.경도
    })

    st.map(df, zoom=5.5)

with tab2:

    file_name = '보행자신호등_횡단보도.csv'
    path = "datas\\" + file_name
    data = pd.read_csv(path, encoding='cp949')

    df = pd.DataFrame({
        'lat': data.위도,
        'lon': data.경도
    })
    st.map(df, zoom=5.5)

    st.text('')
    st.subheader('참고사진')
    image = Image.open('datas\image\보행자신호등_횡단보도.png')
    st.image(image)
    st.caption('출처: https://blog.bullsone.com/2278')

with tab3:

    file_name = '보도턱낮춤_횡단보도.csv'
    path = "datas\\" + file_name

    data = pd.read_csv(path, encoding='cp949')

    df = pd.DataFrame({
        'lat': data.위도,
        'lon': data.경도
    })
    st.map(df, zoom=5.5)
    st.text('')
    st.subheader('참고사진')
    image = Image.open('datas\image\보도턱낮춤.jpeg')
    st.image(image)
    st.caption('출처: https://m.yna.co.kr/view/AKR20150423018300004')

with tab4:

    file_name = '점자블록_횡단보도.csv'
    path = "datas\\" + file_name

    data = pd.read_csv(path, encoding='cp949')

    df = pd.DataFrame({
        'lat': data.위도,
        'lon': data.경도
    })
    st.map(df, zoom=5.5)

    st.text('')
    st.subheader('참고사진')
    image = Image.open('datas\image\횡단보도_점자블록.jpg')
    st.image(image)
    st.caption('출처: http://www.safetimes.co.kr/news/articleView.html?idxno=201809')