
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st


plt.rc('font',family = 'malgun gothic')

def basic():
#파일 불러오기
    df = pd.read_csv('한국전력공사_지역별 전기차 현황정보_20230331.csv',encoding='EUC-KR')


    #피벗 해제(열의 데이터로 변환)
    df_melt = pd.melt(df,id_vars='기준일',value_vars=['서울', '인천', '경기', '강원', '충북', '충남', '대전', '세종', '경북', '대구', '전북',
        '전남', '광주', '경남', '부산', '울산', '제주', '합계'],var_name='지역',value_name='자동차수')

    df_melt['년'] = df_melt['기준일'].str[:4]
    df_melt['월']  = df_melt['기준일'].str[5:7]

    return df_melt


def region_mean(df_melt):
#지역별, 년도별 자동차수 평균계산
    year_region_da = round(pd.pivot_table(df_melt,index='년',columns='지역',values='자동차수',aggfunc='mean'))
    st.dataframe(year_region_da)

# 행,렬 전환
    year_region_da = year_region_da.T

    region_query = year_region_da[year_region_da.index != "합계"]

#데이터 프레임 이용한 차트
    # region_query.plot(kind='bar',rot=0) 
    ax = region_query.plot(kind='bar',rot =0)
    fig = ax.get_figure()
    st.pyplot(fig)

    # plt.show()

def mean_2023(df_melt):
    df_melt_2023 = df_melt[df_melt['년'] == '2023']
    df_melt_2023 = df_melt_2023[df_melt_2023['지역'] != "합계"]
    df_2023 = round(pd.pivot_table(df_melt_2023,index='년',columns='지역',values='자동차수',aggfunc='mean'))
    st.dataframe(df_2023)

    ax = df_2023.plot(kind='bar',rot =0)
    fig = ax.get_figure()
    st.pyplot(fig)


    #조건 비교 함수
    df_2023['분기'] = np.where((df_2023['월'] >= 1) & (df_2023['월'] <= 3),'1분기' , 
                                np.where((df_2023['월'] >= 4) & (df_2023['월'] <= 6), '2분기',
                                np.where((df_2023['월'] >= 7) & (df_2023['월'] <= 9), '3분기', 
                                '4분기')))


    # return df_melt



def q_mean(df_melt):
    df_2022 = df_melt[df_melt['년'] == '2022']
    df_2022['월'] = df_2022['월'].astype(int)

    import numpy as np

    #조건 비교 함수
    df_2022['분기'] = np.where((df_2022['월'] >= 1) & (df_2022['월'] <= 3),'1분기' , 
                            np.where((df_2022['월'] >= 4) & (df_2022['월'] <= 6), '2분기',
                            np.where((df_2022['월'] >= 7) & (df_2022['월'] <= 9), '3분기', 
                            '4분기')))

    df_2022_d = round(pd.pivot_table(df_2022,index='지역',columns='분기',values='자동차수',aggfunc='mean'),0)

    df_2022_d = df_2022_d[df_2022_d.index != "합계"]
    st.dataframe(df_2022_d.T)

    # df_2022_d2 = df_2022.groupby(['지역','분기'])[['자동차수']].mean().reset_index()
    # st.dataframe(df_2022_d2)


    # df_2022_d.plot(kind='bar',rot=0)
    # plt.show()
    ax = df_2022_d.plot(kind='bar',rot =0)
    fig = ax.get_figure()
    st.pyplot(fig)






#main 실행   
def elec_exe():
    menu = st.selectbox('분석내용',['선택','지역별/연도별 분석','2023년 지역별 분석','2022년 분기별 분석'])
    # st.header('탐색적 분석 : 전기자동차분석')
    df_melt = basic()

    if menu == "지역별/연도별 분석":
        region_mean(df_melt)
    elif menu == "2023년 지역별 분석":     
        mean_2023(df_melt)
    elif menu == "2022년 분기별 분석" :  
        q_mean(df_melt)
    else:
        st.image('고래.png',width=500)
# while True:
    
#     menu = int(input("메뉴 입력(1:지역별/년도별 분석, 2: 2023분석, 3:2022년 분기별 분석, 0:종료)"))

#     if menu == 1:
#         region_mean(df_melt)
    
#     elif menu == 2:    
#         q_mean(df_melt)
    
#     elif menu == 0:    
#         break
    
#     else :
#         print('입력오류')

if __name__=='__main__':    
    elec_exe()  
