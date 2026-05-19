import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# 1. 頁面基本設定
st.set_page_config(page_title="參數設定後台", layout="wide")

st.title("⚙️ 系統參數設定與歷史報表")
st.divider()

# 2. 主要佈局：切分為左右兩欄
col_left, col_right = st.columns([1, 1], gap="large")

# --- 左欄：藥丸標籤 + 多行備忘錄 ---
with col_left:
    st.markdown("### 📝 基本配置")
    
    # 藥丸標籤 (st.pills 在 Streamlit 1.35+ 支援，若版本較舊可用 st.segmented_control 或 st.radio 替代)
    category = st.pills(
        "選擇設定維度",
        options=["⚡ 高性能模式", "🌱 節能模式", "🛠️ 自訂模式"],
        default="⚡ 高性能模式"
    )
    
    # 多行備忘錄
    memo = st.text_area(
        "備忘錄 / 變更原因說明",
        placeholder="請輸入此次參數調整的原因或備忘紀錄...",
        height=120
    )

# --- 右欄：滑動開關 + 動態數字計數器 ---
with col_right:
    st.markdown("### 🎛️ 進階控制")
    
    # 滑動開關
    enable_threshold = st.toggle("開啟監控閾值限制", value=False)
    
    # 條件判斷：開啟時才顯示數字計數器
    if enable_threshold:
        threshold_value = st.number_input(
            "請設定觸發閾值 (單位: %)",
            min_value=0,
            max_value=100,
            value=80,
            step=5,
            help="當數值超過此閾值時，系統將發送自動告警。"
        )
        st.caption(f"💡 目前已鎖定閾值：:red[{threshold_value}%]")
    else:
        st.caption("🔒 監控閾值已關閉，目前使用系統預設值。")

st.divider()

# 3. 最下方：展示模擬歷史設定報表
st.markdown("### 📊 歷史設定變更報表")

# 建立模擬的歷史數據
today = datetime.now()
mock_data = {
    "變更時間": [
        (today - timedelta(days=1)).strftime("%Y-%m-%d %H:%M"),
        (today - timedelta(days=3)).strftime("%Y-%m-%d %H:%M"),
        (today - timedelta(days=5)).strftime("%Y-%m-%d %H:%M"),
        (today - timedelta(days=7)).strftime("%Y-%m-%d %H:%M"),
    ],
    "設定維度": ["⚡ 高性能模式", "🌱 節能模式", "⚡ 高性能模式", "🛠️ 自訂模式"],
    "監控狀態": ["開啟", "關閉", "開啟", "開啟"],
    "閾值設定": ["85%", "N/A", "80%", "90%"],
    "操作人員": ["Alex", "Bob", "Alex", "Cindy"],
    "備忘錄說明": [
        "因應伺服器高峰期調整",
        "週末離峰時段切換節能",
        "例行性系統效能最佳化",
        "測試自訂排程變更"
    ]
}

df = pd.DataFrame(mock_data)

# 使用 st.dataframe 展示報表，並設定欄位寬度自動調配與容器填滿
st.dataframe(
    df, 
    use_container_width=True, 
    hide_index=True
)
