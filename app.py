import streamlit as st

# 1. 頁面設定
st.set_page_config(page_title="微型 TimeTree", layout="wide")

# 2. 側邊欄
with st.sidebar:
    st.write("### 行事曆群組")
    st.radio("選擇群組", ["工作", "家庭"])

# 3. 主要內容區（三欄佈局）
col_left, col_center, col_right = st.columns([1, 2, 1.2], gap="large")

with col_left: 
    st.write("### 新增區") 
    st.button("按鈕放左邊")

with col_center: 
    st.write("### 看板區") 
    st.info("主要行程訊息放中間")

with col_right: 
    st.write("### 設定區") 
    st.button("控制項放右邊")

# 4. 下方行程卡片
with st.container(border=True): 
    st.write("**標題：** 開學典禮") 
    st.write("**時間：** 09:00")
