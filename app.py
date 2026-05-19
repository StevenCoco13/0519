import streamlit as st
st.set_page_config(page_title="微型 TimeTree", layout="wide")

with st.sidebar:
    st.write("###  行事曆群組")
    st.radio("選擇群組", ["工作", "家庭"])


with st.container(border=True): 
    st.write(" 標題：開學典禮") 
    st.write(" 時間：09:00")
