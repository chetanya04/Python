def unit(n):
    n = n * 2.54
    return n
a = int(input("enter your length\n"))
b = int(input("enter your length\n"))
print(f"your length in cm is{unit(a)}")
print(f"your length in cm is{unit(b)}")