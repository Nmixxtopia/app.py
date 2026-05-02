import streamlit as st
import random
import time

# 팩트 기반 30문제 데이터 (규진 문제 수정 완료)
quiz_data = [
    {"q": "엔믹스의 데뷔일은 2022년 2월 몇 일일까요? (숫자만)", "a": "22"},
    {"q": "멤버 설윤이 연습생 시절 합격했던 '3대 기획사'는 SM, YG, 그리고 어디일까요?", "a": "JYP"},
    {"q": "엔믹스 멤버 중 유일하게 활동명을 사용하는 멤버는? (본명: 배진솔)", "a": "배이"},
    {"q": "곡 'DICE'에서 가사 중 주사위 번호를 언급하는 순서는 'One, Two, Three, Four, Five' 그리고 무엇일까요?", "a": "Six"},
    {"q": "해원이 리더로서 가진 고유 번호는 몇 번일까요? (숫자만)", "a": "22"},
    {"q": "엔믹스의 첫 번째 미니 앨범 이름은?", "a": "expergo"},
    {"q": "곡 'O.O'에서 가사 중 'Baile, Baile, Baile'의 뜻은 스페인어로 무엇일까요?", "a": "춤춰"},
    {"q": "멤버 지우의 혈액형은 무엇일까요? (대문자로)", "a": "AB"},
    {"q": "엔믹스 멤버 전원이 보컬, 댄스, 비주얼이 다 된다는 의미의 수식어는?", "a": "올라운더"},
    {"q": "곡 'DASH'가 수록된 미니 2집 앨범의 타이틀은?", "a": "Fe3O4: BREAK"},
    {"q": "멤버 릴리의 국적은 한국과 어디일까요?", "a": "호주"},
    {"q": "곡 'Young, Dumb, Stupid'에 샘플링된 프랑스 유명 동요의 제목은?", "a": "Frere Jacques"},
    {"q": "세계관 내에서 적대 세력을 부르는 이름은?", "a": "모노폴"},
    {"q": "막내 규진은 무대 위 눈빛과 비주얼 때문에 '앙큼 000'라고 불립니다. 이 동물은?", "a": "고양이"},
    {"q": "엔믹스 공식 응원봉의 이름은 무엇인가요?", "a": "믹스틱"},
    {"q": "곡 'Love Me Like This'의 후렴구에서 가장 많이 반복되는 단어는?", "a": "Love"},
    {"q": "멤버 해원의 고향은 어디일까요? (도시 이름)", "a": "인천"},
    {"q": "엔믹스 멤버 중 성이 '최'씨인 멤버는?", "a": "지우"},
    {"q": "곡 'Party O'Clock' 뮤직비디오의 배경이 되는 계절은?", "a": "여름"},
    {"q": "엔믹스 멤버 중 사슴상으로 유명하며 센터 비주얼인 멤버는?", "a": "설윤"},
    {"q": "데뷔곡 'O.O'의 장르를 지칭하는 엔믹스만의 고유 장르는?", "a": "믹스팝"},
    {"q": "곡 'DICE' 뮤직비디오에서 게임의 승자를 결정짓는 마지막 숫자는?", "a": "7"},
    {"q": "멤버 릴리가 출연했던 오디션 프로그램 이름은?", "a": "K팝스타4"},
    {"q": "엔믹스 공식 팬덤 명칭은?", "a": "NSWER"},
    {"q": "멤버 배이의 본명은?", "a": "배진솔"},
    {"q": "엔믹스의 소속 레이블은 JYP 내의 몇 본부일까요? (숫자만)", "a": "4"},
    {"q": "곡 'DASH' 뮤직비디오에서 멤버들이 탈출하는 장소는?", "a": "감옥"},
    {"q": "엔믹스 멤버 중 가장 먼저 JYP에 입사한 멤버는?", "a": "릴리"},
    {"q": "엔믹스 멤버 6명의 국적 종류는 총 몇 개인가요? (숫자만)", "a": "2"},
    {"q": "엔믹스의 인사법에서 '둘, 셋' 다음에 외치는 문구는?", "a": "안녕하세요 엔믹스입니다"}
]

st.set_page_config(page_title="NMIXX FACT 30 퀴즈", page_icon="⭐")

# 세션 상태 초기화
if 'shuffled_quiz' not in st.session_state:
    temp_list = quiz_data.copy()
    random.shuffle(temp_list)
    st.session_state.shuffled_quiz = temp_list
    st.session_state.q_idx = 0
    st.session_state.score = 0
    st.session_state.input_key = 0

st.title("⭐ NMIXX 팩트 체크 30문 퀴즈")
st.write(f"현재 점수: **{st.session_state.score}** / 30")

if st.session_state.q_idx < len(st.session_state.shuffled_quiz):
    current_q = st.session_state.shuffled_quiz[st.session_state.q_idx]
    
    st.progress((st.session_state.q_idx + 1) / 30)
    st.info(f"**문제 {st.session_state.q_idx + 1}:** {current_q['q']}")
    
    with st.form(key=f"quiz_form_{st.session_state.input_key}"):
        user_answer = st.text_input("정답을 입력하세요:", key=f"input_{st.session_state.input_key}").strip()
        submit = st.form_submit_button("정답 확인")
        
        if submit:
            clean_user = user_answer.replace(" ", "").lower()
            clean_correct = current_q['a'].replace(" ", "").lower()
            
            if clean_user == clean_correct:
                msg_placeholder = st.empty()
                msg_placeholder.success(f"🎉 정답입니다! 정답은 '{current_q['a']}'였습니다!")
                st.balloons()
                st.snow()
                
                time.sleep(2)
                
                st.session_state.score += 1
                st.session_state.q_idx += 1
                st.session_state.input_key += 1
                st.rerun()
            else:
                st.error("❌ 틀렸습니다! 다시 한 번 생각해보세요.")
else:
    st.balloons()
    st.success("🎊 모든 문제를 완료했습니다! 당신은 진정한 마스터 NSWER!")
    st.header(f"최종 결과: {st.session_state.score}점 / 30점")
    if st.button("다시 도전하기"):
        del st.session_state.shuffled_quiz
        st.rerun()
