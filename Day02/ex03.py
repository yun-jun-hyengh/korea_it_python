'''
float(x)
- 인자로 들어온 x를 실수 타입으로 변환해준다 
'''

a = 10;
a1 = float(a);
print("a : ", a); print("a : ", type(a));
print("a1 : ", a1); print("a1 : ", type(a1));

b = True;
b1 = float(b);
print("b : ", b); print("b : ", type(b));
print("b1 : ", b1); print("b1 : ", type(b1));

c = 'a';
#c1 = float(c); 에러발생 (문자열을 실수로 변환하려 했기에)
