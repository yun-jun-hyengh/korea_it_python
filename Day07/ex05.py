'''
리스트 다루기
'''

'''
append() 메소드
- 리스트에 요소를 추가하고 싶을 때 사용
- 리스트의 마지막에 새로운 원소를 추가한다 
'''
num = [10,20,30];
print(num);
num.append(40);
print(num);
num.append(50);
print(num);

'''
insert() 메소드
- 삽입하고자 하는 위치(인덱스)를 지정해서 데이터를 삽입할 수 있다
리스트.insert(위치,요소) => 첫 번째 인자[위치] 두 번째 인자[요소]를 파라메타로 전달 
'''
num.insert(1, 200);
print(num);

'''
extend()
- append() 메소드는 한번에 하나의 요소만 추가할 수 있지만 extend() 메소드는 여러개의 요소를 
동시에 리스트에 추가하는데 유용하다
'''
extend_numbers = [60,70,80,90];
num.extend(extend_numbers);
print(num);

'''
리스트 삭제
- remove(), pop()

remove()
- 해당 리스트에서 항목을 값으로 삭제하며, 인덱스 번호로는 삭제하지 않는다 
- remove 메소드 인자로 넘긴 값이 같은 항목이 리스트 안에 하나 이상 존재한다면 
맨 처음 발견한 요소를 삭제한다 

pop()
- 원하는 위치의 요소를 지정하여 삭제를 수행할 수 있다
'''
colors = ["black", "yellow", "red", "black"];
colors.remove("black");
print(colors);

colors.pop(1);
print(colors);

# len() : 리스트 길이 확인
print("colors 리스트 길이 :", len(colors))

# 리스트 반전 : reverse()
# 리스트의 요소 순서를 반전시켜 원본 리스트를 변경한다 
list_num = [2,7,5,3,8,9];
list_num.reverse();
print(list_num);
