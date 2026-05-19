import streamlit as st
import datetime

st.set_page_config(page_title="微型 TimeTree", layout="wide")
mode = st.radio("選擇群組" , ["學生" , "老師" , "家長會" , "校友會"], horizontal=True)

# 初始化 session_state 儲存空間
if "mylist" not in st.session_state:
    st.session_state.mylist = []

l, r = st.columns(2)

# 根據群組動態決定卡片背景色
def get_color(group):
    if group == "學生":
        return "#E3F2FD"
    elif group == "老師":
        return "#E6F5D9"
    elif group == "家長會":
        return "#FFF3E0"
    else:
        return "#F3E5F5"

# --- 左欄：輸入區域 ---
with l:
    t1 = st.text_input("行程主旨")
    t3 = st.date_input("日期選擇" , datetime.date.today())
    t4 = st.time_input("時間選擇")
    n1 = st.number_input(
        "行程開始前幾分鐘提醒？",
        min_value=0, max_value=60,
        value=15
    )
    
    if st.button("新增行程", type="primary"):
        if t1.strip() == "":
            st.error("請輸入行程主旨！")
        else:
            st.session_state.mylist.append({
                "group": mode,
                "title": t1,
                "date": str(t3),
                "time": str(t4)[:5], # 只取到時:分，畫面比較乾淨
                "remind": n1
            })
            # ✨ 關鍵：新增後立刻強制重新整理網頁，讓右欄即時同步
            st.rerun()

# --- 右欄：顯示區域 ---
with r:
    st.write("### 📋 目前排程看板")
    with st.container(border=True):
        if not st.session_state.mylist:
            st.caption("目前尚無任何行程，請由左側新增。")
            
        for item in st.session_state.mylist:
            color = get_color(item["group"])
       
            # 優化：加上 color: #333333 確保文字在淺色背景下的強烈對比度
            st.markdown(f"""
            <div style="
                background-color:{color};
                color: #333333;
                padding:15px;
                border-radius:12px;
                margin-bottom:10px;
                box-shadow: 1px 1px 5px rgba(0,0,0,0.05);
            ">
                <span style="font-weight: bold; background: rgba(255,255,255,0.6); padding: 2px 8px; border-radius: 6px; font-size: 13px;">{item["group"]}</span>
                <h4 style="margin: 8px 0 4px 0; color: #111111;">📌 {item["title"]}</h4>
                <div style="font-size: 14px; line-height: 1.5;">
                    📅 <b>日期：</b> {item["date"]}<br>
                    ⏰ <b>時間：</b> {item["time"]}<br>
                    🔔 <b>提醒：</b> 提前 {item["remind"]} 分鐘
                </div>
            </div>
            """, unsafe_allow_html=True)
