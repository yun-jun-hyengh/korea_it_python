class Person:
    def introduce(self):
        print("안녕하세요");

minsu = Person();
minsu.introduce();

'''
self
- 객체 자신을 가리키는 특별한 변수임 
즉) 메소드 내에서 객체의 속성이나 다른 메소드에 접근하고 이를 변경할 때 사용한다 

minsu.introduce();
파이썬이 내부적으로 변환해서 실행하는 형태 => Person.introduce(minsu)
한마디로 Person 클래스의 introduce 함수를 실행하면서 이 함수를 호출한 인스턴스는 minsu라고 알려준다 
'''