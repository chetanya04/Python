a = int(input("enter you english marks\n"))
b = int(input("enter your maths marks\n"))
c = int(input("enter your science marks\n"))
sum = (a+b+c)/3
if sum > 90:
    print("GRADE : EX")
elif sum > 80:
    print("GRADE : A")
elif sum > 70:
    print("GRADE : B")
elif sum >60:
    print("GRADE : C")
else:
    print("fail")