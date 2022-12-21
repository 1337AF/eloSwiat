#Uszczeloniony zwracacz liczb parzystych
while True:
       try:
              y = int(input("input your number: "))
              break
       except ValueError:
               print('Numbers only!!')
print(f'You have {y//2} even numbers within your number')
for x in range(2, y+1, 2):
       print(x, end=" ")




