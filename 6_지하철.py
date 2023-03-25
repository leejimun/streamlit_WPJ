import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import json
import folium
from pyparsing import empty
from streamlit_folium import st_folium
from streamlit_echarts import st_echarts


st.set_page_config(
    page_icon= ':wheelchair:')

# 서울

df1 = pd.read_csv('datas/서울휠체어리프트 현황.csv', encoding='cp949')

df1.set_index('역명', drop=True, inplace=True)
st.subheader('서울 지하철 역별 휠체어리프트 현황')
st.bar_chart(df1[['운행']])

# 부산
df5 = pd.read_csv('datas/부산휠체어리프트 현황.csv', encoding='cp949')

df5.set_index('역명', drop=True, inplace=True)
st.subheader('부산 지하철 역별 휠체어리프트 현황')
st.bar_chart(df5[['미운행','운행']])

# 인천
df2 = pd.read_csv('datas/인천휠체어리프트 현황.csv', encoding='cp949')

df2.set_index('역명', drop=True, inplace=True)
st.subheader('인천 지하철 역별 휠체어리프트 현황')
st.bar_chart(df2[['운행']])

# 대구
df3 = pd.read_csv('datas/대구휠체어리프트 현황.csv', encoding='cp949')

df3.set_index('역명', drop=True, inplace=True)
st.subheader('대구 지하철 역별 휠체어리프트 현황')
st.bar_chart(df3[['운행']])

# 광주
df4 = pd.read_csv('datas/광주휠체어리프트 현황.csv', encoding='cp949')

df4.set_index('역명', drop=True, inplace=True)
st.subheader('광주 지하철 역별 휠체어리프트 현황')
st.bar_chart(df4[['운행']])
