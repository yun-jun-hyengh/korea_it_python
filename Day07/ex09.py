'''
리스트를 튜플로 튜플을 리스트로 변환
'''
# 리스트를 튜플로 변환 
my_list = [10,20,30];
my_tuple = tuple(my_list); 

print(my_list); print(type(my_list));
print(my_tuple); print(type(my_tuple))

print("-" * 20);

current_tuple = (100,200,300);
current_list = list(current_tuple);

print(current_tuple); print(type(current_tuple));
print(current_list); print(type(current_list))