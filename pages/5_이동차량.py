import plotly.graph_objects as go
import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(
    page_icon= ':wheelchair:')


left_column,right_column = st.columns(2)

with left_column:
    st.title('이동지원차량')
    image = Image.open('datas/image/이동지원차량.png')
    st.image(image)

with right_column:
    file_name = '교통약자이동지원_차트용.csv'
    path = "datas/" + file_name
    df = pd.read_csv(path, encoding='cp949')

    df.set_index('시도', drop=True, inplace=True)
    st.markdown("<h6>지역별 이동지원차량 현황 데이터</h6>", unsafe_allow_html=True)
    st.dataframe(df)

st.markdown("<h4 style='text-align: center;'>지역별 이동지원차량 현황</h4>", unsafe_allow_html=True)
st.caption('전국 장애인이동차량 및 차량종류를 지역별로 분석하여 **bar_chart**로 나타내었습니다.')
st.bar_chart(df[['슬로프형차량','리프트형차량','일반차량']])

st.text('')
st.markdown("<h4 style='text-align: center;'>지역별 이동지원차량 위치 현황</h4>", unsafe_allow_html=True)
st.caption('전국 이동지원차량의 위도,경도 좌표를 **st.map**을 활용하여 지도로 나타내었습니다.')
tab1,tab2 = st.tabs(["이동지원차량",' '])

with tab1:
    file_name = '교통약자이동지원.csv'
    path = "datas/" + file_name
    data = pd.read_csv(path, encoding='cp949')

    df = pd.DataFrame({
        'lat': data.위도,
        'lon': data.경도
    })
    st.map(df, zoom=5.5)
