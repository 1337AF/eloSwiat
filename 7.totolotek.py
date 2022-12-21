import random

list_of_all_numbers = []
for x in range(1, 50):
    list_of_all_numbers.append(x)
print(list_of_all_numbers)

six_winning_numbers = []
for i in range(6):
    winning_number = random.choice(list_of_all_numbers)
    list_of_all_numbers.remove(winning_number)
    six_winning_numbers.append(winning_number)
print(six_winning_numbers)

print("""
Put here your six chosen numbers.
*Positive Integers only,
*Range from 1:49,
*Unique number only each time!
*Spread the numbers with a simple space like this : "1 2 3 4 5 6"
""")

choice = None
while True:
    choice = input(f'> ').strip().split(' ')
    if len(choice) != 6:
        print("here you must put exactly 6 numbers!")
        continue
    else:
        break

chosen_numbers = [int(n) for n in choice]

good_choices = [x for x in chosen_numbers if x in six_winning_numbers]

print(f'You have {len(good_choices)} good choices and they are {good_choices}.')

