for i in range(1, 6):
    for j in range(1, 6):
        print("*", end=' ');
    print();


# print 함수 옵션 
# sep(separation) : 단어를 분리하여 출력 다만 분리할 구분자를 지정할 수 있음 
print("zzzz@zzzz.com", "ssss@naver.com", "aaaa@daum.net", sep=', ')

# end : end 옵션을 사용하면 그 뒤의 출력값이 그 라인에 출력됨(줄바꿈을 하지 않게 됨)
print("I like", end=' '); 
print("money");