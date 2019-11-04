import cProfile


def get_len(array: []) -> int:
    return len(array)


def get_sum(array: []) -> int:
    s: int = 0
    for i in array:
        s += i
    return s


def main():
    lst = [i for i in range(10000000)]
    a = get_len(lst)
    b = get_sum(lst)


cProfile.run('main()')
