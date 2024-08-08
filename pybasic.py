#구구단 만들기
import streamlit as st
import random

def gugudan():
    dan = st.number_input("단입력 >> ",value=1)
    # dan = int(dan)

    if dan > 1:
        for i in range(1,10):
            r= dan*i
            st.write(f"{dan} x {i} = {r}")




def recommand_food():
    # 음식추천프로그램
    c_food=['자장면','짬뽕','탕수육','팔보채','유산슬']
    k_food=['비빔밥','갈비탕','육개장','된장찌개','김치찌개']

    # 1번 입력하면 --> 중식 추천
    # 2번 입력하면 --> 한식 추천
    st.subheader("음식추천")
    menu = st.radio("",["중식","한식"],index=None)
    if menu == '중식':
        st.write(f"오늘의 중식 추천메뉴: {random.choice(c_food)}")
    elif menu == '한식':
        st.write(f"오늘의 한식 추천메뉴: {random.choice(k_food)}")
    else:
        st.write("음식종류를 선택하세요!!")


# gugudan()
# recommand_food()      


def basic():
    tab1, tab2 = st.tabs(["구구단", "음식추천"])

    with tab1:
        gugudan()
    with tab2:
        recommand_food()   
