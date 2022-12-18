#tu wydaję się, że już nic nie ma do poprawy , zastosowałem tutaj obsługę błędu "valueError"

time_amount = None
while True:
    try:
        time_amount = float(input('What is the time amount we are talking about? '))
        break
    except ValueError:
        print('Numbers only!!')
while True:
    type = input('Is it (M)inutes or (H)ours? ')
    if type.upper() == 'M':
        print(f'It is {time_amount / 60} Hours')
        break
    elif type.upper() == 'H':
        print(f'It is {time_amount * 60} Minutes')
        break
    else:
        print('Choose only (M) or (H) !!')
