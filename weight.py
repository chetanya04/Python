weight = float(input("enter your weight---"))
unit = input('(L)bs or (K)g')
if unit.upper()== "L":
    weight = weight * 0.45
    print(f"your weight in kg{weight}")
elif unit.upper()== "K":
    weight = weight / 0.45
    print(f"your weight in lbs{weight}")