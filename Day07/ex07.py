'''
리스트 입력받기 
'''
# split() 메소드로 공백 기준으로 쪼갠 문자열 조각들을 정수로 바꿔서 최종 리스트로 반환하는 법 
list = list(map(int, input("입력 >> ").split()))
print(list);
