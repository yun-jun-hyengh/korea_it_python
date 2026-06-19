'''
딕셔너리 메소드
'''
user = {"id": "user01", "passwd": "1234", "nickname": "귤빵"};
print(user['id']);
#print(user['id1']);
# get 메소드를 사용하면 존재하지 않는 키값이라도 에러 떨구지 않음
print(user.get('id1'));
print(user.get('nickname'))
# 딕셔너리에 존재하지 않는경우 기본값 지정하기
print(user.get("email", "이메일 없음.."))

# keys() : 딕셔너리에 있는 모든 키값을 불러올 수 있다
print(user.keys());
for key in user.keys():
    print(key);

# 딕셔너리에 있는 모든 value값 가져오기
print(user.values());
score = {"kor": 90, "eng": 85, "mat": 95};
total_score = sum(score.values());
print("총점 : ", total_score);

for key, value in score.items():
    print(f"과목 : {key} 점수 : {value}");

# update() : 여러 데이터를 한번에 수정하기
score.update({"kor": 100, "eng": 75})
print(score);