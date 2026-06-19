class Person:
    # 클래스로 객체가 만들어지면 자동으로 self라는 매개변수에 그 객체가 저장됨
    def introduce(self, name):
        self.name = name
        print("안녕하세요 저는", name, "입니다.");

minsu = Person();
minsu.introduce("민수");

namsu = Person();
namsu.introduce("남수");