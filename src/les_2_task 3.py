"""
Рекурсия
"""


def func(a: int, b: int) -> str:
    if a == b:
        return f'{a}'
    elif a > b:
        return f'{a}, {func(a-1, b)}'
    else:
        return f'{a}, {func(a+1, b)}'


if __name__ == '__main__':
    print(func(1, 10))
