'''
Визначити суму від’ємних елементів матриці з обома парними індексами.
'''

a=[[3,5,-3],
   [-4,-2,4],
   [4,7,-2]
]
s=0
for i in range(0,len(a),2):
    for j in range(0,len(a[i]),2):
        if a[i][j]<=0:
            s+=a[i][j]


print(s)