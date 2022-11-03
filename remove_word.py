def unit(string,word):
    a = string.replace(word,"")
    return a.split()
this = "    this is harry    "
a = unit(this,"harry")
print(a)