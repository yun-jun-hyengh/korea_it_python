money = 5000;

while money >= 3000:
    print("아이스크림을 사 먹었습니다.", money);
    money = money - 1000;

'''
아이스크림을 몇번 구매했는지 확인하려면 ??
'''

pay = 5000;
cnt = 0;
while pay >= 3000:
    pay = pay - 1000;
    cnt = cnt + 1;
    print("아이스크림을", cnt, "번 사먹었습니다.");