'''
모든 인스턴스가 공통적으로 사용해야될 변수 또는 값이 하나만
유지되어야 하는 상태를 관리할 경우 멤버변수를 선언

인스턴스 변수
- 객체 마다 고유한 값을 가진다 self.name = name

클래스 변수
- 클래스에서 생성된 모든 객체가 값을 공유하는 공통 자원
total_robot = 0;
'''
class Robot:
    total_robot = 0;
    def __init__(self, model):
        self.model = model;
        Robot.total_robot = Robot.total_robot + 1;

rb1 = Robot("A-01010101");
rb2 = Robot("A-01010102");
rb3 = Robot("A-01010103");
print(Robot.total_robot);
