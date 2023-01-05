command = input(">").lower()
while command != 'quit':
    if command == 'start':
        print("Car Started")
        break
    elif command == 'stop':
        print("Car Stopped")
        break
    elif command == 'help':
        print('''
            help : 
            start - to start the car
            stop - to stop the car
            quit - to quit
            ''')
        command = input(">").lower()

    else:
        print('''
        I Don't Understand your command
        Please opt from below ones
        Thanks for co-operation in advance:
        -----------------------------------
        -----------------------------------
        start - to start the car
        stop - to stop the car
        help - to get help in commands
        quit - to quit
            ''')
        command = input(">").lower()


else:
    print("Quit")
