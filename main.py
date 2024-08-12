import streamlit as st
import electric_car as ec
import pybasic as pb
import project as p7

#로그인화면
st.sidebar.title("＆＆＆로그인＆＆＆")
user_id = st.sidebar.text_input("아이디(ID) 입력",value='',max_chars=10)
user_pw = st.sidebar.text_input("패스워드 입력",value='',type='password')


# st.write(user_id)
# st.write(user_pw)


if user_pw =='1234' and user_id == 'jiknyuh':
    # st.title("안녕하세요~~ 반가워요~")
    st.sidebar.title(">>혜경의 첫 포트폴리오<<")
    # st.image('DATA\고래.png')

    menu = st.sidebar.radio('메뉴선택',['나는 누구일까요?','파이썬기초','탐색적 분석 : 전기자동차분석','머신러닝',"파이썬기초:project"],index=None)
    st.sidebar.write(menu)
    
    if menu == '나는 누구일까요':
        st.header('공부할께 너무너무 많아 슬픈 아줌마입니다 ㅠㅠ') 
    elif menu == '탐색적 분석 : 전기자동차분석':
        ec.elec_exe()
    elif menu == '파이썬기초':
        pb.basic()
    elif menu == '머신러닝':
        st.header('공사중') 
    elif menu == '파이썬기초:project':
        p7.mbti_main()  

        


