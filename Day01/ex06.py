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
#food1 = 'Python's favorite food is perl'; 큰따옴표 안에 들어 있는 작은따옴표는 문자열을 나타내는 기호로 인식되지 않는다. 

# 문자열에 큰따옴표 포함시키기 
#say = ""Python is very is." he says."; 작은따옴표 안에 사용된 큰따옴표는 문자열을 만드는 기호로 인식되지 않는다.
say = '"Python is very very easy." he says.';
print(say);

# 역슬래시를 사용해서 작은따옴표와 큰따옴표를 문자열에 포함시키기 
food1 = 'Python\'s favorite food is perl';
say1 = "\"Python is very easy.\" he says.";
print(food1);
print(say1);

# 여러 줄인 문자열을 변수에 대입하기 
address = '''우편번호 123456
서울시 영등포구 여의도동
서울빌딩 501호
'''
print("address : ", address);

address1 = "우편변호 123456\n서울시 영등포구 여의도동\n서울빌딩 501호";
print("address1 : ", address1);