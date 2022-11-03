mydict = {
    "pankhan" : "fan",
    "dabba" : "box",
    "cheez" : "item"
}
print("select the words which you want to translate : ",mydict.keys())
a = input("enter the words which yu want to translate")
print("the meaning of this words is: ",mydict.get(a))