# 다중예외처리
try:
    num1 = int(input("숫자입력 >> "))
    num2 = int(input("숫자입력 >> "));
    print(num1 // num2);
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다");
except ValueError:
    print("숫자만 입력이 가능합니다");