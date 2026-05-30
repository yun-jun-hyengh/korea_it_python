'''
파이썬 함수 선언 방법

def
- 파이썬은 함수를 선언할 때 def라는 키워드를 사용한다 
- c, java와 달리 동적타이핑 언어이므로 인터프리터가 알아서 타입을 
판단하므로 함수선언시 반환 타입을 지정해 줄 필요가 없음 

형식)
def 함수이름(매개변수):
    실행문..

매개변수란?
- 외부에서 전달받은 값을 함수 내부로 전달하기 위해 사용하는 변수 

return 이란?
- 함수 내부에서 작업한 결과를 함수를 호출한 곳으로 돌려준다
'''
def a(a, b):
    return a + b;

def b(a, b):
    return a - b;

def c(a, b):
    return a * b;

def d(a, b):
    return a // b;

num1 = int(input("숫자입력 >> "))
num2 = int(input("숫자입력 >> "))
print(a(num1, num2))
print(b(num1, num2));
print(c(num1, num2))
print(d(num1, num2))



