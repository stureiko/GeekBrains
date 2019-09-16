# Даны два списка фруктов. Получить список фруктов, присутствующих в обоих исходных списках.
#
#     Примечание: Списки фруктов создайте вручную в начале файла.

# Исходные списки
fruits_1 = ['apple', 'peach', 'banana', 'baba', 'hjkd', 'hbn']
fruits_2 = ['cocos', 'melon', 'figa', 'hbn']

# формирвоание результата черз генератор и проверку
result = [fruit for fruit in fruits_1 if fruit in fruits_2]
print(result)
