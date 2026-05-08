'''
str(x)
- 인자로 들어온 x를 문자열로 변환시켜서 반환한다 
'''
a = str(10);
print(a); print(type(a));

b = str(3.14);
print(b); print(type(b));

c1 = str(True);
print(c1); print(type(c1));

c2 = str(False);
print(c2); print(type(c2));

'''
chr(x)는 인자로 들어온 x를 문자로 변환시켜서 반환해줌 
특징이 인자로 들어오는 정수형 유니코드(unicode) 값을 인자로 받아 그 번호에 대응하는
문자 하나를 반환한다 

유니코드란?
- 전 세계의 모든 문자를 컴퓨터에서 일관되게 표현하기 위해 각 문자마다 고유한 숫자를 
부여한 국제 문자 표준 
'''
d = chr(65);
print(d); print(type(d));

# TypeError: 'str' object cannot be interpreted as an integer
# 정수가 들어가야 되는데 문자열이 들어가서 생긴 문제 
#e = chr('a');
#print(e);