speed = int(input("speed: "))
unit = input("(K)m or (M)iles")
if unit.upper()=="K":
    converted = speed*0.621371
    print(f"your speed in miles is: {converted}")
else:
    converted = speed*1.6
    print(f"your speed in kilometer is: {converted}")