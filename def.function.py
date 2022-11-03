def percentage(name):
    p = ((name[0]+name[1]+name[2]+name[3])/4)
    return p
name = [58,47,78,84]
percentage1 = percentage(name)
name2 = [84,45,69,78]
percentage2 = percentage(name2)
name3 = [47,58,98,78]
percentage3 = percentage(name3)
print(percentage1,percentage2,percentage3)