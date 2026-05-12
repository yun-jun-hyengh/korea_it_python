'''
사용자로부터 임의의 양의 정수를 하나 입력받은 뒤 1부터 입력받은 정수까지 모든 
수의 합계를 출력하는 프로그램을 작성하세요 
'''
num = int(input("숫자입력 >> "));
sum = 0;
for i in range(1, num + 1):
    sum = sum + i;
print("합계 : ", sum);