num1=int(input("enter the number"))
num2=int(input("enter the number"))
symbol=input("enter the symbol")
if symbol=="+":
    print(num1+num2)
elif symbol=="-":
    print(num1-num2)
elif symbol=="*":
    print(num1*num2)
elif symbol=="**":
    print(num1**num2)
elif symbol=="/":
    print(num1/num2)
elif symbol=="//":
    print(num1//num2)
elif symbol=="%":
    print(num1%num2)
else:
    print("error")
