'''
2단부터 9단까지 구구단을 출력하되 
짝수단은 역순 홀수단은 정순으로 출력하세요 

2 x 9 = 18
2 x 8 = 16
..
3 x 1 = 3
3 x 2 = 6
...
'''

for i in range(2, 10):
    if i % 2 == 0:
        for j in range(9, 0, -1):
            print(i, "x", j, "=", i * j);
        print();
    else:
        for j in range(1, 10):
            print(i, "x", j, "=", i * j);
        print();