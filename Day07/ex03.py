'''
리스트 슬라이싱

예시)
리스트[start:stop:step]
'''
example = [3, 9, "y", 2, "K", True];
print(example[1:4]);
print(example[2:6]);
print(example[0:5])

# 중첩된 리스트에서 슬라이싱
my_list = ["Mit", [30,60,90], "red", "green"];
# 만약 30 60 을 추출하고 싶다면 
print(my_list[1][0:2])

# 리스트의 연산
# 리스트 더하기 : 여러개의 리스트를 하나의 리스트로 합쳐 새로운 리스트를 만들 수 있다
list1 = ["A", "B", "C"];
list2 = ["D", "E"];
list3 = list1 + list2;
print(list3);

# 리스트 곱하기 : 해당 리스트를 반복하여 더 큰 리스트를 만들 수 있다
list_mul = ["10","20","30"];
result = list_mul * 5;
print(result);