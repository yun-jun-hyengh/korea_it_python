'''
A와 B가 한 오디션 프로의 결승전에 진출했다
결승전의 승자는 심사위원의 투표로 결정된다
심사위원의 투표 결과가 주어졌을 때 어떤 사람이 우승하는지 구하세요
단) 소문자로 입력받아도 제대로 작동되도록 만들어 주세요

입력 >> AABBBBABABB
(A는 4표, B는 7표)
우승자는 B입니다.
'''
a = input("입력 >> ");
a_upper = a.upper(); # 입력받은 문자열을 모두 대문자로 변환
count_a = a_upper.count("A"); # A의 개수는 몇개있는지 확인
count_b = a_upper.count("B"); # B의 개수는 몇개있는지 확인
print(f'(A는 {count_a}표, B는 {count_b}표)');
if count_a > count_b:
    print("우승자는 A입니다");
else:
    print("우승자는 B입니다")