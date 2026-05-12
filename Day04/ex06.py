'''
성적 관리 프로그램
'''
score = int(input("점수입력 >> "));
if score >= 90:
    if score >= 95:
        print("A+학점");
    else:
        print("A학점");
elif score >= 80:
    if score >= 85:
        print("B+학점");
    else:
        print("B학점");
elif score >= 70:
    if score >= 75:
        print("C+학점");
    else:
        print("C학점");
elif score >= 60:
    if score >= 65:
        print("D+학점");
    else:
        print("D학점");
else:
    print("F학점");