'''
두 정수를 입력받아 두 정수를 붙여서 쓴 값을 출력하는 프로그램을 
작성하세요 
예시로 
12 와 3을 입력받았다면 123 이 출력되어야 하고 
3 과 12 를 입력받았다면 312가 출력되어야 합니다 
'''
a = int(input("정수입력 >> "));
b = int(input("정수입력 >> "))
str_a = str(a);
str_b = str(b);
result = str_a + str_b;
print(result);