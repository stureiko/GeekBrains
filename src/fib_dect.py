import cProfile


def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test for {i}: OK')


def fib_dect(n):
    fib_d = {0: 0, 1: 1}

    def _fib_dict(n):
        if n in fib_d:
            return fib_d[n]

        fib_d[n] = _fib_dict((n - 1)) + _fib_dict(n - 2)
        return fib_d[n]

    return _fib_dict(n)


cProfile.run('fib_dect(500)')

# 19/1    0.000    0.000    0.000    0.000 fib_dect.py:14(_fib_dict) 10
# 39/1    0.000    0.000    0.000    0.000 fib_dect.py:14(_fib_dict) 20
# 99/1    0.000    0.000    0.000    0.000 fib_dect.py:14(_fib_dict) 50
# 199/1    0.000    0.000    0.000    0.000 fib_dect.py:14(_fib_dict) 100
# 399/1    0.001    0.000    0.001    0.001 fib_dect.py:14(_fib_dict) 200
# 999/1    0.002    0.000    0.002    0.002 fib_dect.py:14(_fib_dict) 500


# test_fib(fib_dect)

# python -m timeit -n 1000 -s "import fib_dect" "fib_dect.fib_dect(500)"

# "fib_dect.fib_dect(10)"
# 1000 loops, best of 5: 5.74 usec per loop

# "fib_dect.fib_dect(15)"
# 1000 loops, best of 5: 8.72 usec per loop

# "fib_dect.fib_dect(20)"
# 1000 loops, best of 5: 11.5 usec per loop

# "fib_dect.fib_dect(100)"
# 1000 loops, best of 5: 58.3 usec per loop

# "fib_dect.fib_dect(200)"
# 1000 loops, best of 5: 115 usec per loop

# "fib_dect.fib_dect(500)"
# 1000 loops, best of 5: 346 usec per loop