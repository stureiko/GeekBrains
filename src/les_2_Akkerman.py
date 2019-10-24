def akker(m: int, n: int)->int:
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return akker(m - 1, 1)
    return akker(m - 1, akker(m, n - 1))


if __name__ == '__main__':
    print(akker(1, 1))
    print(akker(2, 4))
    print(akker(3, 4))
