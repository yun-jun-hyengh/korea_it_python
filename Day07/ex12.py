'''
set을 list와 tuple로 변환하기 
'''
my_set = {10,20,30,40};
#print(type(my_set))
# 리스트로 변환
my_list = list(my_set);
print(my_list);
print(my_list[2]);

my_tuple = tuple(my_set);
print(my_tuple);
print(my_tuple[2]);