'''
클래스를 이용하여 해당 기능을 구현하세요
1번메뉴를 선택하면 회원가입
2번메뉴를 선택하면 로그인
3번메뉴는 프로그램 종료

1. User 클래스를 만들어주세요 회원정보는(아이디, 비밀번호, 이름) 속성을 가집니다
2. UserManager 클래스를 만들어 주세요 이 클래스는 회원가입, 로그인 시스템의
기능을 담당합니다
2-1 : 회원가입시 기존에 회원가입한 아이디라면 이미 존재하는 아이디라고 출력
중복된 아이디가 아니라면 회원가입 정상적으로 등록시키고 성공 메시지 출력
2-2 : 로그인시 아이디와 비밀번호를 입력하는데 만약 아이디가 존재하지 않는다면
"로그인 실패 : 아이디가 존재하지 않습니다" 출력 만약 비밀번호가 틀렸다면
"로그인 실패 : 비밀번호가 일치하지 않습니다" 출력 아이디와 비밀번호가 일치하다면
로그인 성공시키기 !!
3. 프로그램 종료 하기 !!
'''

class User:
    def __init__(self, user_id, user_pw, user_name):
        self.user_id = user_id
        self.user_pw = user_pw
        self.user_name = user_name

class UserManager:
    def __init__(self):
        self.users = {};
    # 딕셔너리에 값을 넣을때 key 값을 user_id 를 key로 잡고 values 는 레퍼런스 자체를 넣을것
    # 회원가입
    def register(self, user_id, user_pw, user_name):
        if user_id in self.users:
            print("가입실패", user_id, "는 이미 존재하는 아이디입니다.");
            return False;
        new_user = User(user_id, user_pw, user_name);
        self.users[user_id] = new_user;
        print("회원가입 성공", user_name, "님 회원가입을 축하합니다.");
        return True;

    # 로그인
    def login(self, user_id, user_pw):
        if user_id not in self.users:
            print("로그인 실패 : 아이디가 존재하지 않습니다")
            return False;
        user = self.users[user_id];
        if user.user_pw == user_pw:
            print("로그인 성공 :", user.user_name, "님이 로그인하였습니다.");
            return True;
        else:
            print("로그인 실패 : 비밀번호가 일치하지 않습니다");
            return False;

userManager = UserManager();
while True:
    print("★ 회원관리시스템 ★")
    print("1. 회원가입")
    print("2. 로그인")
    print("3. 프로그램 종료");

    menu = int(input("메뉴선택 >> "));

    if menu == 1:
        id = input("아이디 입력 >> ");
        pw = input("비밀번호 입력 >> ");
        name = input("이름 입력 >> ")
        userManager.register(id, pw, name);
    elif menu == 2:
        id = input("아이디 입력 >> ")
        pw = input("비밀번호 입력 >> ")
        userManager.login(id, pw)
    elif menu == 3:
        print("프로그램 종료");
        break;


