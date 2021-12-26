'''
Використовуючи підпрограму для знаходження скалярного добутку, обчислити
значення виразу s=2<a,b>-3<a,c>, де a,b,c e R , <x,y> – скалярний добуток
векторів.
'''
def scal_dob(a=0,b=0,):
    x=a*b
    return x
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))

s=2*scal_dob(a,b)-3*scal_dob(a,c)
print(s)