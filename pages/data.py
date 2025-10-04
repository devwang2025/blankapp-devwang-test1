import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# 한글 폰트 설정 (NanumGothic-Regular.ttf)
font_path = os.path.join(os.path.dirname(__file__), '..', 'fonts', 'NanumGothic-Regular.ttf')
fontprop = fm.FontProperties(fname=font_path)
plt.rc('font', family=fontprop.get_name())
plt.rcParams['axes.unicode_minus'] = False

st.title("데이터 분석 및 시각화 예시")

# 데이터 샘플 생성
st.header("샘플 데이터")
df = pd.DataFrame({
	'연도': [2020, 2021, 2022, 2023, 2024],
	'매출': [100, 150, 130, 170, 200],
	'고객수': [50, 65, 60, 80, 90]
})
st.dataframe(df)

# 간단한 통계 분석
st.header("기초 통계 분석")
st.write("매출 평균:", df['매출'].mean())
st.write("고객수 최대값:", df['고객수'].max())

# 시각화 예시
st.header("매출 추이 (라인 차트)")
st.line_chart(df.set_index('연도')['매출'])

st.header("고객수 추이 (바 차트)")
st.bar_chart(df.set_index('연도')['고객수'])

# Matplotlib 활용 예시
st.header("매출과 고객수 산점도 (Matplotlib)")
fig, ax = plt.subplots()
ax.scatter(df['매출'], df['고객수'])
ax.set_xlabel('매출', fontproperties=fontprop)
ax.set_ylabel('고객수', fontproperties=fontprop)
ax.set_title('매출 vs 고객수', fontproperties=fontprop)
st.pyplot(fig)
