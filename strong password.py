letter=input("enter the  letter:-")
if letter>="A" or letter<="Z":
    special_char=input("enter the special character:-")
    if special_char=="@"or "$" or "#":
        numeric=int(input("enter the number:-"))
        if numeric>=1:
            print(letter+special_char+str(numeric))
        else:
            print("invalid")
    else:
        print("it is not special character")
else:
    print("it is not letter")