import streamlit as st
import datetime

today = st.date_input(
  "選擇日期",
  datetime.date.today()
)

# 1. 頁面基本設定 (API 1: set_page_config)
st.set_page_config(page_title="微型 TimeTree", layout="wide")

# 2. 側邊欄設定 (API 2: sidebar)
with st.sidebar:
    st.write("### 📅 行事曆群組")
    group = st.radio("選擇群組", ["工作", "家庭", "個人學習"])
    st.divider()
    st.write(f"目前檢視：**{group}**")

# 3. 主畫面雙欄佈局 (API 3: columns)
# 依需求切分成左右兩欄，比例為 1:3
col_left, col_right = st.columns([1, 3], gap="large")

# --- 左欄：新增行程的提示區 ---
with col_left:
    st.write("### ➕ 新增行程")
    # 這裡放新增行程的輸入欄位提示
    todo_title = st.text_input("行程名稱", placeholder="例如：開學典禮")
    todo_time = st.text_input("時間", placeholder="例如：09:00")
    
    if st.button("儲存行程", use_container_width=True):
        st.success(f"已成功提示新增：{todo_title}")

# --- 右欄：行程看板區 ---
with col_right:
    st.write("### 📋 行程分頁看板")
    
    # 使用外框容器包裹內容 (API 4: container)
    with st.container(border=True):
        
        # 在容器內部嵌入一組分頁頁籤 (API 5: tabs)
        tab1, tab2 = st.tabs(["📅 本月行程", "🗄️ 已封存行程"])
        
        # 頁籤 1 的內容
        with tab1:
            st.write("#### 這裡顯示本月未完成的行程")
            
            # 您原本的行程卡片範例
            st.info("💡 提示：點擊右側按鈕可進行封存")
            c1, c2 = st.columns([3, 1])
            with c1:
                st.markdown(f"**標題：** 開學典禮 ({group})")
                st.markdown("**時間：** 09:00")
            with c2:
                st.button("封存", key="archive_btn1")
                
        # 頁籤 2 的內容
        with tab2:
            st.write("#### 這裡顯示過去已封存的歷史行程")
            st.caption("目前尚無封存行程...")


title = st.text_input(
  "行程主旨",
  placeholder="請填寫會議名稱..."
)

meeting_time = st.time_input(
  "選擇時間"
)


my_color = st.color_picker(
 "挑選辨識顏色",
 "#1A73E8"
)


view = st.segmented_control(
  "檢視模式",
  ["月視角", "週視角"],
  default="月視角"
)


tag = st.pills(
  "行程屬性",
  ["#工作", "#家庭", "#緊急"]
)


note = st.text_area(
  "行程備忘錄 / 詳細說明"
)
