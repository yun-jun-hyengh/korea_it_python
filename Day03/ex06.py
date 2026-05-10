'''
논리 연산자
- 논리 연산자는 논리적인 연산을 수행하여 참 거짓을 판별한다 

연산자
and : 좌항 우항 비교했을 때 좌항 우항 모두 True 일 때만 True를 반환하고 나머지는 모두 False를 반환
or : 좌항 우항 비교했을 때 좌항 우항 둘중 하나라도 True이면 True를 반환하고 두 항 모두 False이면 False를 반환
not : True를 False로 False를 True로 바꿈
'''
a = True; 
b = False; 
c = True; 
d = False;

print("##### and 연산자 #####");
print(a and b);
print(a and c);
print(b and d);

print("##### or 연산자 #####")
print(a or b);
print(a or c);
print(b or d);


print("##### not 연산자 #####")
power = False # 전원꺼짐
power = not power; # 전원킴(False를 True로)
print(power);