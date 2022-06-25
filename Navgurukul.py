
print("wellcome to navgurukul")
covid=input("do you have covid test:-")
if covid=="yes":
    state=input("enter the state:-")
    if state=="maharashtra":
        print("you have to 7 days quaratine")
    else:
        print("you have to 14 days quarantine")
elif covid=="no":
    print("you have to go hospital")
    report=input("do you have report:-")
    if report=="yes":
        resul=input("your report is possitive or negative:-")
        if report=="possitive":
            print("you have addmit")
        elif report=="negative":
            print("wellcome to navgurukul")
        else:
            print("go back to home")
    else:
        print("error")
else:
    print("invalid")