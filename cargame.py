command = ""
started = False

while True:
    command = input(">").lower()
    if command=="start":
        if started:
            print("!!!BUT ITS ALREADY STARTED!!!")
        else:
            started = True
            print("!!!CAR STARTED!!!")
    elif command=="stop":
        if not started:
            print('!!!CAR ALREADY STOPPED!!!')
        else:
            started = False
            print("!!!CAR STOPPED!!!")
    elif command=="help":
        print("""
START--- TO START A CAR
STOP---  TO STOP A CAR
QUIT---  TO QUIT THE GAME
""")
    elif command=="quit":
        break
    else:
        print("SORRY BUT I DONT UNDERSTAND")