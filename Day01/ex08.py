'''
문자열 인덱싱
- 인덱싱(Indexing)이란 무언가를 가리킨다라는 뜻
- 문자열의 각 문자는 고유한 인덱스 번호를 가짐 
'''
a = "Hello";
first_index = a[0];
second_index = a[1];
third_index = a[2];
print("first_index : ", first_index);
print("second_index : ", second_index);
print("third_index : ", third_index);

'''
파이썬은 문자열에 인덱스를 부여할 때 타 언어와 차이점은 마이너스(-) 인덱스가 존재한다 
문자열의 맨 끝의 문자를 -1로 시작한다 
'''
last_char = a[-1];
print("last_char : ", last_char);
second_char = a[-2];
print("second_char : ", second_char);
third_char = a[-3];
print("third_char : ", third_char);

# 공백도 문자열에 포함(공백또한 문자열 인덱스 번호가 존재한다)
str1 = "Hello World";
print("str1[5] : ", str1[5]);
print("str1[6] : ", str1[6]);

# 인덱싱을 활용하여 한문자만 아닌 단어를 추출해 낼 경우 
str2 = "Life is too short, You need Python";
addStr = str2[0] + str2[1] + str2[2] + str2[3];
print("addStr : ", addStr);