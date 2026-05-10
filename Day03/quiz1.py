'''
초를 입력받아 분 / 초의 형태로 출력하세요 

예시)
60  => 1 / 0
70  => 1 / 10
'''

cho = int(input("초 입력 >> "));
result1 = cho // 60;
result2 = cho % 60;
print(result1, " / ", result2);