import random

n = 3
k = int(input('введите k '))

#arr = [[random.randint(1,5) for j in range(n)] for i in range(n)]
with open("D:\КустовДанилАндреевич_УМ-222_vvod.txt", 'r') as f:
    arr = [[int(num) for num in line.split(',')] for line in f]
for i in range(n):
    print(arr[i])
for i in range(n):
   for j in range(n):
       if k-1 == i:
           arr[i][j] = arr[i][j] / arr[i][i]
print('новая матрица: ')

file = open("D:\КустовДанилАндреевич_УМ-222_vivod.txt", 'w')
for i in range(n):
    print(arr[i])
    l=str(arr[i])
    file.write(l)
file.close()