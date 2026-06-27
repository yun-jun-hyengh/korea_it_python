'''
내장모듈
- 파이썬을 설치할 때 기본적으로 제공되는 모듈 별도의 설치 없이
바로 import 하여 사용할 수 있다
- math(수학연산), random(난수), datetime(날짜), json(JSON 파싱 및 생성)
'''

import math
import random
print(math.pi); # 원주율 출력

# 소수점 올림과 내림
print(math.ceil(4.2)); # 올림
print(math.floor(4.8)); # 내림

# 리스트에서 무작위로 하나 고르기
food = ["짜장면", "짬뽕", "치킨", "피자", "두쫀쿠", "고구마케이크", "삼겹살"]
print("오늘 먹을 음식은:", random.choice(food))

# 리스트 순서 무작위로 섞기
cards = ['A','B','C','W','E','R','Q'];
random.shuffle(cards);
print("결과 : ", cards);

import datetime
now = datetime.datetime.now();
print(now);
# 년도 월 일 형식으로 출력 2026-06-21
result = now.strftime("%Y-%m-%d");
print("현재 날짜 : ", result)