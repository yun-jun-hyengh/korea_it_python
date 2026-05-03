'''
1. 문자열 인덱싱과 슬라이싱을 활용하여 5자리로 구성된 학번'31025'를 
학년, 반, 번호로 나눠 출력하는 프로그램을 구현하세요 

실행결과) 3학년 10반 25번
'''
str1 = "31025";
result1 = str1[:1];
result2 = str1[1:3];
result3 = str1[3:5];
print(result1 + "학년", result2 + "반", result3 + "번");

'''
2. "python is good" 문자열을 2번째 위치에 있는 문자 y를 출력하세요 
'''
str2 = "python is good";
print(str2[1]);

'''
3. "123456789" 문자열을 콘솔 첫번째 줄에는 홀수만 두번째 줄에는 짝수만 출력하세요 

실행결과)
13579
2468
'''
str3 = "123456789";
print("홀수 : ", str3[::2]);
print("짝수 : ", str3[1::2]);

'''
4. "Python is amazing" 이 문자열의 길이를 구하세요 
실행결과) 17
'''
print(len("Python is amazing"));