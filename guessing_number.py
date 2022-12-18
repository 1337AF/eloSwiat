#tu jest moja zgadywanka. Jest niezła chyba. Można było tu też napewno zastosować for loops

win_number = 10
guess_amount = 0
while guess_amount < 3:
    try:
        guess = int(input("input your number: "))
    except ValueError:
        print('Numbers only!!')
        continue
    if guess == win_number:
        print('Bravo')
        break
    elif guess != win_number:
        print('Wrong number')
    if guess_amount == 2:
        print(f'It was your {guess_amount + 1} try. I will help You a little')
    guess_amount = guess_amount + 1
while guess_amount >= 3:
    try:
        guess = int(input("input your number: "))
    except ValueError:
        print('Numbers only!!')
    if guess < win_number:
        print('Winning number is higher')
    elif guess > win_number:
        print('Winning number is lower')
    elif guess == win_number:
        print(f'Bravo! It was your {guess_amount} try!')
        quit()
    guess_amount = guess_amount + 1
    print (f'It was your {guess_amount} try')

