name = input("enter your name")
if len(name) < 3:
    print(f"{'ERROR'} the name should be more than 3 character")
elif len(name) > 50:
    print(f"{'ERROR'} the name should be less than 50 character")
else:
    print("its a lovely name")