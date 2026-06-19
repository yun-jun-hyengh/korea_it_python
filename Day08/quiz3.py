'''
빈리스트를 선언하여
총 N개의 정수를 해당 리스트에 넣고 정수 v가 몇개인지 구하세요

크기 >> 11
입력 >> 1 4 1 2 4 2 4 2 3 4 4
숫자입력 >> 2
결과 ) 3개
'''
array = []; # 빈리스트 생성
length = int(input("크기 >> "));
for i in range(length): # 입력받은 크기만큼 루프를 돌며
    array.append(int(input("입력 >> "))); # array라는 리스트에 값을 넣음

num = int(input("숫자입력 >> "))
count = 0;
for i in range(len(array)): # array 리스트의 크기만큼 루프 회전
    # 각 인덱스에 접근하면서 입력받은 값과 저장되어 있는 값이 같다면
    if array[i] == num:
        count = count + 1; # count변수값을 1씩 증가시킨다
print(count);