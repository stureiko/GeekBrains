"""
Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
которые не меньше медианы, в другой — не больше медианы.
"""

"""
Алгоритм нахождения медианы
Выберем индекс списка. Способ выбора не важен, на практике вполне подходит и случайный. 
Элемент с этим индексом называется опорным элементом (pivot).
Разделим список на две группы:
Элементы меньше или равные pivot, lows
Элементы строго большие, чем pivot, highs
Мы знаем, что одна из этих групп содержит медиану. Предположим, что мы ищем k-тый элемент:
Если в lows есть k или больше элементов, рекурсивно обходим список lows в поисках k-того элемента.
Если в lows меньше, чем k элементтов, рекурсивно обходим список highs. 
Вместо поиска k мы ищем k-len(lows)

Засада снижения скорости кроется в алгоритме для подбора опорных элементов pivot
Привожу выбор за линейное время pivot, 
который в худшем случае удаляет достаточное количество элементов для обеспечения скорости O(n) 
при использовании его вместе с quicks_elect. 
Этот алгоритм был разработан в 1973 году Блумом (Blum), Флойдом (Floyd), Праттом (Pratt), 
Ривестом (Rivest) и Тарьяном (Tarjan)
"""

import random
import statistics

size = 50
width = size * 10
array = [random.randint(0, width) for i in range(2 * size + 1)]


def sort_bubble(array: list):
    """
    Сортировка пузырьком
    :param array: массив данных
    :return: работаем с самим массивом
    """
    n = 1
    while n < len(array):
        for i in range(len(array) - n):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1


def nlogn_median(array):
    """
    Простейшая медиана - сортируем массив и берем середину
    """
    sort_bubble(array)
    if len(array) % 2 == 1:
        return array[len(array) // 2]
    else:
        return 0.5 * (array[len(array) // 2 - 1] + array[len(array) // 2])


def chunked(array, chunk_size):
    """
    Разделяем массив array на фрагменты размера chunk_size
    :param array: массив данных для разделения
    :param chunk_size: размер фрагмента
    :return: список массивов
    """
    return [array[i: i + chunk_size] for i in range(0, len(array), chunk_size)]


def pivot_func(array: list) -> int:
    """
    Выбираем хорошй pivot в списке чисел l
    Этот алгоритм выполняется за время O(n)
    :param array: массив данных для выбора
    :return: int - pivot - опорный элемент
    """

    if len(array) < 5:
        """
        сортировка пузырьком массива из 5-и элементов или менее - считаем время постоянным
        """
        return nlogn_median(array)

    # разделим array на группы по 5 элементов
    chunks = chunked(array, 5)

    # Для простоты мы можем отбросить все группы, которые не являются полными
    full_chunks = [chunk for chunk in chunks if len(chunk) == 5]

    # атем мы сортируем каждый фрагмент. Каждая группа имеет фиксированную длину,
    # поэтому каждая сортировка занимает постоянное время
    sorted_groups = [sorted(chunk) for chunk in full_chunks]

    # Медиана каждого фрагмента имеет индекс 2
    medians = [chunk[2] for chunk in sorted_groups]

    median_of_medians = quick_median(medians, pivot_func)
    return median_of_medians


def quick_median(array: list, pivot_fn) -> float:
    """
    Функция Вычисление медианы
    :param array: массив данных
    :param pivot_fn: функция выбора опорного элемента
    """
    if len(array) % 2 == 1:
        return quick_select(array, len(array) / 2, pivot_fn)
    else:
        return 0.5 * (quick_select(array, len(array) / 2 - 1, pivot_fn) +
                      quick_select(array, len(array) / 2, pivot_fn))


def quick_select(array: list, k, pivot_fn) -> int:
    """
    Функция выбора k-го элемента в списке array (с нулевой базой)
    :param array: исходный массив данных
    :param k: индекс
    :param pivot_fn: функция выбора опорного элемента
    :return: k-ое значение
    """
    if len(array) == 1:
        # assert k == 0
        return array[0]

    pivot = pivot_fn(array)

    lows = [item for item in array if item < pivot]
    highs = [item for item in array if item > pivot]
    pivots = [item for item in array if item == pivot]

    if k < len(lows):
        return quick_select(lows, k, pivot_fn)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return quick_select(highs, k - len(lows) - len(pivots), pivot_fn)


print(quick_median(array, pivot_func))  # вычисляем медиану
print(statistics.median(array))  # проверяем, что верно

