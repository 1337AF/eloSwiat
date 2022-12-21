# Tutaj sposób jak wydrukować zobie "E" bez mnożenia stringu ( z neta)

numbers = [5, 1, 5, 1, 5]
for x in numbers:
    output = ''
    for y in range(x):
        output += '*'
    print(output)