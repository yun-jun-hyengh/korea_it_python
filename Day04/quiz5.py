'''
어떤 차의 높이가 170cm 이다 
이 차는 3개의 터널을 차례대로 지나게 될 것이다.
터널의 높이가 차의 높이보다 같거나 낮다면 차는 터널과 충돌하여 사고가 날 것이다 
터널의 높이가 차례대로 3개 주어지면 터널을 무사히 잘 통과하면 PASS 사고가 난다면 CRASH를 
출력하세요 

입출력 예시)
터널1 >> 170 
터널2 >> 168 
터널3 >> 175
출력 : CRASH 
'''

car = 170;
tunnel_1 = int(input("터널1 >> "));
tunnel_2 = int(input("터널2 >> "));
tunnel_3 = int(input("터널3 >> "));

if tunnel_1 > 170 and tunnel_2 > 170 and tunnel_3 > 170:
    print("PASS");
else:
    print("CRASH");