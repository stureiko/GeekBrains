"""
9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
"""


def sum_num(n: int) -> int:
    res: int = 0
    while n > 0:
        res += n % 10
        n //= 10
    return res


res: int = 0
res_num: int = 0

while True:
    num = input('Введите число, для завершения введите любой символ кроме числа: ')
    if num.isdigit():
        num = int(num)
        if res < sum_num(num):
            res = sum_num(num)
            res_num = num
    else:
        print(f'Число = {res_num}, сумма его цифр = {res}')
        break
