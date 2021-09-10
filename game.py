def showMenu():
    print(" ---- Welcome to the Rocket Game ----- ")
    print()
    
    while True:
        command = input("Press [s] to Start or [e] to exit ")

        if (command == 's' or command == 'e' or command == 'S' or command == 'E'):
            break
        else:
            print("Invalid input. Try again.")
    
    return command

def isInteger(str):
    try:
        num = int(str)
    except ValueError:
        return False
    
    return True

def getInput(prompt):
    while True:
        inputString = input(prompt)

        if (isInteger(inputString)):
            inputInt = int(inputString)

            if (inputInt >= 6 and inputInt <= 100):
                return inputInt
        
        print("Invalid input.")

def newGame():
    command = showMenu()
    
    # Exit Game
    if (command == 'E' or command == 'e'):
        return

    # Starting Game!
    sideDice = getInput("How many sides do you want on your dice? Between 6 and 100, inclusive. ")
    numSegments = getInput("How many segments do you want your rockets to have? ")

    print(sideDice)
    print(numSegments)

newGame()
