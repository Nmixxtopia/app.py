import streamlit as st
import random

# 더 어려워진 퀴즈 데이터 (질문: 정답)
quiz_data = [
    {"question": "엔믹스의 데뷔곡 'O.O'에서 가사에 등장하는 '어떤 음료'는 무엇일까요?", "answer": "코카콜라"},
    {"question": "멤버 해원의 별명 중 하나로, 예능감이 뛰어나 붙여진 이 별명은? (힌트: 외모는 00, 성격은...)", "answer": "광기"},
    {"question": "엔믹스 멤버 중 '차세대 보컬 퀸'으로 불리며 호주 출신인 멤버의 본명은?", "answer": "릴리"},
    {"question": "노래 'DICE'에서 가사 중 '머리 위로 굴려 000000'에 들어갈 말은?", "answer": "Big wave"},
    {"question": "엔믹스 내에서 '차세대 센터'이자 사슴상으로 유명한 멤버는?", "answer": "설윤"},
    {"question": "막내 규진의 별명으로, 귀엽지만 무대 위에서 압도적이라 붙여진 이름은?", "answer": "메앙귀"},
    {"question": "엔믹스의 공식 팬덤 명칭은 무엇인가요?", "answer": "NSWER"},
    {"question": "멤버 배이(BAE)가 연습생 시절 '가장 늦게 합류'한 것으로 알려진 이 멤버의 본명은?", "answer": "배진솔"}
]

st.set_page_config(page_title="엔써 전용 고난도 퀴즈", page_icon="🎤")

# 세션 상태(상태 유지) 설정
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'current_quiz' not in st.session_state:
    st.session_state.current_quiz = random.choice(quiz_data)
if 'answered' not in st.session_state:
    st.session_state.answered = False

st.title("🎤 NMIXX 고난도 퀴즈 챌린지")
st.write(f"현재 점수: **{st.session_state.score}** 점")
st.divider()

# 현재 문제 표시
quiz = st.session_state.current_quiz
st.subheader(f"Q. {quiz['question']}")

# 사용자 입력
user_input = st.text_input("정답을 입력하세요 (띄어쓰기 주의):", key="input").strip()

if st.button("제출하기"):
    if user_input.lower() == quiz['answer'].lower():
        st.success("🎉 정답입니다! 다음 문제로 넘어갑니다.")
        st.session_state.score += 10
        # 새로운 문제 선택
        st.session_state.current_quiz = random.choice(quiz_data)
        st.balloons()
        # 페이지 리프레시 (입력창 비우기 위해)
        st.rerun()
    else:
        st.error("❌ 틀렸습니다! 다시 한번 생각해보세요.")

if st.button("다른 문제로 넘기기"):
    st.session_state.current_quiz = random.choice(quiz_data)
    st.rerun()

st.sidebar.info("정답이 생각나지 않으면 힌트를 검색해보세요! 🔍")
