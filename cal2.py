a = int(input("enter the no. a:"))
b = int(input("enter the no. b:"))
print("""1.summation.
2.subtraction.
3.multiplication.
4.division.
5.modulo""")
choice = int(input("enter your choice"))
while choice:
    if choice == 1:
        s = a + b
        print('sum is:')
        print(s)
        choice = int(input("enter your choice"))
    elif choice == 2:
        s1 = a - b
        print('sub is:')
        print(s1)
        choice = int(input("enter your choice"))
    elif choice == 3:
        m = a * b
        print('mul is:')  
        print(m)
        choice = int(input("enter your choice"))
    elif choice == 4:
        d = a / b
        print('div is:')
        print(d)
        choice = int(input("enter your choice"))
    elif choice == 5:
        m1 = a % b
        print('mod is:')
        print(m1)
        choice = int(input("enter your choice"))
    else:
        print('nothing')
        break
        


