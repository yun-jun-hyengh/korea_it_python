'''
에러(Error)와 예외(Exception) 차이

에러(Error)
- 시스템이 종료되어야 할 수준의 상황과 같이 수습할 수 없는 심각한 문제를 의미

예외(Exception)
- 개발자가 구현한 로직에서 발생한 실수나 사용자의 영향에 의해 발생한다

형식)
try:
    코드
except 예외명:
    코드..

try 블럭안에 예외가 발생할 소지가 있는 코드를 명시하고
except 블럭안에 예외가 발생했을 시 처리할 코드를 명시한다
'''
try:
    num1 = int(input("숫자입력 >> "))
    num2 = int(input("숫자입력 >> "))
    result = num1 // num2;
    print("result : ", result);
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다");

