'''
문자열에 따라 다음과 같이 두 수의 크기를 비교하려 한다 
두 수가 n과 m이라면 
">","=" : n >= m
"<","=" : n <= m
">","!" : n > m
"<","!" : n < m
두 문자열 ineq와 eq가 주어진다. ineq는 "<"와 ">"중 하나이고 eq는 "="와"!"중 하나이다
그리고 두 정수 n과 m이 주어질 때 n과 m이 ineq와 eq의 조건에 맞으면 1을 아니면 0을 
return 하도록 solution 함수를 완성하시오 

입출력 예
ineq : <
eq : =
n : 20
m : 50
결과 : 1

ineq : >
eq : !
n : 41
m : 78
결과 : 0

20 <= 50은 참이기 때문에 1을 return합니다.  41 > 78은 거짓이기 때문에 0을 return합니다.
'''

def solution(ineq, eq, n, m):
    answer = 0;
    if ineq == ">" and eq == "=":
        if n >= m:
            answer = 1;
        else:
            answer = 0;
    elif ineq == "<" and eq == "=":
        if n <= m:
            answer = 1;
        else:
            answer = 0;
    elif ineq == ">" and eq == "!":
        if n > m:
            answer = 1
        else:
            answer = 0
    elif ineq == "<" and eq == "!":
        if n < m:
            answer = 1;
        else:
            answer = 0;
    return answer;

ineq = input("ineq : ")
eq = input("eq : ")
n = int(input("n : "))
m = int(input("m : "))
print(solution(ineq, eq, n, m));
