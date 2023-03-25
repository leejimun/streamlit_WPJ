import streamlit as st
import pandas as pd
import plotly
from PIL import Image

st.set_page_config(
    page_icon= ':wheelchair:')

left_column,right_column = st.columns(2)
with left_column:
    st.title('신호등')
    st.text('')

    image = Image.open('D:/workspace/pythonProject1/datas/image/보행자신호등.png')
    # 이미지 크기 줄이기
    width, height = image.size
    max_size = 200
    if width > max_size or height > max_size:
        ratio = max_size / max(width, height)
        image = image.resize((int(width * ratio), int(height * ratio)))
    st.image(image)

with right_column:
    file_name = '신호등_차트용.csv'
    path = "D:/workspace/pythonProject1/datas//" + file_name
    df = pd.read_csv(path, encoding='cp949')

    df.set_index('시도명', drop=True, inplace=True)
    st.markdown("<h6>지역별 신호등 현황 데이터</h6>", unsafe_allow_html=True)
    st.dataframe(df)

st.text('')
st.markdown("<h4 style='text-align: center;'>지역별 신호등 현황</h4>", unsafe_allow_html=True)
st.caption('전국 보행자신호등 및 장애인이동보조수단을 지역별로 분석하여 **bar_chart**로 나타내었습니다.')
st.bar_chart(df[['보행자작동신호기유무', '시각장애인용음향신호기유무', '일반보행자신호등']])
st.text('')
st.markdown("<h4 style='text-align: center;'>지역별 신호등 및 이동보조수단 위치 현황</h4>", unsafe_allow_html=True)
st.caption('전국 보행자신호등 및 장애인이동보조수단의 위도,경도 좌표를 **st.map**을 활용하여 지도로 나타내었습니다.')
tab1, tab2, tab3 = st.tabs(["보행자신호등", "보행자작동신호기", "음향신호기"])

with tab1:

    file_name = '보행자신호등.csv'
    path = "D:/workspace/pythonProject1/datas//" + file_name

    data = pd.read_csv(path, encoding='cp949')

    print(data.columns)

    df = pd.DataFrame({
        'lat': data.위도,
        'lon': data.경도
    })
    st.map(df, zoom=5.5)

with tab2:

    file_name = '보행자작동신호기_신호등.csv'
    path = "D:/workspace/pythonProject1/datas//" + file_name

    data = pd.read_csv(path, encoding='cp949')

    df = pd.DataFrame({
        'lat': data.위도,
        'lon': data.경도
    })
    st.map(df, zoom=5.5)
    st.text('')
    st.subheader('참고사진')
    image = Image.open('D:/workspace/pythonProject1/datas/image/보행자작동신호기.png')
    st.image(image)
    st.caption('출처: http://www.safetimes.co.kr/news/articleView.html?idxno=112032')
with tab3:

    file_name = '음향신호기_신호등.csv'
    path = "D:/workspace/pythonProject1/datas//" + file_name

    data = pd.read_csv(path, encoding='cp949')

    df = pd.DataFrame({
        'lat': data.위도,
        'lon': data.경도
    })
    st.map(df, zoom=5.5)
    st.text('')
    st.subheader('참고사진')
    image = Image.open('D:/workspace/pythonProject1/datas/image/음향신호기.jpg')
    st.image(image)
    st.caption('출처: http://www.globalnewsagency.kr/news/articleView.html?idxno=96173')
