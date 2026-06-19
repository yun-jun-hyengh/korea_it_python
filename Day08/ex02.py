'''
key값으로 value값 얻기
'''
person = {
    "name" : "kim",
    "age" : 30,
    "phone" : "010-1234-5678",
    "subject" : ["Python", "Java"]
};

print(person);
print(person['name']);
print(person['age']);
print(person['phone']);
print(person['subject'])

'''
이름      가격      재고
메로나    300       20
비비빅    400       3
죠스바    250       100

위의 내용을 참고하여 아이스크림 이름을 키값으로 (가격, 재고) 리스트를
딕셔너리 값으로 저장하세요 
'''
ice_cream = {"메로나" : [300,20], "비비빅" : [400,30],
             "죠스바" : [250,100]};
print(ice_cream)