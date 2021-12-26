'''
Побудувати матрицю А, елементи якої задаються формулою:
Побудувати одновимірний масив (переписати матрицю в одновимірний масив).
'''
from math import *
a=[]
n=int(input('n='))
m=int(input('m='))
s=0
for i in range(n):
    row=[]
    for j in range(m):
        if (i*j)//2==0:
            row.append(factorial(j))
        else:
            s+=i
            row.append(s)
    a.append(row)

print(*a, sep = "\n")