English = int(input("enter your marks"))
Maths = int(input("enter your marks"))
Sst = int(input("enter your marks"))
sum = English+Maths+Sst
Percentage = sum%3!=0
if Percentage >=80:
    print("Congo You Got Science stream")
elif Percentage>=70:
    print("Congo You Got science STream")
else:
    print("COngo You got humanaties Stream")