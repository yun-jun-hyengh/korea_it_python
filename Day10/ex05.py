class Person:
    def __init__(self, name):
        self.name = name;

    def introduce(self):
        print("안녕하세요 제 이름은", self.name, "입니다.");

    def go_to_school(self):
        print("저는 학교에 안갑니다.");

    def eat(self):
        print("저는 집에서 밥을 먹습니다");

class Teacher(Person):
    def __init__(self, name):
        self.name = name;

    def introduce(self):
        print("안녕하세요 저는 선생님입니다.");
        print("제 이름은", self.name, "입니다.");

    def go_to_school(self):
        print("저는 학원에 출근합니다.");
        print("퇴근하고 싶다");

    def eat(self):
        print("저는 외식을 합니다.");

class Student(Person):
    def __init__(self, name):
        self.name = name;

    def introduce(self):
        print("안녕하세요 저는 학생입니다");
        print("제 이름은", self.name, "입니다.");

    def go_to_school(self):
        print("저는 학교에 등교합니다");
        print("집가고 싶다");

    def eat(self):
        print("저는 급식을 먹습니다.");


person = Person("홍길동");
person.introduce();
person.go_to_school();
person.eat();

print();

student = Student("김길동");
student.introduce();
student.go_to_school();
student.eat();

print();

teacher = Teacher("아몰라");
teacher.introduce();
teacher.go_to_school();
teacher.eat();