class Animal:

    def __init__(self, name, sound):
        self.name = name;
        self.sound = sound;

    def __del__(self):
        print(self.name, "가죽었습니다.");

    def cry(self):
        print(self.sound);

cat = Animal("나비", "야옹");
cat.cry();

dog = Animal("껌둥이", "멍멍");
dog.cry();

'''
객체 소멸을 위해 반드시 del 키워드를 사용하여 직접 사용해야 하는건 아님 
사실상 프로그램이 종료될 때에는 모든 객체의 소멸자가 자동으로 호출된다 
'''