'''
finally
- 예외 발생 유무와 상관없이 실행되는 구문이면 생략할 수 있다
- 예외처리를 할때 예외와 상관없이 반드시 처리해야 하는 구문들을
작성할 때 사용한다
'''
try:
    score = int(input("숫자입력 >> "))
    if score >= 60:
        print("합격");
    else:
        print("불합격");
except Exception:
    print("숫자만 입력할 수 있습니다")
finally:
    print("프로그램 종료");