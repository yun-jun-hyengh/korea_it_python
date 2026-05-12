'''
반복문
- for문과 while문이 있음
- 반복문이란 프로그램 내에서 똑같은 명령을 일정 횟수만큼 반복하여 수행하도록 제어하는 구문
프로그램이 처리하는 대부분의 코드는 반복적인 형태가 많으며 조건문과 더불어 가장 많이 사용되는 제어문 중 하나 
'''

# for문
# 예를 들어 Hello World!!~~ 를 10번을 출력을 해야 한다면??
for i in range(1, 11):
    print("Hello World!!~~", i, "번");

# 1 ~ 10까지 출력 
for i in range(1, 11, 1):
    print(i);

'''
파이썬의 for문 
- 타 언어와 다르게 range() 함수를 사용하여 루프를 돌린다 

참고!!
c, java 스타일
for(int i = 1; i <= 10; i++) {
    System.out.println(i);
}
'''