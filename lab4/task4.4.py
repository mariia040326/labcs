'''
Знайти значення y.
#0
a,b,c- сталі числа
d-кінцеве значення
'''
#1 введення даних
import math
a=int(input('A='))
c=int(input('C='))
n=int(input('N='))
#2порівняня
if a==c==n:
    d=math.cos(a+n+c)
    print('y={0:.2f}' .format(d))
elif a<c==n:
    d=math.cos(a*c*n)
    print('y={0:.2f}' .format(d))
elif a<c<n:
    d=math.cos((a+c)*n)
    print('y={0:.2f}' .format(d))
else:
    print('y=0')
