'''
논리형(bool)
- 논리형은 True(참), False(거짓) 두가지 값만 가질 수 있다.
- True 와 False는 반드시 첫글자를 대문자로 작성해야 한다 !! 
'''

a = True; print(a);
b = False; print(b);
#a1 = true; print(a1);

# 파이썬에서 False는 값이 없는 모든 경우에 해당한다 예시로 숫자 0, 빈문자열, 빈 리스트 등 모두 False로 인식
print('bool : ', bool(0));
print('bool : ', bool(''));
print('bool : ', bool([]));