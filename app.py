import streamlit as st

st.set_page_config(
    page_title="매출·재고 조회 챗봇",
    page_icon="📊"
)

st.title("📊 매출·재고 조회 챗봇")
st.write("자연어로 매출, 거래, 재고 정보를 조회해보세요.")

question = st.chat_input("질문을 입력하세요.")

if question:
    with st.chat_message("user"):
        st.write(question)

    with st.chat_message("assistant"):
        st.write("아직 모델 연결 전입니다!")