'''
수정 불가능한 회원 명단을 수정해보세요 
절때 수정할 수 없는 회원 명단이 있는데 이를 
철수 영의 민수 지민 이 출력되도록 구현해 주세요 

출력결과
철수 영희 민수 지민
'''
members = ("철수", "영희", "민수");
list_members = list(members);
list_members.append("지민");

for i in list_members:
    print(i, end=' ')