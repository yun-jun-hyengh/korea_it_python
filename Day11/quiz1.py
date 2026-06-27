'''
컴퓨터가 1 ~ 100 숫자중 하나를 랜덤으로 정한다 사용자는 이 숫자를 맞춰야
한다 입력한 숫자보다 정답이 크면 "UP"을 출력 입력한 숫자보다 정답이
작으면 "DOWN" 출력 정답을 맞추면 정답입니다 O회 맞에 맞췄어요 를 출력하고
지금까지 숫자를 입력한 횟수를 알려준다
단) 사용자가 숫자가 아닌 값을 입력받았을 때 다시 입력받도록 구현을 하고
잘못입력 받은 것도 게임횟수에 추가를 시켜야 된다

실행예시)
컴퓨터가 1 ~ 100중 랜덤 숫자 하나를 정합니다 이
이 숫자를 맞춰주세요
숫자입력 >> 50
DOWN
숫자입력 >> ㄴㅇㄱㄹㄷ
숫자만 입력이 가능합니다
숫자입력 >> 30
up
숫자입력 >> 35
정답입니다 4회 만에 맞췄어요
'''
import random
computer = random.randint(1,100);
count = 0;
while True:
    try:
        num = int(input("숫자입력 >> "));
        if num > computer:
            print("DOWN");
            count += 1;
        elif num < computer:
            print("UP");
            count += 1;
        elif num == computer:
            count += 1;
            print("정답입니다", count, "회 만에 맞췄습니다.");
            break;
    except Exception as e:
        print("숫자만 입력가능합니다 다시 입력해주세요");
        count += 1;





