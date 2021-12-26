'''
Дано дійсне число а. Обчислити a(a+1)...(a+n-1)
'''
a=2
n=3
dob=1
for i in range(n+1):
    c=a+i-1
    dob*=c
print(dob)