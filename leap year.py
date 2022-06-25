

year=int(input("enter the year: "))
if year%100==0:
    if year%400==0:
        print("century year")
    else:
        print("is not century year")
else:
    if year%4==0:
        print("leap year")
    else:
        print("is not leap year")