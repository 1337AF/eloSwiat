lista = [7, 5, 3, 67, 0, 4, 12, 0]
count_loops = 0

for i in range(len(lista)):
     for j in range(len(lista) - 1 - i):
          print(count_loops)
          count_loops += 1
          if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
print(lista)