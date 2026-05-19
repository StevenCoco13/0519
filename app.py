import streamlit as st
import datetime

st.set_page_config(page_title="微型 TimeTree", layout="wide")
mode = st.radio("選擇群組" , ["學生" , "老師" , "家長會" , "校友會"], horizontal=True)

# 初始化 session_state
if "mylist" not in st.session_state:
    st.session_state.mylist = []

l, r = st.columns(2)

def get_color(group):
    if group == "學生":
        return "#E3F2FD"
    elif group == "老師":
        return "#E6F5D9"
    elif group == "家長會":
        return "#FFF3E0"
    else:
        return "#F3E5F5"

# --- 左欄：操作配置區 ---
with l:
    st.subheader("➕ 新增行程")
    t1 = st.text_input("行程主旨")
    t3 = st.date_input("日期選擇", datetime.date.today())
    t4 = st.time_input("時間選擇")
    n1 = st.number_input("行程開始前幾分鐘提醒？", min_value=0, max_value=60, value=15)
    
    if st.button("確認新增行程", type="primary"):
        if t1.strip() == "":
            st.error("請填寫行程主旨！")
        else:
            st.session_state.mylist.append({
                "group": mode,
                "title": t1,
                "date": str(t3),
                "time": str(t4)[:5],
                "remind": n1
            })
            st.rerun()  # ✨ 刪除/新增後立即刷新網頁
            
    st.divider()
    
    # 🗑️ 安全的刪除功能區
    st.subheader("🗑️ 刪除行程")
    list_length = len(st.session_state.mylist)
    
    if list_length > 0:
        # ✨ 關鍵防錯：動態計算 max_value，確保當有資料時才允許設定最大索引值
        ni = st.number_input(
            "請輸入要刪除的行程編號", 
            min_value=0, 
            max_value=list_length - 1, 
            value=0,
            step=1
        )
        if st.button("確認刪除該行程", type="secondary"):
            del st.session_state.mylist[ni]
            st.rerun()  # ✨ 刪除後立即刷新網頁
    else:
        st.info("目前無任何行程可供刪除。")

# --- 右欄：看板顯示區 ---
with r:
    st.subheader("📋 目前排程看板")
    with st.container(border=True):
        if not st.session_state.mylist:
            st.caption("目前尚無任何行程。")
            
        # 使用 enumerate 同時抓出 index(編號) 與 內容，方便使用者識別要刪哪一條
        for idx, item in enumerate(st.session_state.mylist):
            color = get_color(item["group"])
       
            st.markdown(f"""
            <div style="
                background-color:{color};
                color: #333333;
                padding:15px;
                border-radius:12px;
                margin-bottom:10px;
                position: relative;
            ">
                <!-- 在卡片右上角貼上編號標籤 -->
                <div style="
                    position: absolute; 
                    top: 10px; 
                    right: 15px; 
                    background: rgba(0,0,0,0.1); 
                    padding: 2px 8px; 
                    border-radius: 20px; 
                    font-size: 12px; 
                    font-weight: bold;
                ">
                    編號 #{idx}
                </div>
                
                <span style="font-weight: bold; background: rgba(255,255,255,0.6); padding: 2px 6px; border-radius: 4px; font-size: 12px;">
                    {item["group"]}
                </span>
                <h4 style="margin: 8px 0 4px 0; color: #111111;">📌 {item["title"]}</h4>
                <div style="font-size: 14px;">
                    📅 <b>日期：</b> {item["date"]}<br>
                    ⏰ <b>時間：</b> {item["time"]}<br>
                    🔔 <b>提醒：</b> 提前 {item["remind"]} 分鐘
                </div>
            </div>
            """, unsafe_allow_html=True)
