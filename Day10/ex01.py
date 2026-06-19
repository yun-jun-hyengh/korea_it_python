'''
상속
- 상속은 파이썬뿐 아니라 자바, c++등 다양한 객체 지향 프로그래밍 언어에서 제공하는 중요한 기능이다

상속의 역할)
기능과 데이터를 물려주는 부모역할
기능과 데이터를 물려받는 자식역할
'''
class Parent:
    def hello(self):
        print("안녕하세요");

class Child(Parent):
    def bye(self):
        print("안녕히가세요");

parent = Parent();
parent.hello(); # 부모객체는 자식멤버에 접근할 수 없다

# 자식객체는 부모 멤버에 자유롭게 접근이 가능하다 
child = Child();
child.hello();
child.bye();