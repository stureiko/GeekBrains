import cProfile


def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test for {i}: OK')


def fib_loop(n):
    if n < 2:
        return n

    first, second = 0, 1

    for i in range(2, n + 1):
        first, second = second, first + second

    return second


cProfile.run('fib_loop(1000)')

# test_fib(fib_for)

# "fib_loop.fib_loop(10)"
# 1000 loops, best of 5: 1.2 usec per loop

# "fib_loop.fib_loop(20)"
# 1000 loops, best of 5: 1.98 usec per loop

# "fib_loop.fib_loop(100)"
# 1000 loops, best of 5: 8.48 usec per loop

# "fib_loop.fib_loop(200)"
# 1000 loops, best of 5: 17.2 usec per loop

# "fib_loop.fib_loop(500)"
# 1000 loops, best of 5: 50.3 usec per loop

# "fib_loop.fib_loop(1000)"
# 1000 loops, best of 5: 112 usec per loop