day=input("enter the day:-")
if day=="monday":
    print("ok")
    disco_per=input("take disco disco permission:-")
    if disco_per=="ok":
        print("imform the team member")
        team_member=input("take team member permission:-")
        if team_member=="yes":
          print("ok")
          place=input("enter the place:-")
          if place=="hospital":
            print("you can go")
            going_time=int(input("enter the going time:-"))
            if going_time==10:
              print("ok")
              coming_time=int(input("enter the coming time:-"))
              if coming_time==7:
                  print("yes")
                  prefertion=input("enter the prefertion:-")
                  if prefertion=="mask" and "sanitizer":
                    print("you can go")
                  else:
                    print("you cant go")
              else:
                print("no")
            else:
              print("not ok")
          else:
            print("you cant go")
        else:
          print("is not ok")
    else:
        print("dont ask")
else:
  print("invalid")
