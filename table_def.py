def table(a):
    for i in range(1,11):
        print(a, "*", i, " = ", a * i)
    return a
a = 2
n = 3
b = 4
print(table(a),table(n),table(b))
