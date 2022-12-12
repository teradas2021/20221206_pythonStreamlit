import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

# st.title('Streamlit 超入門')

# progressbar
# latest_iteration = st.empty()
# bar = st.progress(0)

# for i in range(100):
#     latest_iteration.text(f'イテレーション{i+1} ')
#     bar.progress(i + 1)
#     time.sleep(0.03)
'Done!'

# st.write('DataFrame')

# df = pd.DataFrame({
#     '１列目':[1, 2, 3, 4],
#     '２列目':[5, 6, 7, 8]
# } )

# st.dataframe(df.style.highlight_max(axis=0), width=800,height=300)

st.title('Streamlit image')

st.write('Display Image')
# img = Image.open('istockphoto-1389845778-612x612.jpg')

if st.checkbox('Show Image'):
    img = Image.open('../images/istockphoto-1444085138-612x612.jpg')
    st.image(img, caption = 'overseas', use_column_width=True)

number = st.selectbox(
    'あなたが好きな数学を選択してください。',
    list(range(1,11))
)
'数字は',number,'です。'

text = st.text_input('あなたの趣味')
'趣味：',text

st.sidebar.title('Sidebar Widget')
condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション：', condition

left_column,right_column = st.columns(2)
button = left_column.button('右からむにボタンを表示')
if button:
    right_column.write('ここは右カラム')

expander1 = st.expander('問い合わせ１')
expander1.write('問い合わせ１の回答１')
expander1.write('問い合わせ１の回答２')
if expander1 == '問い合わせ１の回答１':
    st.write(expander1)
expander1 = st.expander('問い合わせ２')
expander1.write('問い合わせ２の回答')
expander1 = st.expander('問い合わせ３')
expander1.write('問い合わせ３の回答')


