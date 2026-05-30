'''
인터넷 서비스들은 대부분 아이디와 패스워드를 이용한다 
이때 사용되는 패스워드는 여러 가지 방법으로 암호화되어 저장된다 

* 어떤 인터넷 서비스의 2가지 암호화 방법 
- 입력받은 문자의 ASCII 코드값 + 2
사용자의 패스워드를 2가지 방법으로 암호화한 결과를 출력하는 프로그램을 작성하세요 

입력
첫번째 줄에는 20자 이내로 구성된 암호를 입력한다.(단, 입력되는 암호에 공백은 포함되지 않는다)

입출력 예시)
입력 >> TEST
출력 : VGUV

입력 >> sedfjwhsiufdhsdiuhfiurhgufhgiudhgiehgiuerhgkjfdhgiuserhfsdhfsdfh
출력 : 문자열 범위 초과하였거나 공백이 포함되어 있습니다 

입력 >> erd dfsf
출력 >> 문자열 범위 초과하였거나 공백이 포함되어 있습니다 
'''
def solution(string):
    new_string = ""
    if len(string) > 20 or ' ' in string:
        new_string = "문자열 범위 초과하였거나 공백이 포함되어 있습니다.";
    else:
        for i in string:
            code = ord(i);
            new_string = new_string + chr(code + 2);
    return new_string;

string = input("입력 >> ");
print(solution(string))

