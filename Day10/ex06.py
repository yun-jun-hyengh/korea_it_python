'''
다중상속
- 둘 이상의 클래스를 상속하는 것을 말함 
- 상속받을 클래스를 콤마로 구분해서 나열하면 된다 즉) 부모가 둘이라 보면됨

다중상속의 문제점
- 클래스간의 관계가 모호해진다 또한 이로인해 여러 가지 문제를 일으킬 수 있다(비지니스가 꼬임)
- Java같은 경우 클래스간 다중상속을 불허한다 
- 다중상속은 꼭 필요한게 아님 !! 
'''

class Person:
    def greeting(self):
        print("안녕하세요");

class University:
    def greeting(self):
        print("안녕하세요");

class Undergraduate(Person, University):
    def study(self):
        print("공부하기");