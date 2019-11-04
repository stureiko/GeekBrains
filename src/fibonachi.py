import cProfile
import timeit

# def test_fib(func):
#     lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
#     for i, item in enumerate(lst):
#         assert item == func(i)
#         print(f'Test for {i}: OK')


def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

if __name__ == '__main__':
    cProfile.run('fib(10)')

# python -m timeit -n 1000 -s "import fibonachi" "fibonachi.fib(15)"

# "fibonachi.fib(10)"
# 1000 loops, best of 5: 32.4 usec per loop

# "fibonachi.fib(15)"
# 1000 loops, best of 5: 364 usec per loop

# "fibonachi.fib(20)"
# 1000 loops, best of 5: 4.05 msec per loop

#