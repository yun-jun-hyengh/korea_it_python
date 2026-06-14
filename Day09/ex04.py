class Person:
    # 클래스로 객체가 만들어지면 자동으로 self 라는 매개변수에 그 객체가 저장된다 
    def introduce(self, name):
        # 생성된 객체에 name이라는 변수를 생성하여 introduce 메소드 호출 시 전달받은 name 변수에 값을 대입함 
        self.name = name;
        print("안녕하세요 저는", name, "입니다.");

minsu = Person();
minsu.introduce("민수");

namsu = Person();
namsu.introduce("남수");
