# Vasilii Sitdikov
# GeekBrains Courses. Algorithms
# Lesson 7 task 3
# October 2019

# task: 3 Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
#       Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
#       которые не меньше медианы, в другой — не больше медианы.
#       Примечание: задачу можно решить без сортировки исходного массива.
#       Но если это слишком сложно, используйте метод сортировки, который не рассматривался на уроках
#       (сортировка слиянием также недопустима).
# ----------------------------------------------------------------------------------------------------------------------
# Solution:
# Предложенное решение позволяет достаточно быстро находить медиану БЕЗ СОРТИРОВКИ массива.
# Решение состоит из двух функций, вспомогательной appr_perc, подсчитывающей количество эллементов в массиве,
# передаваемом первым аргументом, которые меньше, равны или больше предложенного вторым аргументом "кандидата".
# Основная функция perc_miner предлагает вспомогательной функции "кандидатов", расчитывая значение нового кандидата
# исходя из предыдущего анализа линейным приближением.
# Я оставил в коде выводы промежуточных результатов, позволяющие посмотреть количество проходов для поиска.
# Видно, что функция работает достаточно резво. Для нормальных распределений медиана находится за одну итерацию,
# вне зависимости от величины массива, при больщой дисторции количество проходов увеличивается, но даже для
# экспоненциального ряда понадобилось только 2 прохода (имеются ввиду проходы, изменяющие линейную сложность решения).


def appr_perc(a, cand):
    # В целях оптимизации работы ищем реального кандидата (среди элементов списка), то есть либо равного,
    # либо самого ближнего из меньших.
    new_cand_exist = False
    new_cand = 0
    for el in a:
        if el == cand:
            new_cand = el
            break
        elif el > cand:
            continue
        elif not new_cand_exist:
            new_cand_exist = True
            new_cand = el
        elif new_cand < el < cand:
            new_cand = el
    cand = new_cand
    print(f'New candidate from appr_perc function is {cand}')

    # Считаем количество элементов больше, меньше, и равных кандидату на ответ
    count_less = 0
    count_more = 0
    count_eq = 0
    for el in a:
        if el < cand:
            count_less += 1
        elif el > cand:
            count_more += 1
        else:
            count_eq += 1

    return count_less, count_eq, count_more, cand


# ----------------------------------------------------------------------------------------------------------------------
def perc_miner(a, perc=50):
    # Определяем максимум и минимум (сделано без встроенных функций для прозрачности сложности)
    my_max = my_min = a[0]
    for el in a:
        if el < my_min:
            my_min = el
        if el > my_max:
            my_max = el
    print('*' * 50)
    print(f'Minimum = {my_min}, Maximum = {my_max}')
    search_pos = (len(a) * perc) // 100 + 1
    print(f"Massive's length is {len(a)}. Searched position is {search_pos}")
    cand = my_min + (my_max - my_min) * perc / 100  # Кандидат на ответ исходя из предположения линейности
    print(f'Candidate 0 = {cand}')
    count_less, count_eq, count_more, cand = appr_perc(a, cand)

    i = 0
    while True:
        i += 1
        print('*' * 50)
        print(f'Pass {i}:')
        print(f'Count_less = {count_less}, Count_eq = {count_eq}, Count_more = {count_more}, Candidate = {cand}')
        if count_less + 1 <= search_pos <= count_less + count_eq + 1:
            print('*' * 50)
            return cand
        elif count_less + 1 > search_pos:
            my_max = cand
            cand = my_min + (my_max - my_min) * search_pos / (count_less + 1)
            count_less, count_eq, count_more, cand = appr_perc(a, cand)
        elif count_more + 1 > search_pos:
            my_min = cand
            cand = my_min + (my_max - my_min) * search_pos / (count_more + 1)
            count_less, count_eq, count_more, cand = appr_perc(a, cand)


my_list = [1000000, 1000000, 1, 10, 100, 1000, 10000, 100000, 100000]
print(f'Median is equal to {perc_miner(my_list)}')
