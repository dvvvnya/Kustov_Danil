import math
x=int(input("Vvedite x: "))
t=int(input("Vvedite t: "))
z=((9*math.pi*t+10*math.cos(x))/(math.sqrt(t)-math.fabs(math.sin(t))))*math.pow(math.e,x)
print('z = ', z)
