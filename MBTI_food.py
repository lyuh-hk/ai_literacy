import random

mbti_foods = {
    "ISTJ": ["로스팅 치킨", "스테이크", "감자튀김", "치킨 샐러드", "브리또"],
    "ISFJ": ["치킨 스프", "라자냐", "샌드위치", "프렌치 토스트", "토마토 수프"],
    "INFJ": ["채식 요리", "퀴노아 샐러드", "연어 스테이크", "흑임자 샐러드", "콰좡"],
    "INTJ": ["스시", "불고기", "피자", "샐러드 바", "삼겹살"],
    "ISTP": ["버거", "타코", "파스타", "피쉬 앤 칩스", "타코 샐러드"],
    "ISFP": ["피자", "망고 샐러드", "크로와상", "아보카도 토스트", "샌드위치"],
    "INFP": ["베이거릭 빵", "파스타", "피칸 파이", "허니버터 칩", "시리얼"],
    "INTP": ["카레", "피클", "마카로니 치즈", "스테이크", "브리또"],
    "ESTP": ["타코", "핫도그", "베이컨", "소세지", "치킨 낙지"],
    "ESFP": ["피자", "타코", "아이스크림", "버거", "프렌치 프라이"],
    "ENFP": ["팬케이크", "타코", "스무디", "케이크", "딸기 사과 샐러드"],
    "ENTP": ["피자", "타코", "버거", "파스타", "스테이크"],
    "ESTJ": ["스테이크", "햄버거", "마카로니 치즈", "비스킷 앤 그레이비", "포크"],
    "ESFJ": ["피자", "파스타", "감자튀김", "케이크", "바베큐 리브"],
    "ENFJ": ["샐러드", "스무디", "토스트", "파스타", "샌드위치"],
    "ENTJ": ["스테이크", "피자", "햄버거", "토스트", "크로와상"]
}

def re_food(mbti_type):

  if mbti_type in mbti_foods:
    m_list = mbti_foods[mbti_type]
    m_food = random.choice(m_list)
    return m_food
