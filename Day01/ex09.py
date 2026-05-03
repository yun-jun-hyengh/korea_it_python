'''
문자열 슬라이싱
- 문자열 인덱스를 이용하여 특정 문자를 추출할 수 있을 뿐 아니라 문자열의 일부(단어)를 
원하는 만큼 추출해 낼 수 있다. 이를 슬라이싱 이라고 함 

변수명[start:stop:step]

start(시작 인덱스) : 슬라이싱을 시작할 위치를 지정한다. 이 값은 생략이 가능하며 기본값은 0이다 
stop(종료 인덱스) : 끝 인덱스를 지정한다 이 값 또한 생략이 가능하며 끝인덱스 -1 이다 
step(증감폭) : 인덱스의 증가 또는 감소 값을 지정한다 
'''

str1 = "Hello";
print(str1[0:3]);

text = "I Love Python";

substring_1 = text[2:6]; # 시작인덱스 2  끝인덱스 6으로 지정
print('substring_1 : ', substring_1);

substring_2 = text[7:13];
print('substring_2', substring_2);

substring_3 = text[7:13:2];
print('substring_3', substring_3);

# 시작인덱스 또는 종료인덱스를 생략하여 슬라이싱 하기 
a = "Life is too short";
# 시작인덱스 생략
print(a[:4]); print(a[:7]);
# 종료 인덱스 생략 
print(a[12:]); # 시작인덱스 부터 문자열 끝까지 출력됨 
# 시작인덱스와 종료인덱스 둘다 생략
print(a[:]); # 문자열 전체가 출력됨 ! 