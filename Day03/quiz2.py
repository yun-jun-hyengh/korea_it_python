'''
두 수를 입력받아 두 수를 비교하여 큰수를 출력하세요 
조건) 삼항연산자로 구현할 것 

실행결과)
숫자입력 >> 20
숫자입력 >> 10
결과 : 20
'''
num1 = int(input("숫자입력 >> "));
num2 = int(input("숫자입력 >> "));

result = num2 if num1 < num2 else num1;
print(result); 