'''
문자열 my_string과 정수 s, e가 매개변수로 주어질 때 my_string에서 인덱스 s부터 
인덱스 e까지를 뒤집은 문자열을 return 하는 solution 함수를 작성해 주세요 

입력 >> Progra21Sremm3
입력 >> 6
입력 >> 12
결과 : ProgrammerS123

입력 >> Stanley1yelnatS
입력 >> 4
입력 >> 10
결과 : Stanley1yelnatS
'''

def solution(my_string, s, e):
    answer = "";
    prefix = my_string[0: s];
    target = my_string[s: e + 1]
    suffix = my_string[e + 1 : ]
    reversed_string = target[::-1];
    print("prefix : ", prefix);
    print("target : ", target);
    print("suffix : ", suffix);
    answer = prefix + reversed_string + suffix
    return answer;

my_string = input("입력 >> ")
s = int(input("입력 >> "))
e = int(input("입력 >> "))
print(solution(my_string, s, e))