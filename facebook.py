email=input("enter your email or phone number:-")
if email>="a" and email<="z":
    password=int(input("enter the password:-"))
    if password>=0:
        username=input("enter the user name:-")
        if username>="a" and username<="z":
            date=int(input("enter your birth date:-"))
            if date>=1 and date<=100:
                month=int(input("enter the birth  month"))
                if month>0 and month<=12:
                    year=int(input("enter the birth year"))
                    if year>0:
                        gender=input("enter your birth gender:-")
                        if gender=="female" or "male":
                           language=input("enter the language:-")
                           if language=="english" or "hindi" or "marathi":
                               login=input("do you want to log in:-")
                               if login=="yes":
                                    print("your facebook account is successfuly created, thank you")
                               else:
                                    print("invalid")
                           else:
                               print("error")

                        else:
                            print("unsuccessful")
                    else:
                        print("not done")
                else:
                    print("jyoti")
            else:
                print("stop")
        else:
            print("not ok")
    else:
        print("forget password")
else:
    print("incorrect email")