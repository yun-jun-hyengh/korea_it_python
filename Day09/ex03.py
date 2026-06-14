class Animal:

    def cry(self, sound):
        print("저의 울음소리는", sound, "입니다.");

cat = Animal();
cat.cry("야옹"); # 고양이가 운다 self 자리에  cat(인스턴스)을 집어넣고 인자로 야용을 전달했으니 울어 !! 

dog = Animal();
dog.cry("멍멍");

'''
지금 예시와 같이 어떤 인스턴스인지 구분하여 울음소리를 낸다 
'''