def gcd(m: int, n: int)->int:
    while m != n:
        if m > n:
            m -= n
        else:
            n -= m
    return m


def gdc_div_rek(m: int, n: int)-> int:
    if n == 0:
        return m
    gdc_div_rek(n, m % n)


def gdc_div(m: int, n: int) -> int:
    while n != 0:
        m, n = n, m % n
    return m

