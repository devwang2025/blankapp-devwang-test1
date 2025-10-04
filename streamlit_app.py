import streamlit as st

st.title("🎈 Streamlit 요소 데모 페이지")
st.header("기본 텍스트 요소")
st.subheader("서브헤더 예시")
st.text("텍스트 예시")
st.markdown("**마크다운** _예시_ :sparkles:")
st.code("print('Hello Streamlit!')", language="python")
st.latex(r"E = mc^2")

st.header("데이터 표시")
import pandas as pd
import numpy as np
df = pd.DataFrame(
    np.random.randn(5, 3),
    columns=['a', 'b', 'c']
)
st.dataframe(df)
st.table(df.head(3))
st.json({"name": "Streamlit", "type": "Demo", "items": [1,2,3]})

st.header("미디어 요소")
st.image(
    "https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png",
    caption="Streamlit 로고"
)
st.audio(
    np.random.uniform(-1, 1, 44100),
    format='audio/wav',
    sample_rate=44100
)
st.video(
    "https://www.youtube.com/watch?v=B2iAodr0fOo"
)

st.header("인터랙티브 위젯")
st.button("버튼")
st.checkbox("체크박스")
st.radio("라디오 버튼", ["A", "B", "C"])
st.selectbox("셀렉트박스", ["Apple", "Banana", "Cherry"])
st.multiselect("멀티셀렉트", ["Python", "Java", "C++"])
st.slider("슬라이더", 0, 100, 50)
st.number_input("숫자 입력", min_value=0, max_value=100, value=10)
st.text_input("텍스트 입력", "기본값")
st.text_area("텍스트 영역", "여러 줄 입력")
st.date_input("날짜 입력")
st.time_input("시간 입력")
st.file_uploader("파일 업로더")

st.header("상태 및 진행")
st.progress(70)
st.spinner("로딩 중...")
st.success("성공 메시지")
st.info("정보 메시지")
st.warning("경고 메시지")
st.error("에러 메시지")

st.header("사이드바")
st.sidebar.title("사이드바 타이틀")
st.sidebar.button("사이드바 버튼")
st.sidebar.selectbox("사이드바 셀렉트박스", ["옵션1", "옵션2"])

st.header("플로팅 및 레이아웃")
col1, col2 = st.columns(2)
col1.button("왼쪽 버튼")
col2.button("오른쪽 버튼")

with st.expander("더보기 (Expander)"):
    st.write("숨겨진 내용입니다.")
