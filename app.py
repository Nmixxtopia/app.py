import streamlit as st
import random
from streamlit_confetti import confetti  # 폭죽 라이브러리 추가

# 고난도 30문제 데이터
quiz_data = [
    {"q": "엔믹스 세계관에서 가고자 하는 유토피아의 이름은?", "a": "믹스토피아"},
    {"q": "데뷔곡 'O.O' 뮤직비디오에서 멤버들이 처음으로 눈을 뜨는 장소의 배경은?", "a": "도넛가게"},
    {"q": "엔믹스의 슬로건은 'Nice to ______ you'입니다. 빈칸은?", "a": "MIXX"},
    {"q": "곡 'DICE'에서 가사 중 '머리 위로 굴려' 다음에 나오는 영어 구절은?", "a": "Big wave"},
    {"q": "세계관 속에서 멤버들을 방해하는 적대적인 존재를 상징하는 동물은?", "a": "고양이"},
    {"q": "멤버 설윤이 'DICE' 활동 당시 입었던 의상 중 화제가 된 카드 문양은?", "a": "하트"},
    {"q": "곡 'Love Me Like This'에서 반복되는 가사 '철장 없는 000'은?", "a": "나비장"},
    {"q": "해원의 별명 중 '차린건 쥐뿔도 없지만'에서 유래된 광기 어린 별명은?", "a": "외모는 강아지 성격은 광기"},
    {"q": "엔믹스 멤버 중 '가장 연습생 기간이 긴' 멤버는?", "a": "릴리"},
    {"q": "곡 'O.O' 가사 중 'Check out, popcorn, Rock n Roll' 뒤에 나오는 가사는?", "a": "Come and get it"},
    {"q": "세계관 내에서 적대 세력을 부르는 이름은?", "a": "모노폴"},
    {"q": "곡 'Soñar (Breaker)'에서 'Soñar'의 스페인어 뜻은?", "a": "꿈을 꾸다"},
    {"q": "엔믹스 공식 응원봉의 이름은 무엇인가요?", "a": "믹스틱"},
    {"q": "데뷔 앨범의 타이틀 명칭은?", "a": "AD MARE"},
    {"q": "멤버 배이의 본명은?", "a": "배진솔"},
    {"q": "멤버 지우의 생일은 몇 월인가요? (숫자만)", "a": "4"},
    {"q": "곡 'Young, Dumb, Stupid'에서 샘플링한 동요의 제목은?", "a": "Frere Jacques"},
    {"q": "엔믹스의 자체 콘텐츠 'MIXXTAPE'에서 해원과 배이의 조합을 부르는 말은?", "a": "차개조"},
    {"q": "릴리가 K팝 스타 시즌 4에서 최종 몇 위를 했나요? (숫자만)", "a": "4"},
    {"q": "곡 'Party O'Clock'의 작사, 작곡에 참여한 JYP 수장은?", "a": "박진영"},
    {"q": "규진의 별명 중 '메인 앙큼 귀요미'의 줄임말은?", "a": "메앙귀"},
    {"q": "곡 'DASH' 뮤직비디오에서 멤버들이 갇혀 있다가 탈출하는 장소는?", "a": "감옥"},
    {"q": "세계관에서 '꿈'과 '현실'을 연결하는 매개체로 자주 등장하는 사탕의 종류는?", "a": "젤리"},
    {"q": "엔믹스 멤버 중 가장 키가 큰 멤버는?", "a": "배이"},
    {"q": "곡 'Roller Coaster' 가사 중 '심장은 0000000000' 빈칸은? (8글자)", "a": "Bumpy bumpy round and round"},
    {"q": "엔믹스 멤버들의 고유 숫자가 있습니다. 릴리의 숫자는? (숫자만)", "a": "7"},
    {"q": "팬덤 NSWER의 뜻은 'North South West East ______'의 약자입니다.", "a": "Route"},
    {"q": "엔믹스의 장르를 일컫는 말로, 두 가지 이상의 장르를 섞은 것은?", "a": "믹스팝"},
    {"q": "곡 'O.O' 가사 중 '어때? 00 00 00' 빈칸에 들어갈 말은?", "a": "질러 질러 질러"},
    {"q": "엔믹스의 인사법 '둘 셋! 안녕하세요 0000입니다!' 빈칸은?", "a": "엔믹스"}
]

st.set_page_config(page_title="NMIXX 고난도 30문 퀴즈", page_icon="🎤")

# 세션 상태 초기화
if 'q_idx' not in st.session_state:
    random.shuffle(quiz_data)
    st.session_state.q_idx = 0
    st.session_state.score = 0
    st.session_state.input_key = 0
    st.session_state.correct_anim = False # 정답 애니메이션 상태

# 현재 문제 가져오기
if st.session_state.q_idx < len(quiz_data):
    current_q = quiz_data[st.session_state.q_idx]

    st.title("🎤 NMIXX 마스터 챌린지 (30문)")
    st.write(f"**진행 상황:** {st.session_state.q_idx + 1} / 30 | **현재 점수:** {st.session_state.score}")
    st.progress((st.session_state.q_idx + 1) / 30)

    st.subheader(f"Q. {current_q['q']}")
    
    # 정답 맞췄을 때 폭죽 팡팡!
    if st.session_state.correct_anim:
        confetti(content_count=200, explosion_speed=2) # 폭죽 효과!
        st.success(f"🎉 정답입니다! : {current_q['a']}")
        st.session_state.correct_anim = False # 상태 초기화

    # 폼을 사용하여 정답 제출 후 입력창 자동 초기화
    with st.form(key=f"quiz_form_{st.session_state.input_key}"):
        user_answer = st.text_input("정답을 입력하세요:", key="user_input").strip()
        submit_button = st.form_submit_button(label="제출하기")

        if submit_button:
            # 띄어쓰기/대소문자 무시 체크
            if user_answer.replace(" ", "").lower() == current_q['a'].replace(" ", "").lower():
                st.session_state.score += 1
                st.session_state.q_idx += 1
                st.session_state.input_key += 1
                st.session_state.correct_anim = True # 폭죽 애니메이션 켜기
                st.rerun()
            else:
                st.error("❌ 틀렸습니다! 다시 한 번 생각해보세요.")
else:
    confetti(content_count=500, explosion_speed=1) # 최종 클리어 폭죽!
    st.title("🏆 축하합니다! 모든 문제를 풀었습니다!")
    st.header(f"최종 점수: {st.session_state.score} / 30")
    if st.button("다시 시작하기"):
        st.session_state.q_idx = 0
        st.session_state.score = 0
        st.rerun()
