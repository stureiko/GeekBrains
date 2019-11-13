from collections import deque

if __name__ == '__main__':

    a = 42
    b = bin(a)
    c = oct(a)
    d = hex(a)
    print(f'a = {a}')
    print(f'b = {b}')
    print(f'c = {c}')
    print(f'd = {d}')
    print('*' * 50)

    print('Автоматом перевод и в разные системы счиления указать в int параметр base=')
    print(f"1453 по базе 10: {int('1453', base=10)}")
    print(f"1453 по базе 16: {int('1453', base=16)}")
    print(f"1453 по базе 32: {int('1453', base=32)}")

    print('*' * 50)
    print(f'Код символа "f": {ord("f")}')
    print(f'Код символа "л": {ord("л")}')
