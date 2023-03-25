import streamlit as st
import pandas as pd
import plotly
from PIL import Image

st.set_page_config(
    page_icon= ':wheelchair:')

left_column,right_column = st.columns(2)
with left_column:
    st.title('육교')
    image = Image.open('datas\image\육교.png')

    st.image(image)

with right_column:
    file_name = '육교_차트용.csv'
    path = "datas\\" + file_name
    df = pd.read_csv(path, encoding='cp949')

    df.set_index('시도', drop=True, inplace=True)
    st.markdown("<h6>지역별 육교 현황 데이터</h6>", unsafe_allow_html=True)
    st.dataframe(df)

st.markdown("<h4 style='text-align: center;'>지역별 육교 현황</h4>", unsafe_allow_html=True)
st.caption('전국 육교 및 장애인이동보조수단을 지역별로 분석하여 **bar_chart**로 나타내었습니다.')
st.bar_chart(df[['엘리베이터', '경사로', '점자블럭']])


st.text('')
st.markdown("<h4 style='text-align: center;'>지역별 육교 및 이동보조수단 위치 현황</h4>", unsafe_allow_html=True)
st.caption('전국 육교 및 장애인이동보조수단의 위도,경도 좌표를 **st.map**을 활용하여 지도로 나타내었습니다.')
tab1, tab2, tab3, tab4 = st.tabs(["육교", "엘리베이터", "경사로",'점자블럭'])

with tab1:

    file_name = '육교.csv'
    path = "datas\\" + file_name

    data = pd.read_csv(path, encoding='cp949')

    print(data.columns)

    df = pd.DataFrame({
        'lat': data.위도,
        'lon': data.경도
    })
    st.map(df, zoom=5.5)

with tab2:

    file_name = '육교_엘리베이터.csv'
    path = "datas\\" + file_name

    data = pd.read_csv(path, encoding='cp949')

    df = pd.DataFrame({
        'lat': data.위도,
        'lon': data.경도
    })
    st.map(df, zoom=5.5)

    st.text('')
    st.subheader('참고사진')
    image = Image.open('datas\image\육교_엘리베이터.jpg')
    st.image(image)
    st.caption('출처: http://www.daejonilbo.com/news/articleView.html?idxno=1494074')

with tab3:

    file_name = '육교_경사로.csv'
    path = "datas\\" + file_name

    data = pd.read_csv(path, encoding='cp949')

    df = pd.DataFrame({
        'lat': data.위도,
        'lon': data.경도
    })
    st.map(df, zoom=5.5)

    st.text('')
    st.subheader('참고사진')
    image = Image.open('datas\image\육교_경사로.jpg')
    st.image(image)
    st.caption('출처: https://www.ohmynews.com/NWS_Web/View/at_pg.aspx?CNTN_CD=A0000970676')

with tab4:

    file_name = '육교_점자블럭.csv'
    path = "datas\\" + file_name

    data = pd.read_csv(path, encoding='cp949')

    print(data.columns)

    df = pd.DataFrame({
        'lat': data.위도,
        'lon': data.경도
    })
    st.map(df, zoom=5.5)

    st.text('')
    st.subheader('참고사진')
    image = Image.open('datas\image\육교_점자블록.jpg')
    st.image(image)
    st.caption('출처: http://midammall.kr/board/bbs/board.php?bo_table=4_case_1&wr_id=158&page=3')