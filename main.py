# from dotenv import load_dotenv
# load_dotenv()

from langchain_openai import ChatOpenAI
llm = ChatOpenAI()

import streamlit as st
st.title('인공지능 시인 :sunglasses:')
theme = st.text_input("시의 주제를 제시해주세요.")
st.write("시의 주제는", theme)

if theme != "" and st.button("시 짓기"):
    with st.spinner('시 작성중...'):
        result = llm.invoke(f"{theme}에 대한 시를 써줘").content
        st.write(result)
elif theme == "" and st.button("시 짓기"):
    st.warning('주제가 아직 입력되지 않았어요!', icon="⚠️")
