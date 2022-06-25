per=int(input("enter the marks"))
if per>=90:
    print("a grade")
elif per>=80 and per<=90:
    print("b grade")
elif per>=60 and per<=80:
    print("c grade")
elif per<=60 and per>=35:
    print("d grade")
else:
    print("fail")




pr=int(input("enter the number"))
if pr<=75:
    print("not allowe to sit in exam")
else:
    print("allowed to sit in exam")