class Animal:

    def cry(self, sound):
        print("저의 울음소리는", sound + "입니다.");

cat = Animal();
cat.cry("야옹");

dog = Animal();
dog.cry("멍멍");
'''
self
- 객체 자신을 가리키는 특별한 변수 
즉) 메소드 내에서 객체의 속성이나 다른 메소드에 접근하고 
이를 변경할 때 사용한다
'''