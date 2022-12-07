import random

n = int(input('введите порядок матрицы '))
arr = [[random.randint(1,5) for j in range(n)] for i in range(n)]
for i in range(n):
    print(arr[i])

trans=[[0 for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        trans[j][i]=arr[i][j]
print('транспонированная матрица:')
for i in range(n):
    print(trans[i])