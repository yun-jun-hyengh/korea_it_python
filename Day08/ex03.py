empty_dict = {};
print(empty_dict); print(type(empty_dict));

student = {
    "name" : "김철수",
    "age" : 20,
    "major" : "컴퓨터공학과",
    "skills" : ["c","c++","java","python"]
};
print(student);
# 딕셔너리에 값 추가 key와 value를 추가
student["grade"] = "A";
print(student);
student["phone"] = "010-1111-1111"
print(student);

# 딕셔너리 수정 기존에 010-1111-1111을 010-2222-2222로 변경
student["phone"] = "010-2222-2222";
print(student);

# 딕셔너리 삭제 : del 키워드와 pop() 메소드를 사용하여 삭제할 수 있다
# del 키워드 : 특정 키를 삭제
del student["age"];
print(student);

# pop 메소드 : 특정 키를 삭제하면서 그 값을 반환받음
remove_student = student.pop("skills");
print(remove_student);
print(student);

# clear() : 딕셔너리 안의 모든 데이터를 삭제
student.clear(); print(student);
