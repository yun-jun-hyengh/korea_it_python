'''
사용자로부터 다음과 같은 숫자를 입력받아 입력받은 숫자의 
총 합을 구하는 프로그램을 함수버전으로 작성하세요 

입력 >> 65 45 2 3 45 8

'''

def ads(*args):
    sum_val = 0
    for i in args:
        sum_val = sum_val + i
    return sum_val


data = list(map(int, input().split(',')))
print(ads(*data))