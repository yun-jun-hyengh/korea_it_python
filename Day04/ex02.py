'''
변수를 사용하여 조건식 만들기
'''
age = 20;
if age >= 20:
    print("20세 이상입니다.");

# 짝수인지 홀수인지 판별하기
number = 10;
if number % 2 == 0:
    print("짝수");
else:
    print("홀수");

# 논리 연산자와 함께 제어문 구현
# 국영수 점수가 모두 60점 이상이면 합격
kor = 100;
eng = 85;
math = 95;

if kor >= 60 and eng >= 60 and math >= 60:
    print("합격입니다.");
else:
    print("불합격입니다.");

# 국영수 점수 중 하나라도 60점 미만이면 불합격 
if kor < 60 or eng < 60 or math < 60:
    print("불합격입니다.");
else:
    print("합격입니다.");