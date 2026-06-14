class Calculator:
    def add(self, a, b):
        return a + b;

    def sub(self, a, b):
        return a - b;

    def mul(self, a, b):
        return a * b;

    def div(self, a, b):
        return a / b;

cal = Calculator();

num1 = int(input("입력 >> "));
num2 = int(input("입력 >> "))
print("덧셈 : ", cal.add(num1, num2));
print("뺄셈 : ", cal.sub(num1, num2));
print("곱셈 : ", cal.mul(num1, num2));
print("나눗셈 : ", cal.div(num1, num2));