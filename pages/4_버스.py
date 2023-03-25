import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# 페이지 기본 설정
st.set_page_config(
    page_title= '버스 현황',
    page_icon= ':wheelchair:',
    layout='wide',
    menu_items= {
        'About' : '장애인의 이동보조수단 현황을 나타내는 대시보드입니다.'
    },
    initial_sidebar_state= 'expanded'
)

st.title('버스')
st.subheader('전국 시도별 저상버스 도입 현황')

bus = pd.read_csv('datas/버스.csv', encoding='cp949')
rate = pd.read_csv('datas/도입률.csv', encoding='cp949')
city = pd.read_csv('datas/시내버스.csv', encoding='cp949')
low = pd.read_csv('datas/저상버스.csv', encoding='cp949')

col1 = ['합계(시내)','서울특별시(시내)','부산광역시(시내)','대구광역시(시내)','인천광역시(시내)','광주광역시(시내)','대전광역시(시내)','울산광역시(시내)','세종특별자치시(시내)','경기도(시내)','강원도(시내)','충청북도(시내)','충청남도(시내)','전라북도(시내)','전라남도(시내)','경상북도(시내)','경상남도(시내)','제주특별자치도(시내)']
col2 = ['합계(저상)','서울특별시(저상)','부산광역시(저상)','대구광역시(저상)','인천광역시(저상)','광주광역시(저상)','대전광역시(저상)','울산광역시(저상)','세종특별자치시(저상)','경기도(저상)','강원도(저상)','충청북도(저상)','충청남도(저상)','전라북도(저상)','전라남도(저상)','경상북도(저상)','경상남도(저상)','제주특별자치도(저상)']
col3 = ['합계','서울특별시','부산광역시','대구광역시','인천광역시','광주광역시','대전광역시','울산광역시','세종특별자치시','경기도','강원도','충청북도','충청남도','전라북도','전라남도','경상북도','경상남도','제주특별자치도']

tab0, tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12, tab13, tab14, tab15,tab16, tab17  = st.tabs(['전국','서울','부산','대구','인천','광주','대전','울산','세종','경기','강원','충북','충남','전북','전남','경북','경남','제주'])

bus.set_index('년', drop=True, inplace=True)
rate.set_index('년', drop=True, inplace=True)
st.dataframe(city)
st.dataframe(low)

with tab0:
    st.bar_chart(bus[[col1[0], col2[0]]])
    st.line_chart(rate[[col3[0]]])
with tab1:
    st.bar_chart(bus[[col1[1], col2[1]]])
    st.line_chart(rate[[col3[1]]])
with tab2:
    st.bar_chart(bus[[col1[2], col2[2]]])
    st.line_chart(rate[[col3[2]]])
with tab3:
    st.bar_chart(bus[[col1[3], col2[3]]])
    st.line_chart(rate[[col3[3]]])
with tab4:
    st.bar_chart(bus[[col1[4], col2[4]]])
    st.line_chart(rate[[col3[4]]])
with tab5:
    st.bar_chart(bus[[col1[5], col2[5]]])
    st.line_chart(rate[[col3[5]]])
with tab6:
    st.bar_chart(bus[[col1[6], col2[6]]])
    st.line_chart(rate[[col3[6]]])
with tab7:
    st.bar_chart(bus[[col1[7], col2[7]]])
    st.line_chart(rate[[col3[7]]])
with tab8:
    st.bar_chart(bus[[col1[8], col2[8]]])
    st.line_chart(rate[[col3[8]]])
with tab9:
    st.bar_chart(bus[[col1[9], col2[9]]])
    st.line_chart(rate[[col3[9]]])
with tab10:
    st.bar_chart(bus[[col1[10], col2[10]]])
    st.line_chart(rate[[col3[10]]])
with tab11:
    st.bar_chart(bus[[col1[11], col2[1]]])
    st.line_chart(rate[[col3[11]]])
with tab12:
    st.bar_chart(bus[[col1[12], col2[12]]])
    st.line_chart(rate[[col3[12]]])
with tab13:
    st.bar_chart(bus[[col1[13], col2[13]]])
    st.line_chart(rate[[col3[13]]])
with tab14:
    st.bar_chart(bus[[col1[14], col2[14]]])
    st.line_chart(rate[[col3[14]]])
with tab15:
    st.bar_chart(bus[[col1[15], col2[15]]])
    st.line_chart(rate[[col3[15]]])
with tab16:
    st.bar_chart(bus[[col1[16], col2[16]]])
    st.line_chart(rate[[col3[16]]])
with tab17:
    st.bar_chart(bus[[col1[17], col2[17]]])
    st.line_chart(rate[[col3[17]]])