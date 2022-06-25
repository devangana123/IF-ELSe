name=input("enter the name:-")
basic=int(input("enter the salary:-"))
if basic<=10000:
    HRA=basic*20/100
    DA=basic*80/100
    gross=basic+HRA+DA
    print(gross,"gross salary")
elif basic<=20000:
    HRA=basic*25/100
    DA=basic*90/100
    gross=basic+HRA+DA
    print(gross,"gross salary")   
else:
    HRA=basic*30/100
    DA=basic*95/100
    gross=basic+HRA+DA
    print(gross,"gross salary")  