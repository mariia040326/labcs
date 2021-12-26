a=[[3,5],
   [2,1]
]
z=1
x=1
for i in range(len(a)):
    for j in range(len(a[i])):
        if i==j:
            z*=a[i][j]
        else:
            x*=a[i][j]
n=z-x
print(n)

