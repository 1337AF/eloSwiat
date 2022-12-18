#mój kalkulator, zaletą kodu tutaj jest to że się do dobrze czyta. Ale jak mi Arek zasugerował: "O raju, inwazja while True:

number1 = None
number2 = None
commands = ['ADD', 'SUB', 'MULT', 'DIV', 'OFF']
while True:
    while True:
        command = input("""
Choose Calculation type: "ADD", "SUB", "MULT", "DIV"
To quit the Calculator type "OFF"
> """).upper()
        if command in commands:
            if command == 'OFF':
                print("bye bye")
                quit()
            else:
                break
        else:
            print('Wrong input guy!')
            continue
    while True:
        try:
            number1 = float(input('Put the first number '))
            number2 = float(input('Put the second number '))
            break
        except ValueError:
            print('Numbers only!!')
    while True:
        if command == 'ADD':
            print(number1 + number2)
        elif command == "SUB":
            print(number1 - number2)
        elif command == "MULT":
            print(number1 * number2)
        elif command == "DIV":
            if number2 == 0:
                print('division by zero is a sin you know')
            else:
                print(number1 / number2)
        break
