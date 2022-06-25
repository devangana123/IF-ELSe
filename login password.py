
username=input("enter the name:-")
password=int(input("enter the password:-"))
if username>="a" and username<="z":
   if password>=0:
         print("your login is succesfully")
   else:
       print("incorrect password")
elif username!="divya" and password!=19:
         print("both condition are wrong")
         print("create new account") 
         username1=input("enter the name")  
         password1=int(input("enter the password"))
         print("your new accout is successfullu created")
else:
    print("incorrect user name")
