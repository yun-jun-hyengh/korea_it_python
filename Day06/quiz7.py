balance = 0;
def println():
    print("-------------------------------");
    print("1.예금 | 2.출금 | 3.잔금 | 4.종료");
    print("-------------------------------");


def inputFunction(string):
    num = int(input(string));
    return num;

def deposit(money):
    global balance;
    balance = balance + money;

def withDrawal(money):
    global balance;
    if money > balance:
        print("잔액이 부족합니다.");
    else:
        balance = balance - money;

def balanceInquiry():
    print("잔액 :", balance);

while True:
    println();
    menu_tooltip = "메뉴 입력 >> "
    num = inputFunction(menu_tooltip);
    if num == 1:
        str1 = "예금액 >> "
        money = inputFunction(str1);
        deposit(money);
    elif num == 2:
        str2 = "출금액 >> "
        money = inputFunction(str2);
        withDrawal(money)
    elif num == 3:
        balanceInquiry();
    elif num == 4:
        print("프로그램 종료");
        break;

'''
* 리팩토링이란
- 프로그램의 결과는 유지하면서 이해하기 쉽고 유지보수하기 좋은 코드로 개선하는 작업

[과업(ATM 퀴즈 소스코드 리팩토링)]
콘솔 창에서 작동 하는 atm기 시스템을 구현하려고 한다 프로그램은 실행되면 (1.예금 2.출금 3.잔금
4. 종료)를 보여 주고 사용자 가 종료를 누르기 전까지 계속 해서 서비스 를 제공 해야 한다

[제한조건]
코드의 재 사용성과 가독성을 위해 기능별로 Function을 구현하세요
메뉴 출력 기능, 입력 기능, 입금 기능, 출금 기능, 잔액 조회 기능이 각각 독립된 함수 여야 합니다
'''