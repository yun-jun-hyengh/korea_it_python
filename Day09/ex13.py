'''
상속(Inheritance)
- 클래스에서 상속이란 부모클래스의 기능을 자식객체가 사용할 수 있다라는것
즉) 자식 클래스는 따로 필드와 메소드를 정의하지 않더라도 부모클래스의
필드와 메소드를 사용할 수 있게 된다 !!
부모클래스 == 슈퍼클래스
자식클래스 == 서브클래스
- 파이썬에서 다중상속이 가능함 !! 
'''
# 부모클래스
class Person:
    name = "";
    age = 0;
    city = ""

    def show(self):
        print("사람클래스 메소드");

# 자식클래스를 생성할 때 상속받을 부모 클래스의 이름을 명시한다
class Student(Person):
    def __init__(self, name, age, city):
        self.name = name;
        self.age = age;
        self.city = city;

    def show_name(self):
        print("이름:", self.name);

    def show_age(self):
        print("나이:", self.age);

    def show_city(self):
        print("도시:", self.city);

student = Student("윤준형", 32, "부산시");
student.show() # 자식객체가 부모 클래스에 있는 멤버를 호출한 예시 !!
student.show_name()
student.show_age()
student.show_city()