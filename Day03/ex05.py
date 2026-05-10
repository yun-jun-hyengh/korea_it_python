'''
비교 연산자
- 두 개의 값을 비교하여 그 결과가 참(True) 인지 거짓(False)인지 판별하는 연산자임 

> : 왼쪽 값이 오른쪽 값보다 크다 
< : 왼쪽 값이 오른쪽 값보다 작다 
>= : 왼쪽 값이 오른쪽 값보다 크거나 같다 
<= : 왼쪽 값이 오른쪽 값보다 작거나 같다
== : 왼쪽 값과 오른쪽 값이 같다
!= : 왼쪽 값과 오른쪽 값이 같지 않다
'''

a = 20; b = 10;

print("a > b : ", a > b);
print("a < b : ", a < b);
print("a >= b : ", a >= b);
print("a <= b : ", a <= b);
print("a == b : ", a == b);
print("a != b : ", a != b);

str1 = "abc"; str2 = "a" + "b" + "c";
equals = str1 == str2;
print(equals);
str_one = "1";
num_one = 1;
print(str_one == num_one);