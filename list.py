number = [2,2,6,5,7,3,3]
unique = []
for i in number:
    if i not in unique:
        unique.append(i)
print(unique)