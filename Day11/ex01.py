'''
모듈(Module)
- 함수, 변수, 클래스 등을 모아놓은 하나의 파일이라고 보면 됨 !!
- 공통된 기능을 하나의 모듈로 구현해 놓고 필요할 때마다 호출하여
재사용할 수 있게끔 해준다
* 파이썬에서 모듈 종류로는 내장모듈, 사용자 정의 모듈이 있다
'''
# 파일 이름이 곧 모듈 이름이 되고 같은 경로에 있어야 불러올 수 있다
import mod
num1 = int(input("숫자입력 >> "))
num2 = int(input("숫자입력 >> "))
print(mod.add_nums(num1, num2))
print(mod.mul_nums(num1, num2))