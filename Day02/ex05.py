'''
bool(x)
- 인자로 들어온 x를 bool 타입으로 변환시킴 
* 0을 제외한 모든 숫자는 True로 취급함 !! 
컴퓨터 세상에서는 
'''
a = bool(54);
print(a); print(type(a));

b = bool(100);
print(b); print(type(b));

c = bool(0);
print(c); print(type(c));

d = bool(-1);
print(d); print(type(d));

e = bool(3.14);
print(e); print(type(e));

# 문자열을 bool 변환시에는 문자열이 비어있냐 비어있지 않냐에 따라 True False로 갈림 
f = bool('dfsdfs');
print(f); print(type(f)); 

g = bool('');
print(g); print(type(g));