print("""1.not
	2.and
	3.or
	4.nand
	5.nor""")
p = bool(int(input("enter p:")))
q = bool(int(input("enter q:")))
ch = int(input("enter choice"))
while 1<=ch<=5:
	if ch == 1:
		print("ans is:",not p)
		print("ans is:",not q)
		break
	elif ch == 2:
		print("ans is:",p and q)
		break
	elif ch == 3:
	    print("ans is:",p or q)
	    break
	elif ch == 4:
	    print("ans is:",not(p and q))
	    break
	elif ch == 5:
	    print("ans is:",not(p or q))
	    break
	else:
	 	print("invalid choice")
	 	break
	             	