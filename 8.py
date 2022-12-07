import random

n = int(input('введите порядок матрицы '))
k = int(input('введите k '))

arr = [[random.randint(1,5) for j in range(n)] for i in range(n)]
for i in range(n):
    print(arr[i])
for i in range(n):
   for j in range(n):
       if k-1 == i:
           arr[i][j] = arr[i][j] / arr[i][i]
print('новая матрица: ')
for i in range(n):
    print(arr[i])