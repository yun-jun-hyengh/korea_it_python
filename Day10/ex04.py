'''
메소드 오버라이딩
- 메소드 재정의
- 메소드 이름이 같고 매개변수 개수가 같지만 기능만 다른것
즉 부모클래스에 있는 메소드를 자식클래스에서 재정의 해서 사용한다 
'''

class Car:
    def __init__(self, color):
        self.color = color;

    def ride(self):
        print(self.color, "차가 달립니다.");
        print("쌩쌩")

class Bus(Car):
    def __init__(self, color, bell_sound):
        super().__init__(color)
        self.bell_sound = bell_sound;

    def ride(self):
        print(self.color, "버스가 달립니다.");
        print("천천히")
    
    def press_bell(self):
        print(self.bell_sound);

car = Car("Blue");
car.ride();
print();

bus = Bus("Red", "Ding-Dong");
bus.ride(); # 오버라이딩된 메소드가 호출
bus.press_bell();