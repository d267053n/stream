import time

import streamlit as st

import numpy as np
import pandas as pd


st.title('This is a demo')

st.write("Create a **Table**：")

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
df

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])
st.line_chart(chart_data)

map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [22.7, 120.3],
    columns=['lat', 'lon'])
st.map(map_data)

if st.checkbox('顯示地圖圖表'):
    map_data = pd.DataFrame(
        np.random.randn(100, 2) / [50, 50] + [22.7, 120.3],
        columns=['lat', 'lon'])
    st.map(map_data)

    
option = st.selectbox(
    '你喜歡哪種動物？',
    ['狗', '貓', '鸚鵡', '天竺鼠'])
'你的答案：', option

left_column, right_column = st.beta_columns(2)
left_column.write("這是左邊欄位。")
right_column.write("這是右邊欄位。")

# 增加一個空白元件，等等要放文字
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'目前進度 {i+1} %')
    bar.progress(i + 1)
    time.sleep(0.1)
