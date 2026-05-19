'''
while문
- 조건이 참인 동한 블록안에 있는 실행문을 실행

형식)
while 조건식:
    실행문 => 조건식이 참이면 실행되는 코드 
'''

i = 1; # 초기식
while i <= 10: # 조건식
    print(i);
    i = i + 1; # 증감식


print("==========");

j = 1;
while j <= 10:
    print("Hello World", j, "번");
    j = j + 1;