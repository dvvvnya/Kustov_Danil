n = int(input('введите число: '))
for i in range(n) :
    if i != 0 or i%10 != 0 :
        for j in str(i):
            ji = int(j)
            if ji != 0 and ji != 1 and i % ji:
                break
        else:
            print(i) 
