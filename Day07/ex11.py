'''
세트(set)
- 리스트와 달리 순서가 없고 중복된 값을 허용하지 않는 자료구조이다 
- 리스트와 튜플은 각각 대괄호[], 소괄호()를 사용하여 표현했지만 세트는 중괄호{}를 사용하여 표현한다 
- 튜플과 리스트처럼 중괄호 안에 담고 싶은 요소들을 쉼표로 구분하여 나열하면 됨 
- 다양한 데이터를 저장할 수 잇다 
- 인덱싱과 슬라이싱을 활용할 수 없다 왜냐 애초에 순서가 없는 데이터 구조이기에 
인덱스 번호가 존재하지 않는다
'''
fruits = {"apple", "banana", "orange"};
print(fruits); print(type(fruits));

#set_banana = {"banana", "banana milk"};
#print(set_banana[0]);

# 다양한 자료형을 세트로 변환 
str1 = "apple";
list1 = [10,20,30];
tuple1 = (10,20,30);

print("str1 : ", str1);
print("list1 : ", list1);
print("tuple1 : ", tuple1);

# set으로 변환
set_str = set(str1);
set_list = set(list1);
set_tuple = set(tuple1);
print("<set으로 변환한 자료형>");
print("set_str : ", set_str);
print("set_list : ", set_list);
print("set_tuple : ", set_tuple);