'''x=input('x=')
y=input('y=')
n=10
a=[]
for i in range(1,n+1):
    a=[]
    # el[3]==y
    el=(i-2)+((i-1)/2**(i-1))*(i-3)
    a.append(el)
    el[3]=y
print(a)'''
a=[
    [2,9,4,5],
    [4,6,1,2],
    [4,0,1,4],
    [1,0,3,7]
]
d=1
for i in range(0,len(a),2):
    a[i].sort()


print(*a, sep = "\n")