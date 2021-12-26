'''
За даними дійсними числами а і b обчислити.
u=f(a,b)+f(2,a)
'''
from math import sqrt
def f(x,y):
    if x>y:
        f=x**3+sqrt(x**2+y**4)
        return f
    else:
        f=(x**2-2*x+sqrt(x))//x**(3/5)
        return f
a=int(input('a='))
b=int(input('b='))

u=f(a,b)+f(a,2)+2
print('u={0:0f}'.format(u))