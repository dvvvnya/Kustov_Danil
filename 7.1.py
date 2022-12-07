def zam(x) :
    tmp=x[0]
    x[0]=x[len(x)-1]
    x[len(x)-1]=tmp
a=[]
m=int(input('введите длину массива: '))
for i in range(m): 
    print('введите ', i, 'элемент массива: ')
    a.append(int(input()))
print(a)
zam(a)
print(a)