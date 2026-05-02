import streamlit as st
import random

# 멤버 데이터
nmixx_members = {
    "릴리": "메인보컬, 호주 출신, 시원한 고음과 독보적인 음색",
    "해원": "리더, 메인보컬, 밈 천재이자 예능감 넘치는 엔믹스의 기둥",
    "설윤": "비주얼 담당, 사슴상, 확신의 센터이자 뛰어난 보컬 실력",
    "배이": "개그 담당, 매력적인 중저음 보이스, 훤칠한 모델 포스",
    "지우": "메인래퍼, 귀여운 강아지상, 파워풀하고 유연한 춤선",
    "규진": "막내(메앙귀), 완벽한 올라운더, 무대 위 압도적인 퍼포먼스"
}

st.set_page_config(page_title="NMIXX 멤버 퀴즈", page_icon="🌟")
st.title("🌟 NMIXX 멤버 맞히기 게임")
st.write("힌트를 보고 멤버의 이름을 맞춰보세요!")

# 세션 상태 초기화 (문제 출제용)
if 'target' not in st.session_state:
    st.session_state.target = random.choice(list(nmixx_members.items()))
    st.session_state.score = 0

name, desc = st.session_state.target

st.info(f"**힌트:** {desc}")

# 사용자 입력
user_answer = st.text_input("정답 입력:", key="input_field")

if st.button("정답 확인!"):
    if user_answer.strip() == name:
        st.success(f"✅ 정답입니다! 역시 NSWER시군요!")
        st.balloons()
        if st.button("다음 문제 풀기"):
            st.session_state.target = random.choice(list(nmixx_members.items()))
            st.rerun()
    else:
        st.error(f"❌ 틀렸습니다! 다시 생각해보세요.")

st.sidebar.write(f"현재 퀴즈 진행 중!")
