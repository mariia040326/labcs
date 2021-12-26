'''
Перевірити справедливість рівності при заданій точності e :
'''
import math
e=10
x=3
s=0
for i in range(e+1):
    a = (1 / 2 * i - 1) * math.pow(((x - 1) / (x + 1)), (2 * i - 1))
    s+=a
print(s+2)
if math.log1p(x)==(s+2):
    print('рівність виконується')
else:
    print('рівність не виконується')
