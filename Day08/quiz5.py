'''
랜덤 모듈을 이용해 10개의 수를 추출하여 (1 ~ 30까지 랜덤숫자지정)
리스트에 저장한 후 저장된 값들 중 최대값과 최소값을
구하는 코드를 작성해 주세요
'''
import random
num_list = [];
for i in range(10):
    temp = random.randint(1, 30);
    num_list.append(temp);

#print(num_list);
print("최대값 : ", max(num_list));
print("최소값 : ", min(num_list));
