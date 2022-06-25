from re import A


sub1=int(input("enter the marks of 1st subject:-"))
sub2=int(input("enter the marks of 1st subject:-"))
sub3=int(input("enter the marks of 1st subject:-"))
sub4=int(input("enter the marks of 1st subject:-"))
sub5=int(input("enter the marks of 1st subject:-"))
avg=(sub1+sub2+sub3+sub4+sub5)/5
if avg>=90:
    print("grade:-A",avg)
elif avg>=80 and avg<90:
    print("grade:-B",avg)
elif avg>=70 and avg<80:
    print("grade:-c",avg)
elif avg>=60 and avg<70:
    print("grade:-D",avg)
else:
    print("grade:-F",avg)
