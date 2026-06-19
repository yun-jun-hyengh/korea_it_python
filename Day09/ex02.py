class Person:
    def introduce(self):
        print("안녕하세요");

# Person 클래스로 부터 minsu 라는 객체를 생성함
# .(도트연산자) => 객체 내부 변수 및 메소드에 접근하기 위해 사용하는 기호
minsu = Person();
# Person 클래스의 introduce 메소드를 실행하면서 이 함수를 호출한
# 인스턴스가 minsu라는 인스턴스라는 걸 알려준다 !!
minsu.introduce();  # 파이썬 내부적으로 Person.introduce(minsu) 처리
