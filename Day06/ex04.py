'''
가변인자
- 개수가 정해지지 않는 매개변수를 함수의 파라메타로 전달할 경우
- *args => 임의로 정한 변수 이름 
args는 매개변수를 뜻하는 영단어 arguments의 약자이며 관례적으로 이런식으로 표현을 한다 
'''
def add_many(*args):
    result = 0;
    for i in args:
        result = result + i;
    return result;

print(add_many(1,2,3));
print(add_many(1,2,3,4,5))
print(add_many(1,2,3,4,5,6,7,8,9,10))
