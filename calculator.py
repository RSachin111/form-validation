
num1 =int(input("Enter first number "))
num2 =int(input("Enter second  number "))
choice=int(input('''
choose a number for various operations
1  for sum
2  for sub  
3  for mul 
4  for div 
 '''))
if choice == 1:
    print(num1 + num2)
elif choice== 2:
    print(num1-num2)
elif choice ==3:
    print(num1*num2)
elif choice== 4:
    print(int(num1/num2))


    