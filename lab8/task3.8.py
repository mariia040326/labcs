'''
Використовуючи підпрограму для знаходження n-тового числа Фібоначчі.
Обчислити значення виразу
'''
def number_fibonachi(n):
    number1 = 1
    number2 = 1
    i = 0
    while i < n - 2:
        number_sum = number1 + number2
        number1 = number2
        number2 = number_sum
        i = i + 1
    return number2
s=number_fibonachi(3)+number_fibonachi(8)
print(s)