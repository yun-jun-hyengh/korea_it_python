'''
튜플(Tuple)
- 리스트와 유사한 형태를 가진다 리스트와 마찬가지로 순서가 있는 데이터의 집합이다
- 리스트와의 차이점은 튜플은 불변이라는 특징을 가지고 있다 
즉) 한번 생성된 후에는 요소의 값을 변경하거나 삭제할 수 없다 
- 리스트는 대괄호로 표현되는 반면 튜플은 소괄호를 사용하여 표현한다 
- 리스트와 마찬가지로 쉼표로 요소들을 구분하며 원하는 모든 종류의 데이터를 담을 수 있다 
'''
empty_tuple = () # 빈 튜플 생성
print(empty_tuple); 
print(type(empty_tuple))

alphabets = ('a','b','c');
print(alphabets);

# 튜플 인덱싱
names = ("kim", "lee", "park");
first_name = names[0];
second_name = names[1];
third_name = names[2];
print(first_name); print(second_name); print(third_name)

# 튜플 슬라이싱
example = (3, 9, "y", 2, "k", True);
print(example[1:4]);
print(example[2:6])
print(example[0:5])

# 튜플과 리스트 비교 
list1 = [30,40,50];
tuple1 = (30,40,50);

list1[0] = 300;
#tuple1[0] = 300; # 값을 변경할 수 없다 
print(list1); 
#print(tuple1);

list1.append(10);
print(list1);

#tuple1.append(10); # 튜플은 추가 또한 불가능 
#print(tuple1);