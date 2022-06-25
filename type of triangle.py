a=int(input("enter the length of triangle:-"))
b=int(input("enter the length of triangle:-"))
c=int(input("enter the length of triangle:-"))
if a==b==c:
    print("equilateral triangle")
elif a==b or b==c or c==a:
    print("isoceles triangle")
else:
    print("scalen")