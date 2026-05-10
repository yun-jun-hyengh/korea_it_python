'''
커피 테이크아웃 가게에서 카페 모카를 2잔 산 후 커피 값을 10000원을 지불하고 영수증과 
거스름돈을 받았다. 카페 모카의 가격이 3500원이고 부가세가 10%라면 부가세와 손님에게 
받을 상품의 총액과 거스름돈을 계산하여 출력하는 프로그램을 작성하세요 

실행결과)
카페모카단가입력 >> 3500
수량입력 >> 2
지불한 돈 입력 >> 10000
부가세 : 700
상품총액 : 7700
거스름돈 : 2300
'''

cafeMochaUnitPrice = int(input("카페모카단가입력 >> "))
count = int(input("수량입력 >> "));
pay = int(input("지불한 돈 입력 >> "));

surtax = int((cafeMochaUnitPrice * count) * 0.1)
total_amount = cafeMochaUnitPrice * count + surtax;
change_money = pay - total_amount;
print("부가세 : ", surtax);
print("상품총액 : ", total_amount);
print("거스름돈 : ", change_money);