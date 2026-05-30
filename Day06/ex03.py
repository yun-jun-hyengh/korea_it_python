'''
다양한 함수 형태
'''

# 일반적인 형태의 함수 : 매개변수가 있고 return이 있는 함수 
def add(a, b):
    result = a + b;
    return result;

# 매개변수가 없는 함수 
def say():
    return "Hi"

# return이 없는 함수 
def mul(a, b):
    print(a * b);

# 매개변수가 없고 return 이 없는 함수 
def hello():
    print("Hello World");



num1 = int(input("숫자입력 >> "))
num2 = int(input("숫자입력 >> "))
print(add(num1, num2))
print(say());
mul(num1, num2)
hello();
