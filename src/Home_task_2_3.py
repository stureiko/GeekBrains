# 3: Дан список заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут только уникальные элементы исходного.

# Исходный список
my_list_1 = [2, 2, 5, 12, 8, 2, 12]

# новый список куда будут складываться уникальные значения
my_list_2 = []

# дабы сократить количество итераций приведем исходный список к множеству - это уберет дубликаты
for item in set(my_list_1):  # проходим по всем элементам
    if my_list_1.count(item) > 1:   # если элемент встречается в исходном списке более 1-го раза то
        continue                    # пропускаем его
    else:
        my_list_2.append(item)      # иначе добавляем его в новый список

print(my_list_2)    # печатаем итоговый список