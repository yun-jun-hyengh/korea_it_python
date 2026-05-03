'''
형변환(Type Casting)
- 해당 변후의 자료형을 다른 자료형으로 변환하는 것을 의미함 
예시로 int -> str 타입으로 변환하는 행위 
- 파이썬에서 형변환은 변환하고자 하는 타입의 이름으로 값 혹은 변수명을 감싸주면된다 

정수변환 -> int()
실수변환 -> float()
문자열변환 -> str()
문자변환 -> chr()
불리언변환 -> bool()
'''

# int(x)
# 인자로 들어온 x를 정수 타입으로 변환해준다 
a = 10;
a1 = int(a); # 정수를 정수로 변환(가능은 하지만 의미없다)
print(a1); print(type(a1));

print("=" * 40);

b = 3.14;
b1 = int(b);
print('b : ', b); print('b: ', type(b));
print('b1 : ', b1); print('b1 : ', type(b1));

print("=" * 40);

c = True
c1 = int(c);
print('c : ', c); print('c : ', type(c));
print('c1 : ', c1); print('c1 : ', type(c1));

print("=" * 40);

d = False
d1 = int(d);
print('d : ', d); print('d : ', type(d));
print('d1 : ', d1); print('d1 : ', type(d1));

print("=" * 40)

# 문자열을 정수로 변환하려 하면 오류가 발생함 
# a로도 실습해보기 
e = 'abc';
#e1 = int(e);
print('e : ', e); print('e : ', type(e));
#print('e1 : ', e1); print('e1 : ', type(e1));

'''
* 파이썬에서는 문자(Character) 자료형이 따로 없다 
다른 언어 글자한개 'a' 는 char 글자 한개이상이다 "ab" 라면 String 으로 엄격하게 구분한다 
파이썬은 글자가 한개든 백개든 따옴표 안에 있다면 무조껀 str 타입이다 
방금 a와 같이 자바에서 형변환을 할경우 아스키코드 값이 나온다 !! 
'''