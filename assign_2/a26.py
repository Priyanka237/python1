a = ["mercury","venus","earth","mars","jupiter","saturn","uranus","neptune"]
print(a)
b = input("enter planet name:")
if b in a[0:4]:
    print("enter planet is inner planet")
else:
    print("enter planet is outer planet")

