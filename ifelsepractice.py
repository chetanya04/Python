name = ["rohan","shubham","chetanya","soniya"]
name1 = input("enter the name: ")
if name1 in name:
    print(f"it is already present in name.... "
          f"and the list\n {name}")
else:
    name.append(name1)
    print(f"thanx for let us know {name}")