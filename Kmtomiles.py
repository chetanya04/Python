speed = float(input("SPEED : "))
unit = input("(K)m or (M)iles")
if unit.upper()=="K":
    converted = speed*0.62
    print(f"your speed in miles{converted}")
else:
    converted = speed / 0.62
    print(f"Your speed in kilometer is {converted}")
