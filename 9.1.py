import random

n = 3
with open("D:\КустовДанилАндреевич_УМ-222_vvod.txt", 'r') as f:
    arr = [[int(num) for num in line.split(',')] for line in f]
for i in range(n):
    print(arr[i])
trans=[[0 for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        trans[j][i]=arr[i][j]
print('транспонированная матрица:')
file = open("D:\КустовДанилАндреевич_УМ-222_vivod.txt", 'w')
for i in range(n):
    print(trans[i])
    l=str(trans[i])
    file.write(l)
file.close()