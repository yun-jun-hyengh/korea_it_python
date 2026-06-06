tuple_alphabet = ("a", "a", "b", "c", "c", "a")

print(tuple_alphabet.count('a')); # 튜플 안에 있는 a의 개수 
print(tuple_alphabet.count('b')); # 튜플 안에 있는 b의 개수
print(tuple_alphabet.count('c'));

print("=" * 20)
# index() 메소드
# - 튜플 안에서 특정 값을 찾고 싶을 때 index() 메소드를 사용한다 
# - index() 메소드를 사용하면 찾고자 하는 값이 튜플 안에서 어떤 인덱스에 위치하는지 정확히 알 수 있다
print(tuple_alphabet.index("a")); # 튜플 안에 있는 a의 첫 인덱스 번호 반환
print(tuple_alphabet.index("b")); # 튜플 안에 있는 b의 첫 인덱스 번호 반환
print(tuple_alphabet.index("c"))

'''
튜플을 활용하여 데이터 교환
- 튜플은 각 요소를 직접 수정할 수 없지만 두 튜플을 활용하여 간접적으로 
튜플 요소의 값을 교환할 수 있다 
- 새로운 튜플을 생성하고 = 연산자를 사용하여 새로운 튜플의 값을 기존 튜플 변수에 할당한다 
이러한 방식으로 두 변수의 값을 교환가능함 
'''
x = 10;
y = 20;
print("교환전 : x = ", x, ", y = ", y);

(x, y) = (y, x);
print("교환후 : x = ", x, ", y = ", y);