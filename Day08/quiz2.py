'''
아래 두개의 튜플을 하나의 딕셔너리로 변환하세요
출력결과)
{"apple": 300, "pear": 250, "peach": 400}
'''
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
fruits = {};
for i in range(len(keys)):
    fruits[keys[i]] = vals[i];
print(fruits)