'''
super() 메소드
- 부모클래스의 생성자를 호출하는 메소드
- 슈퍼클래스가 필요한 데이터는 슈퍼 클래스의 생성자를 호출하여 전달하고 
서브 클래스가 추가로 필요한 데이터는  self 객체를 통해 할당할 수 있다 
'''

class Car:
    def __init__(self, color):
        self.color = color;

    def ride(self):
        print(self.color, "car is riding");


class Bus(Car):
    def __init__(self, color, bell_sound):
        super().__init__(color) # super() 메소드를 통해 color 인자값 전달 및 호출
        self.bell_sound = bell_sound;

    def press_bell(self):
        print(self.bell_sound);

bus = Bus("Red", "Diing-Dong");
bus.ride();
bus.press_bell();

'''
Bus 클래스는 Car 클래스를 상속받아 확장되었다 
Bus 클래스는 Car 클래스의 모든 기능을 가지고 있으며 추가로 bell_sound
속성을 가지도록 설계됨
서브클래스는 슈퍼클래스에서 확장하여 별도의 데이터를 가질 수 있다
'''