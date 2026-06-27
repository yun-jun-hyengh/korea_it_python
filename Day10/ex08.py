try:
    # 파이썬에서 값이 없음을 나타낼 때 대문자로 시작하는 None을 사용한다
    # NoneType 클래스의 특별한 데이터 형이고
    # 즉 객체에 null이 할당됨 초기화 되지 않음을 의미함 
    str_array = None
    print("str_array[0]:", str_array[0]);
except TypeError:
    print("str_array 리스트가 None 이므로 접근할 수 없습니다")


