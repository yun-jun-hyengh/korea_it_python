'''
세트의 메소드
'''

# 세트에 요소 추가하기 
# add() : 한번에 하나의 요소를 추가할 수 있다
# update() : 여러개의 요소를 한번에 추가할 수 있다 
set1 = {10,20,30};
set1.add(40);
print(set1);
set1.update([50,60]);
print(set1);

# 요소 삭제하기 
# remove(), discard(), pop(), clear()

set2 = {"apple", "banana", "fruit", "coffee", "book", "people"};
set2.remove("banana"); # 삭제잘됨
print(set2);
set2.discard("apple"); # 삭제잘됨
print(set2);

set2.discard("phone"); # 아무반응없음
print(set2);

# remove 메소드는 없는 값을 삭제하려 하면 에러가 난다 
#set2.remove("phone"); # 에러남
#print(set2);

# pop 메소드
# 임의의 요소를 하나 제거하는 역할을 수행하고 제거된 요소를 반환하기도 한다 
print(set2.pop());
print(set2);

# clear()
set2.clear();
print(set2);