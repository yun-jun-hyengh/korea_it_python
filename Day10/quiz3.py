'''
다음 TV클래스가 있고 실행결과를 참고하여 TV 클래스를 상속받은
ColorTv 클래스를 작성하세요

실행결과)
32인치 검정색
'''
class TV:
    def __init__(self, size):
        self.size = size;

class ColorTv(TV):
    def __init__(self, size, color):
        super().__init__(size)
        self.color = color;

    def print_property(self):
        print(self.size, "인치", self.color)

myTv = ColorTv(32, "검정색");
myTv.print_property();