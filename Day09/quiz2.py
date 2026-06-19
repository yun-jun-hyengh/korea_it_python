'''
Grade 클래스를 작성하세요
3과목의 점수를 입력받아 Grade 객체를 생성하고
평균을 출력하는 메소드를 작성하세요 평균은 정수값으로 출력하면 됩니다
수학 >> 90
과학 >> 88
영어 >> 96
평균은 91
'''
class Grade:
    def average(self, mat, sci, eng):
        return (mat + sci + eng) // 3;

grade = Grade();
mat = int(input("수학 >> "));
sci = int(input("과학 >> "))
eng = int(input("영어 >> "));
print("평균은", grade.average(mat, sci, eng));
