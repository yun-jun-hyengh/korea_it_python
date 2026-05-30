def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i;
    elif choice == "mul":
        result = 1;
        for i in args:
            result = result * i;
    return result;


result1 = add_mul('add', 10,20,30,40,50);
result2 = add_mul('mul', 1,2,3,4,5);

print(result1);
print(result2);