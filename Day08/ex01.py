'''
딕셔너리
- 키(key)와 값(value)의 쌍으로 이뤄진 자료형
- key값을 통해 value값을 찾아낼 수 있다 

형태)
{
    "key1" : value1
    "key2" : value2
}
'''

person = {
    "name" : "윤준형",
    "age" : 32,
    "phone" : "010-3528-8515",
    "subject" : ["Linux", "java", "python", "c", "c++", "Spring boot", "Next.js", "Docker", "Android"]
}

print(person); 
print(type(person))