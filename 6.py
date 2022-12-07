import random

n=int(input('введите длину списка: '))
l=[random.randint(1,5) for i in range(n)]
print(l)
sum = 0
pro = 1
for i in range(n) :
    sum += l[i]
    pro *= l[i]

print ("сумма элементов равна: ", sum)
print ("произведение элементов равно: ", pro)