commands = ['ADD', 'SUB', 'MULT', 'DIV', 'OFF']
inputPrompt = 'Choose Calculation type: "ADD", "SUB", "MULT", "DIV" To quit the Calculator type "OFF" \n'
askForCommand = True
command = None

while True:
    if askForCommand:
        command = input(inputPrompt).upper().strip()
        if command not in commands:
            print('Wrong input guy!')
            continue
        if command == 'OFF':
            print("bye bye")
            quit()  # albo break

    try:
        number1 = float(input('Put the first number '))
        number2 = float(input('Put the second number '))
        if command == 'ADD':
            print(number1 + number2)
        elif command == "SUB":
            print(number1 - number2)
        elif command == "MULT":
            print(number1 * number2)
        elif command == "DIV":
            print(number1 / number2)
        askForCommand = True
    except ValueError:
        print('Numbers only!!')
        askForCommand = False
    except ZeroDivisionError:
        print('division by zero is a sin you know')
        askForCommand = False