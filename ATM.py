
print("welcome to state bank of india,swipe you card:-")
card=input("enter your card")
if card=="atm":
    print("in process")
    language=input("enter the language:-")
    if language=="english":
        print("in process")
        pin=int(input("enter your pin:-"))
        if pin==1995:
            print("in process")
            type=(input("enter the type:-"))
            if type=="current account" or "saving account":
                print("loading")
                trans=input("enter the transection:-")
                if trans=="withdrawal":                                         
                    print("pleas wait.")                                               
                    balance=int(input("enter your balance:-"))
                    if balance>=0 and balance<=10000:   
                        print("you can take money.")
                        total_amount=int(input("enter you totalamount:-"))
                        if total_amount==20000:
                            print(total_amount-balance)
                            receipt=input("did you collect your cash:-")
                            if receipt==("yes"):
                                print("taka a printed receipt,if needed")
                                print("ok your withdrawal successful thank you so much")
                            else:
                                print("invalid")
                        else:
                            print("no")     
                    else:
                        print("you cant take money")  
                else:
                    print("incorrect process") 
            else:
                print("not answered")  
        else:
            print("out process") 
    else:
        print("no response")                                     
else:
    print("out process")   