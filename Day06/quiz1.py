'''
숫자 하나를 입력받아 
입력받은 수의 절대값을 구하는 함수를 
만들어 주세요 

입력 >> -3
출력 : 3

입력 >> 3
출력 : 3
'''
def a(num):
    if num < 0:
        return -num
    else:
        return num;


num = int(input("숫자입력 >> "))
print(a(num));