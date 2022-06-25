age=int(input("enter the age:-"))
if age>=18:
    var=input("go to collage or not:-")
    if var=="yes":
        collage=input("which collage:-")
        field=input("which field:-")
        if field=="science":
            print("2 year after get job")
        elif field=="art":
            print("after 3 years get job")
        elif field=="math":
            print("1.50 year after get job ")
    elif var=="no":
        marrege=input("are you married:-")
        if marrege=="yes":
            type=input("which type of marrage:-")
            if type=="love marrage":
                place=input("which place:-")
                if place=="temple":
                    print("god bless you")
                elif place=="court":
                    print("friend circle")
            elif type=="arreng marrage":
                 print("happy ending")
        elif marrege=="no":
            print("enjoy your self")
elif age<=18:
    var1=input("are you go to school or not:-")
    age2=int(input("enter thr age"))
    if var1=="yes":
        if age2>10:
            subject=input("enter the subject:-")
            if subject=="science" or "math" or "art":
               print("its nice field")
        elif age2<10:
            print("good")
    elif var1=="no":
        print("do your study")
else:
    print("invalid")
