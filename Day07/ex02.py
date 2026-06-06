'''
리스트 인덱싱
- 원리는 문자열 인덱싱과 동일한 원리이다
'''
names = ["kim", "lee", "park"];
first_name = names[0];
second_name = names[1];
third_name = names[2];
print(first_name); print(second_name); print(third_name);

print("============")
# 리스트 마이너스 인덱스
print(names[-1]);
print(names[-2]);
print(names[-3]);

# 중첩 리스트에서의 인덱싱 
list = [[10,20,30], 1, 3, 9];
print(list[0]); print(list[1]);
# 만약 내가 20에 접근하고 싶다면 ? 
print(list[0][1]);

list1 = [[10,20,30,["사과", "포도"]], 1, 3, 9];
# 만약 사과라는 값을 추출해 내고 싶다면 
print(list1[0]);
print(list1[0][3]);
print(list1[0][3][0])