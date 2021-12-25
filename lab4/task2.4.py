'''
Дано два дійсних числа:a,b. З’ясувати, чи належать ці числа інтервалу [1,2]∪(3,7)
'''

number1=float(input('a='))
number2=float(input('b='))
if 2>=number1>=1 or 7>number1>3:
    print('a-належить інтервалу')
else:
    print('Число а-не належить інтервалу')
if 2>=number2>=1 or 7>number2>3:
    print('b-належить інтервалу')
else:
    print('Число b-не належать інтервалу')

