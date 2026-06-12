'''
세트의 연산
- 세트의 연산은 사칙연산이 아닌 집합 연산을 뜻함 
- 교집합, 차집합, 합집합 등 연산을 할 수 있다
'''

# 교집합
# a와 b를 비교하여  a와 b 모두 속하는 요소들로 이뤄진 새로운 세트
# intersection() 메소드를 활용하여 두 세트를 인자로 전달하여 교집합을 반환할 수 있다
set1 = {20,40,60};
set2 = {30,60,90};
intersection_set = set1.intersection(set2);
print(intersection_set);

# 합집합
# 두 세트의 모든 요소를 포함하는 세트 
# 중복을 하용하지 않으므로 합집합의 결과에는 중복요소가 포함하지 않는다 
# union() 메소드를 활용하여 두 세트를 인자로 전달하여 합집합을 반환한다 
set3 = {20,40,60};
set4 = {30,60,90};
union_set = set3.union(set4);
print(union_set);

# 차집합
# 차집합은 두개의 세트 a와 b가 있을 때 세트 a에는 속하지만 세트 b에는 속하지 않는 요소들의 집합 
# difference() 메소드는 두 세트를 인자로 전달하여 차집합을 반환한다 
set5 = {20,40,60};
set6 = {30,60,90};
difference_set = set5.difference(set6);
print(difference_set);