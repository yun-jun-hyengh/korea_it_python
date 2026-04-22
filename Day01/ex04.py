# 파이썬 자료형 종류
# - 숫자형, 문자열, 불리언, 컬렉션 자료형으로 나뉜다 


'''
숫자형
- 숫자를 표시하는 자료형으로 파이썬은 정수, 실수, 복소수 등 다양한 숫자 자료형을 지원함
'''

# 정수형
num1 = 10; print(num1);
num2 = 20; print(num2);

num3 = -10; print(num3);
num4 = -20; print(num4);
num5 = 0; print(num5);
num5 = 100; # 16번째 줄에서 0으로 초기화 했지만 17번째 줄에서 100으로 다시 num5 변수값을 변경하였음 
print(num5);

# 변수를 이용해서 다른 변수에 복사 
# 변수에 직접 값을 대입할 수도 있지만 이미 존재하는 변수의 데이터를 사용하여 다른 변수에 값을 대입할 수 있다
myAge = 20; # myAge 변수에 20을 대입 
yourAge = myAge; # yourAge 변수에 myAge 변수에 저장된 값을 넣음 
print("yourAge : ", yourAge);

# 두 변수값 바꾸기
x = 10;
y = 20;
print("x : ", x); print("y : ", y);

temp = 0; # x의 값을 임시 저장할 변수 선언
temp = x; # x의 값을 temp 변수에 저장
x = y; # y의 값을 x에 대입
y = temp; # temp가 들고 있던 값을 y에 대입 
print("x : ", x); print("y : ", y);

var1 = 100;
var2 = 200;
result = var1 + var2; # var1 변수값과 var2의 변수값을 더한 결과를 result 변수에 대입
print(result); 

'''
실수형(float)
- 소수와 지수로 구성된 수를 나타내는 자료형 
'''
width = 30.5 # 가로 
height = 25.3 # 세로
print("가로 : ", width);
print("세로 : ", height);
print("넓이 : ", width * height);

fx = 1.7;
fy = 2.3;
print(fx + fy);


'''
복소수형(complex)
- 실수와 달리 복소수형은 실수와 허수(j)를 포함하는 숫자를 나타내는 자료형이다. 
실수와 허수는 각각 실수부와 허수부로 구성된다. 
- 복소수형은 파이썬이 제공하는 특별한 자료형이다. 다른 프로그래밍 언어에는 존재하지 않음
공학 물리학 분야에서 사용함 
'''
z = 3 + 4j;
print("z : ", z);