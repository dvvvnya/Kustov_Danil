import random

n=int(input('введите длину списка: '))
l=[random.randint(0,5) for i in range(n)]
print(l)
sr = sum(l)/n
for i in range(n) :
    if l[i] == 0 :
        l[i] = sr
print('получили: ', l)