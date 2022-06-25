sweet=int(input("enter the numbet"))
if sweet%3==0 and sweet%7==0:
    print("chocolate")
elif sweet%3==0:
    print("choco")
elif sweet%7==0:
    print("late")
else:
    print("none")