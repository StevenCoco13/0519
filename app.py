import streamlit as st

from datetime import datetime, time

# 1. 頁面初始化與品牌門面 (API 1, 30)

st.set_page_config(page_title="TimeTree 智慧行事曆", layout="wide")

st.toast("TimeTree 系統已成功連線！", icon="")

# 2. 側邊欄群組空間魔術 (API 2, 11, 25)

with st.sidebar:

    st.title(" 行事曆群組")

    st.caption("edit by 闕河正")

    calendar_group = st.radio("切換當前行事曆：", [" 課務行事曆", " 家庭行程", " 個人重點"])

    st.divider() # (API 9)

    st.subheader(" 權限認證")

    vip_code = st.text_input("輸入 VIP 授權碼", type="password", placeholder="填入 VIP999 啟用")

    if vip_code == "VIP999": st.success(" VIP 優先通知權限已開啟！")

# 3. 頂部看板與動態標籤頁 (API 15, 22)

st.title(" TimeTree 智慧自動化行事曆系統")

st.caption("中科推廣部 AI 實戰班專用教材 | 授權標註：edit by 闕河正")

view_mode = st.segmented_control("主看板視角切換：", options=[" 月份大看板", " 條列式清單檢視"], default=" 月份大看板")

st.divider()

# 4. 三欄式核心佈局 (API 3, 10)

col_left, col_center, col_right = st.columns([1, 2, 1.2], gap="large")

# ------------------------------------------

# 左欄：建立新行程 (API 12, 13, 14, 16, 17, 23, 26, 27)

# ------------------------------------------

with col_left:

    st.subheader(" 建立新行程")

    event_title = st.text_input("行程主旨", placeholder="例如：跨部門 AI 部署會議")

    event_tag = st.pills("行程標籤分類", ["#工作", "#家庭", "#緊急"], default="#工作")

    event_date = st.date_input("選擇日期", datetime.now())

    col_t1, col_t2 = st.columns(2)

    with col_t1: start_time = st.time_input("開始時間", time(9, 0))

    with col_t2: end_time = st.time_input("結束時間", time(10, 0))

    event_color = st.color_picker("行程色彩辨識標籤", "#1A73E8")

    event_note = st.text_area("備忘錄 / 詳細說明")

    

    st.write("") # 呼吸留白 (API 10)

    if st.button("確認加入行事曆", type="primary", use_container_width=True):

        if event_title: st.success(f" 行程【{event_title}】已成功寫入暫存！")

        else: st.error("請填寫行程主旨！")

# ------------------------------------------

# 中欄：行事曆主看板與精美卡片 (API 4, 5, 24, 28, 29)

# ------------------------------------------

with col_center:

    st.subheader(" 當月核心行程看台")

    with st.status("正在與雲端伺服器同步行程...", expanded=False) as status:

        st.write("讀取本週資料庫...")

        status.update(label="同步完畢！呈現最新排程", state="complete")

        

    st.info(f"當前正在檢視：{calendar_group} ({view_mode})")

    

    # 模擬 TimeTree 帶有色彩邊框的高質感 HTML 外觀卡片

    mock_events = [

        {"title": " 闕老師 AI 客服實戰班開課", "date": "2026-05-18", "color": "#E65100", "tag": "#工作"},

        {"title": " 繳交 PhD 研究計畫書草稿", "date": "2026-05-20", "color": "#D32F2F", "tag": "#緊急"}

    ]

    

    # 建立頁籤分流 (API 5)

    tab_active, tab_archived = st.tabs([" 近期行程", " 歷史封存"])

    with tab_active:

        for ev in mock_events:

            with st.container(border=True): # 外框容器 (API 4)

                st.markdown(f"""

                <div style="border-left: 6px solid {ev['color']}; padding-left: 15px; margin: -5px;">

                    <span style="background-color: {ev['color']}22; color: {ev['color']}; padding: 2px 8px; border-radius: 10px; font-size: 11px; font-weight: bold;">{ev['tag']}</span>

                    <h4 style="margin: 5px 0; color: #1A202C;">{ev['title']}</h4>

                    <p style="margin: 0; font-size: 13px; color: #4A5568;"> 日期：{ev['date']}</p>

                </div>

                """, unsafe_allow_html=True) #  修正拼字錯誤

# ------------------------------------------

# 右欄：自動化通知與表格總覽 (API 6, 7, 8, 18, 19, 20, 21)

# ------------------------------------------

with col_right:

    st.subheader(" 24H 郵件自動化設定")

    with st.expander(" 自動發信核心參數設定", expanded=True): # (API 6)

        enable_mail = st.toggle("開啟時間到自動發信通知", value=True)

        remind_min = st.number_input("行程開始前幾分鐘發信？", min_value=0, max_value=60, value=15)

        

    st.divider()

    with st.popover(" 快速進階篩選表格"): # (API 8)

        st.checkbox("顯示已過期行程", value=False)

    st.subheader(" 歷史行程微型資料庫總覽")

    df_data = [

        {"行程名稱": "AI 部署班", "日期": "2026-05-18", "標籤色彩": "#E65100", "已發信": True},

        {"行程名稱": "PhD 計畫書", "日期": "2026-05-20", "標籤色彩": "#D32F2F", "已發信": False},

    ]

    

    #  修正為高相容性的 TextColumn 確保所有舊版本皆不當機

    st.dataframe(

        df_data,

        column_config={

            "標籤色彩": st.column_config.TextColumn("辨識色碼"),

            "已發信": st.column_config.CheckboxColumn("發信狀態"),

            "日期": st.column_config.DateColumn("排定日期", format="YYYY-MM-DD")

        },

        use_container_width=True, hide_index=True

    )

    

    @st.dialog(" 課堂專案公告") # (API 7)

    def show_announcement():

        st.write("今日進度：30 大 API 混和排程版面配置已建構完畢！")

    if st.button(" 查看課堂專案公告", use_container_width=True): show_announcement()
