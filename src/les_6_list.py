import sys


def show_size(x, level=0):
    print('\t' * level, f'type= {x.__class__}, size= {sys.getsizeof(x)}, object= {x}')

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                show_size(xx, level + 1)
        elif not isinstance(x, str):
            for xx in x:
                show_size(xx, level + 1)


if __name__ == "__main__":

    lst = []
    lst.append(1)
    lst.extend([2, 3, 4])
#    print(lst)

    print(f'Версия Python: {sys.version},\nВерсия OS: {sys.platform}')

    a = 5
    b = 12.5
    c = 'Hello moo'

    print(sys.getsizeof(a))
    print(sys.getsizeof(b))
    print(sys.getsizeof(c))

    lst = [i for i in range(10)]
    print(sys.getsizeof(lst))
    print(lst)

    show_size(a)
    show_size(b)
    show_size(c)
    show_size(lst)

    print('*' * 50)

    t = tuple(lst)
    show_size(t)

    print('*' * 50)

    s = set(lst)
    show_size(s)

    print('*' * 50)
    d = {str(i): i for i in range(10)}
    show_size(d)

