'''
문자열 my_str과 정수 k가 주어질 때 my_str을 k번 반복한 문자열을
출력하는 프로그램을 작성하세요 


실행결과)
문자열입력 >> string
정수입력 >> 3
출력결과 : stringstringstring

문자열입력 >> love
정수입력 >> 10
출력결과 : lovelovelovelovelovelovelovelovelovelove
'''
my_str = input("문자열 입력 >> ");
k = int(input("정수 입력 >> "));
result = my_str * k;
print(result);