import random


def gamewin(comp,you):
    if comp == yo
        return None
    elif comp == "s":
        if you=="w":
           return False
        elif you == "g":
            return True
    elif comp == "w":
        if you=="s":
            return True
        elif you=="g":
            return False
    elif comp == "g":
        if you=="s":
            return False
        elif you=="w":
            return True
print("Comp turn : Snake(s), Water(w), Gun(g)")
randno = random.randint(1,3)
if randno == 1:
    comp = "s"
elif randno == 2:
    comp = "w"
elif randno == 3:
    comp = "g"


you = input("Your turn : Snake(s), Water(w), Gun(g)")

print(f"comp turn {comp}")
print(f"your turn {you}")
a = gamewin(comp, you)
if a == None:
    print("THIS IS TIE")
elif a:
    print("YOU WIN")

else:
    print("YOU LOSE")

