'''
소멸자
- 객체가 생성될 때 생성자를 호출하는 것처럼 객체가 소멸될 때 호출되는 
메소드를 소멸자라고 한다 
- 소멸자는 객체가 더 이상 사용되지 않고 메모리에서 제거되기 전에 마지막으로 수행되는 
코드 블록이다 
- 소멸자도 기본적으로 존재하며 별도의 선언 없이도 사용할 수 있다 
선언) __del__() 메소드를 사용하여 선언한다 
호출) 메소드 형태로 호출하지 않고 del 키워드를 사용한다 
- 소멸자는 객체 소멸과정에서 발생하는 메모리 해제, 데이터 정리, 확인 메시지 출력 등 다양한 
작업을 수행한다
'''

class Cup:
    def __init__(self, color, brand):
        self.color = color;
        self.brand = brand;

    def __del__(self):
        print(self.brand, "컵 객체가 소멸되었습니다.");


starCafeCup = Cup("green", "starCafe");
print("컵의 색상은", starCafeCup.color);
print("컴의 브랜드는", starCafeCup.brand);
del starCafeCup;
print();

angelCafeCup = Cup("gold", "angelCafe");
print("컵의 색상은", angelCafeCup.color);
print("컴의 브랜드는", angelCafeCup.brand);
del angelCafeCup
print();

blueCafeCup = Cup("blue", "blueCafe");
print("컵의 색상은", blueCafeCup.color);
print("컴의 브랜드는", blueCafeCup.brand);
del blueCafeCup;