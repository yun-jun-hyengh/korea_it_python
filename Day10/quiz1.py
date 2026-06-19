'''
다음 지시사항을 읽고 책 제목과 저자 정보를 저장할 수 있는 Book 클래스를 생성하세요 

1. 책 제목과 책 저자 정보를 출력하는 print_info() 메소드를 구현하세요 
2. 다음과 같은 방법으로 book1과 book2 인스턴스를 생성하세요 

실행결과)
책 제목 : 어린왕자
책 저자 : 생태쥐페리
책 제목 : 꽃을 보듯 너를 본다
책 저자 : 나태주
'''
class Book:
    def __init__(self, title, writer):
        self.title = title;
        self.writer = writer;

    def print_info(self):
        print("책 제목:", self.title);
        print("책 저자:", self.writer);

book1 = Book("어린왕자", "생태쥐페리");
book2 = Book("꽃을 보듯 너를 본다", "나태주");
book1.print_info();
book2.print_info();