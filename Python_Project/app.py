command=""
while command.lower()!="quit":
    command=input(">").lower()
    if command=="start":
        print("car started.")
    elif command=="stop":
        print("car stopped")
    elif command=="help":
        print("""
        start:to start car
        stop:to stop car
        quit:to quit system
        """)
    elif command=="quit":
        break
    else:
        print("can't understand command")