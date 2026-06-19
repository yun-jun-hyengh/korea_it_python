'''
Human 클래스를 생성하여 본인의 이름, 나이, 성별을
각각 생성자를 통해 초기화 하고
이를 출력하세요

실행결과)
이름 >> 윤준형
나이 >> 32
성별 >> 남자
이름은 윤준형
나이는 32
성별은 남자
'''
class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

name = input("이름 >> ");
age = int(input("나이 >> "));
gender = input("성별 >> ");
human = Human(name, age, gender);
print("이름은", human.name)
print("나이는", human.age)
print("성별은", human.gender)