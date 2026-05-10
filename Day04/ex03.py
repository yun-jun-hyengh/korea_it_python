'''
elif
- 타 언어에서는 else if 라고 보면 됨 
'''
age = int(input("나이입력 >> "));

if age >= 20:
    print("성인입니다.");
elif age >= 13:
    print("청소년입니다.")
elif age >= 8:
    print("어린이입니다.")
elif age >= 0:
    print("아기입니다.");
else:
    print("올바른 나이를 입력해주세요");