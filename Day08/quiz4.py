'''
숫자 6개를 입력받아서 리스트에 저장한다음
이를 오름차순으로 정렬하는 프로그램을 작성하세요
단) 숫자는 중복하지 않습니다

입력 >> 5 5 2 3 4 1
출력 >> 1 2 3 4 5
'''
list1 = [];
for i in range(6): # 루프를 돌며 숫자 6개를 입력받아 리스트에 저장
    list1.append(int(input("숫자입력 >> ")));

set1 = set(list1); # set으로 중복을 제거
sorted_list = sorted(set1); # 오름차순 정렬 시킴
print(sorted_list);