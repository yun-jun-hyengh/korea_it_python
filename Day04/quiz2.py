'''
태어난 해, 월, 일을 입력받아 사주팔자를 보는 프로그램을 작성하세요 
사주보는방법)
세 수(년,월,일)가 주어지면, (년 - 월 + 일)에 마지막 숫자가 0이면 대박을 출력
그렇지 않으면 그럭저럭을 출력하세요 
'''

year = int(input("년도입력 >> "));
month = int(input("월 입력 >> "));
day = int(input("일 입력 >> "));

result = year - month + day
str1 = str(result);
if str1[-1] == '0':
    print("대박");
else:
    print("그럭저럭");