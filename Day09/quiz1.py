'''
Rider 클래스를 만들고 해당 클래스는 deliver라는 메소드를 가진다
이 메소드는 음식이름을 인자로 받아서 "ㅁㅁㅁ 배달을 시작합니다" 라고
출력이 되어야 됨
Rider 클래스를 만들고 인스턴스를 만들어서 입력받은 값을 deliver 메소드로
전달하여치킨 배달을 시작합니다  혹은 피자 배달을 시작합니다라는
문구를 콘솔에 출력하는 프로그램을 작성하세요 ~~
'''
class Rider:
    def deliver(self, food):
        return food + " 배달을 시작합니다";
rider = Rider()
food = input("음식입력 >> ");
print(rider.deliver(food));