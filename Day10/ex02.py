class Parent:
    
    def __init__(self, name):
        self.name = name; # 인스턴스 변수 name 생성 및 초기화

    def hello(self):
        print("안녕하세요 저는", self.name, "입니다.");


class Child(Parent):
    def bye(self):
        print("안녕히가세요");


parent = Parent("김길동");
parent.hello();

child = Child("홍길동");
child.hello();
child.bye();
