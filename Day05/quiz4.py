'''
피보나치 수열
피보나치 수열의 핵심은 전전항과 전항을 더해서 다음항을 만든다 !!
1번째 항 : 1
2번째 항 : 1
3번째 항 : 2 (1 + 1)
4번째 항 : 3 (1 + 3)
5번째 항 : 5 (2 + 3)
6번째 항 : 8 (3 + 5)
이런식으로 구현이 된다 
여기서 문제가 있는데 이 수열의 항을 1번째 부터 차례대로 검사하면서 숫자에 3, 6, 9가 포함되어 있으면 
"짝"을 출력하고 그렇지 않으면 숫자 자체를 출력하는 프로그램을 작성하세요 
수열의 15번째 항까지 진행된다 
'''
num1 = 1;
num2 = 1;
print(num1, end = " ")  
print(num2, end = " ")  
for i in range(3, 16):
    next = num1 + num2;
    num_str = str(next);
    if '3' in num_str or '6' in num_str or '9' in num_str:
        print("짝", end=" ")
    else:
        print(next, end = " ");
    num1 = num2;
    num2 = next;