'''
사용자로부터 하나의 양의정수를 입력받는다 
이 숫자의 각 자릿수 중에서 짝수의 개수와 홀수의 개수를 
각각 구하고 입력받은 숫자를 거꾸로 뒤집은 숫자를 출력하세요 
단) 문자열뒤집기 [::-1] 혹은 리스트를 사용하지 마시오 

뒤집은 숫자 : 54021
짝수의 개수 : 3개 ( 2,0,4 )
홀수의 개수 : 2개 ( 1,5 )
'''
num = int(input("숫자입력 >> "));
str_num = str(num);
count_1 = 0;
count_2 = 0;
str1 = '';
str2 = '';
index = len(str_num) - 1;  # 맨 마지막 글자의 인덱스 구하기 
for i in str_num:
    a = int(i);
    if a % 2 == 0:
        count_1 = count_1 + 1;
        if count_1 == 1:
            str1 = str1 + i;
        else:
            str1 = str1 + "," + i;
    else:
        count_2 = count_2 + 1;
        if count_2 == 1:
            str2 = str2 + i;
        else:
            str2 = str2 + "," + i;
    print(str_num[index], end="");
    index = index - 1;
print();
print("짝수의 개수 : ", count_1, "(", str1, ")");
print("홀수의 개수 : ", count_2, "(", str2, ")");