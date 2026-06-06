'''
컬렉션 자료형
-  컬렉션(Collection) 이란 파이썬에서 여러 요소들을 모아서 처리할 수 있도록 해주는 자료구조를 말한다 
- 파이썬의 컬렉션 자료형에는 리스트, 튜플, 딕셔너리, set(집합) 이 있다 

리스트(List)
- 여러개의 데이터를 하나의 변수에 저장하고 관리할 수 있다 
변수는 하나의 데이터만 저장하는 반면 리스트는 여러개의 데이터를 저장가능함 
- 리스트에는 모든 타입의 데이터는 모두 다 저장이 가능하다 
즉) []안에 있는 값들의 타입이 달라도 상관이 없다 
'''

number = [10,20,30,40]; # 숫자리스트
print(number); print(type(number));

alphabets = ['a','b','c','d']; # 문자 리스트
print(alphabets); print(type(alphabets));

bool_list = [True, False]; # 논리값 리스트
print(bool_list); print(type(bool_list));

greetings = ['hi', "안녕하세요", "hello"]; # 문자열 리스트
print(greetings); print(type(greetings));

# 숫자, 문자, 논리값을 혼합하여 담은 리스트 
example = [3, 10, "y", True];
print(example); print(type(example));

# 리스트 안에 리스트 
list1 = [3, 10, ["살목지", "곤지암", "영덕흉가"]];
print(list1); print(type(list1));