import timeit

import fibonachi

res = fibonachi.fib(10)
print(res)

print(timeit.timeit('fibonachi.fib(10)'))
