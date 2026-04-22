'''
문자열
- 작은따옴표 혹은 큰따옴표, 삼중따옴표로 둘러싸여 있는 단어나, 문자, 숫자들을 말함
'''

# 작은따옴표 혹은 큰따옴표로 문자열 만들기
str1 = 'Hello World';
str2 = "Hello Python";
print("str1 : ", str1);
print("str2 : ", str2);

# 삼중따옴표로 문자열 만들기 
str3 = '''Hello Java''';
str4 = """Hello Linux""";
print("str3 : ", str3);
print("str4 : ", str4);

# 문자열안에 작은따옴표와 큰 따옴표가 들어 있어야 할 경우가 있다 혹은 개행해서 출력을 해야 한다던지
# 문자열에 작은따옴표 포함하고 싶을 때 
food = "Python's favorite food is perl";
print(food);