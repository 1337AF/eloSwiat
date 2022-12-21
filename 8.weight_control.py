dd = [
    [(1, 66), (3, 67), (15, 69)],  # 1
    [(3, 56), (4, 55), (20, 55)],  # 2
    [],                # 3
    [],                # 4
    [],                # 5
    [],                # 6
    [],                # 7
    [],                # 8
    [],                # 9
    [],                # 10
    [(4, 100), (19, 105), (25, 103)],   # 11
    [],                # 12
]
program_is_on = True
while program_is_on:
    weight = int(input('Enter your weight in KGs> '))
    day = int(input('What the day today? (number of the day in this month> '))
    month = int(input('What the number of the month?> ')) - 1

    list_of_days_and_weight = dd[month]
    list_of_days_and_weight.append((day, weight))
    for row in dd:
        print(row)
    stats = input('Whould You like to see some stats? Type "yes" or "no"> ')
    if stats == "yes":
        print(f"""
January. Average weight: {}, Lowest: {}, Highest: {} 
February. Average weight: {}, Lowest: {}, Highest: {}         
March. Average weight: {}, Lowest: {}, Highest: {} 
April. Average weight: {}, Lowest: {}, Highest: {} 
May. Average weight: {}, Lowest: {}, Highest: {} 
June. Average weight: {}, Lowest: {}, Highest: {} 
July. Average weight: {}, Lowest: {}, Highest: {} 
August. Average weight: {}, Lowest: {}, Highest: {}
September. Average weight: {}, Lowest: {}, Highest: {}
October. Average weight: {}, Lowest: {}, Highest: {}
November. Average weight: {}, Lowest: {}, Highest: {}
December. Average weight: {}, Lowest: {}, Highest: {}
    """)
    if stats == "no":
        continue


