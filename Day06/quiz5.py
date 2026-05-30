'''
영어 알파벳으로 이뤄진 문자열이 주어진다 각 알파벳을 대문자는 소문자로 
소문자는 대문자로 변환해서 출력하는 함수를 작성하시오 

입력 >> aBcDeFg
출력 : AbCdEfG
'''
def solution(string):
    new_string = ""
    for i in string:
        code = ord(i); # 문자를 숫자로 변환
        if 65 <= code and code <= 90:
            new_string = new_string + chr(code + 32);
        elif 97 <= code and code <= 122:
            new_string = new_string + chr(code - 32);
    return new_string;

string = input("입력 >> ");
print(solution(string))