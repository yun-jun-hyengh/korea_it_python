'''

*
**
***
****
*****

'''
for i in range(1, 6):
    print("*" * i)


'''

*****
****
***
**
*

'''
print();
for i in range(5, 0, -1):   
    for j in range(i): 
        print("*", end='')
    print()



'''
    *
   ***
  *****
 *******
*********
'''

print();
for i in range(6):
    for j in range((6 - 1) - i):
        print(' ', end=' ');
    for k in range(2 * i + 1):
        print('*', end=' ');
    print();