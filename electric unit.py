units=int(input("entre the n0.units consumed:-"))
if units<50:
    ammount=units*2.60+25
    surcharge=25
    print(ammount)
elif units<=100:
    ammount=130+(units-50)*3.25
    surcharge=35
    print(ammount)
elif units<=200:
    ammount=130+162.50+(units-100)*5.26
    surcharge=45
    print(ammount)
else:
    ammount=130+162.50+5.26+(units-200)*8.45
    print(ammount)


