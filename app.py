import streamlit as st
import random

# 팩트 체크된 고난도 30문제 (질문: q, 정답: a)
quiz_data = [
    {"q": "엔믹스의 데뷔일은 2022년 2월 몇 일일까요? (숫자만)", "a": "22"},
    {"q": "멤버 설윤이 연습생 시절 합격했던 '3대 기획사'는 SM, YG, 그리고 어디일까요?", "a": "JYP"},
    {"q": "엔믹스 멤버 중 유일하게 활동명을 사용하는 멤버는? (본명: 배진솔)", "a": "배이"},
    {"q": "곡 'DICE'에서 가사 중 주사위 번호를 언급하는 순서는 'One, Two, Three, Four, Five' 그리고 무엇일까요?", "a": "Six"},
    {"q": "해원이 리더로서 가진 고유 번호는 몇 번일까요? (숫자만)", "a": "22"},
    {"q": "엔믹스의 첫 번째 미니 앨범 이름은?", "a": "expergo"},
    {"q": "곡 'O.O'에서 가사 중 'Baile, Baile, Baile'의 뜻은 스페인어로 무엇일까요?", "a": "춤춰"},
    {"q": "멤버 지우의 혈액형은 무엇일까요? (대문자로)", "a": "AB"},
    {"q": "엔믹스 멤버 전원이 보컬, 댄스, 비주얼이 다 된다는 의미의 수식어는?", "a": "전원올라운더"},
    {"q": "곡 'DASH'가 수록된 미니 2집 앨범의 타이틀은?", "a": "Fe3O4: BREAK"},
    {"q": "멤버 릴리의 국적은 한국과 어디일까요?", "a": "호주"},
    {"q": "곡 'Young, Dumb, Stupid'에서 샘플링한 동요의 제목은?", "a": "박수 세 번"},
    {"q": "엔믹스 세계관에서 '지혜'를 상징하며 멤버들을 돕는 존재의 이름은?", "a": "픽스"},
    {"q": "멤버 규진이 무대에서 주로 맡고 있는 포지션 중 하나로, 팀의 막내를 뜻하는 별명은?", "a": "메앙귀"},
    {"q": "엔믹스의 공식 팬덤 NSWER의 로고 색상은?", "a": "검정색"},
    {"q": "곡 'Love Me Like This'의 후렴구에서 가장 많이 반복되는 단어는?", "a": "Love"},
    {"q": "멤버 해원의 고향은 어디일까요? (도시 이름)", "a": "인천"},
    {"q": "엔믹스 멤버 중 성이 '최'씨인 멤버는?", "a": "지우"},
    {"q": "곡 'Party O'Clock' 뮤직비디오의 배경이 되는 계절은?", "a": "여름"},
    {"q": "엔믹스 멤버 중 MBTI가 'ISFP'로 알려진 사슴상 멤버는?", "a": "설윤"},
    {"q": "데뷔곡 'O.O'의 장르를 지칭하는 엔믹스만의 고유 장르는?", "a": "믹스팝"},
    {"q": "곡 'DICE' 뮤직비디오에서 게임의 승자를 결정짓는 마지막 숫자는?", "a": "7"},
    {"q": "멤버 릴리가 출연했던 오디션 프로그램 이름은?", "a": "K팝스타4"},
    {"q": "엔믹스 공식 유튜브 채널의 구독자 애칭은?", "a": "엔써"},
    {"q": "멤버 배이가 대학교에서 전공하고 싶다고 언급했던 분야는?", "a": "연기"},
    {"q": "엔믹스의 소속 레이블은 JYP 내의 몇 본부일까요? (숫자만)", "a": "4"},
    {"q": "곡 'DASH' 뮤직비디오에서 멤버들이 벽을 부수고 나갈 때 사용한 도구는?", "a": "해머"},
    {"q": "엔믹스 멤버 중 가장 먼저 JYP에 입사한 멤버는?", "a": "릴리"},
    {"q": "엔믹스 멤버 6명의 국적 총 합은 (한국, 호주 포함) 몇 개국일까요? (숫자만)", "a": "2"},
    {"q": "엔믹스의 인사법에서 '둘, 셋' 다음에 외치는 문구는?", "a": "안녕하세요 엔믹스입니다"}
]

st.set_page_config(page_title="NMIXX FACT 30 퀴즈", page_icon="⭐")

# 세션 상태 초기화
if 'q_idx' not in st.session_state:
    random.shuffle(quiz_data)
    st.session_state.q_idx = 0
    st.session_state.score = 0
    st.session_state.input_key = 0

# 화면 구성
st.title("⭐ NMIXX 팩트 체크 30문 퀴즈")
st.write(f"현재 점수: **{st.session_state.score}** / 30")
st.progress((st.session_state.q_idx) / 30)

if st.session_state.q_idx < len(quiz_data):
    current_q = quiz_data[st.session_state.q_idx]
    
    st.info(f"**문제 {st.session_state.q_idx + 1}:** {current_q['q']}")
    
    # 폼을 사용하여 정답 제출 후 입력창 자동 초기화
    with st.form(key=f"quiz_form_{st.session_state.input_key}"):
        user_answer = st.text_input("정답을 입력하세요 (띄어쓰기 주의):", key="user_input").strip()
        submit = st.form_submit_button("정답 확인")
        
        if submit:
            # 정답 판정 (공백 제거 후 소문자 비교)
            if user_answer.replace(" ", "").lower() == current_q['a'].replace(" ", "").lower():
                st.success("🎉 정답입니다!")
                st.balloons() # 풍선 효과
                st.snow()     # 눈 내리는 효과 (시각적 풍성함 추가)
                st.session_state.score += 1
                st.session_state.q_idx += 1
                st.session_state.input_key += 1 # 입력창 초기화용 키 변경
                st.rerun()
            else:
                st.error("❌ 오답입니다. 다시 생각해보세요!")
else:
    st.balloons()
    st.snow()
    st.success("🎊 모든 문제를 완료했습니다! 당신은 진정한 NSWER!")
    st.header(f"최종 결과: {st.session_state.score}점 / 30점")
    if st.button("다시 도전하기"):
        st.session_state.q_idx = 0
        st.session_state.score = 0
        st.rerun()
