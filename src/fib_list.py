import cProfile



def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test for {i}: OK')


def fib_list(n):
    fib_l = [None] * 1000
    fib_l[:2] = [0, 1]

    def _fib_list(n):
        if fib_l[n] is None:
            fib_l[n] = _fib_list((n - 1)) + _fib_list(n - 2)
        return fib_l[n]

    return _fib_list(n)


cProfile.run('fib_list(20)')

# 19/1    0.000    0.000    0.000    0.000 fib_list.py:15(_fib_list) 10
# 39/1    0.000    0.000    0.000    0.000 fib_list.py:15(_fib_list) 20
# 99/1    0.000    0.000    0.000    0.000 fib_list.py:14(_fib_list) 50
# 199/1    0.000    0.000    0.000    0.000 fib_list.py:14(_fib_list) 100
# 399/1    0.001    0.000    0.001    0.001 fib_list.py:14(_fib_list) 200
# 999/1    0.002    0.000    0.002    0.002 fib_list.py:14(_fib_list) 500


# test_fib(fib_list)

# python -m timeit -n 1000 -s "import fib_list"

# "fib_list.fib_list(10)"
# 1000 loops, best of 5: 8.05 usec per loop

# "fib_list.fib_list(15)"
# 1000 loops, best of 5: 9.4 usec per loop

# "fib_list.fib_list(20)"
# 1000 loops, best of 5: 13.8 usec per loop

# "fib_list.fib_list(100)"
# 1000 loops, best of 5: 56.4 usec per loop

# "fib_list.fib_list(200)"
# 1000 loops, best of 5: 114 usec per loop

# "fib_list.fib_list(500)"
# 1000 loops, best of 5: 313 usec per loop
