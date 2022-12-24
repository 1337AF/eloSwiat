list2D = [
    [66, 0, 0, 0, 0, 67, 0, 0, 0, 0, 67, 0, 0, 0, 0, 67, 0, 68, 0, 0, 0, 69, 0, 0, 0, 0, 69, 0, 0, 0, 69.3],  # 1
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 70, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 2
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 3
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 55, 0, 0, 0, 0, 0, 81, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 4
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 5
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 6
    [0, 0, 0, 0, 70, 0, 0, 0, 0, 60, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 7
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 8
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 9
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 10
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 11
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 67, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 12
]


def stats(x):
    positive_list2D = []
    for y in list2D[x]:
        if y > 0:
            positive_list2D.append(y)
    return positive_list2D


def stats2():
    all_positive_list2D = []
    for x in range(12):
        for y in list2D[x]:
            if y > 0:
                all_positive_list2D.append(y)
    return all_positive_list2D


commands = ['INPUT', 'STATS', 'OFF']
inputPrompt = """
This program keeps your data about your weight.
For input type "INPUT"
For statistics type "STATS"
To quit type "OFF"
> """
command = None
program_is_on = True
while program_is_on:
    while True:
        command = input(inputPrompt).upper().strip()
        if command in commands:
            if command == 'OFF':
                print("bye bye")
                quit()
            elif command == 'INPUT':
                break
            elif command == 'STATS':
                for x in range(12):
                    try:
                        print(f'Month {x+1}. Average weight: {sum(list2D[x]) / len(stats(x))}, Lowest: {min(stats(x))}, Highest: {max(list2D[x])}')
                    except ZeroDivisionError:
                        print(f'No data for {x+1} Month')
                try:
                    print(f'Whole year view. Average weight: {sum(stats2()) / len(stats2())}, Lowest: {min(stats2())}, Highest: {max(stats2())}')
                except ZeroDivisionError:
                    print(f'No data for whole year.')
        else:
            print('Wrong input guy!')
            continue
    while True:
        try:
            weight = float(input('Enter your weight in KGs> '))
            day = int(input('What the day today? (number of the day in this month> '))
            month = int(input('What the number of the month?> ')) - 1
            list2D[month][day] = weight
            break
        except ValueError:
            print('Numbers only!!')
