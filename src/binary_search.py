from binarytree import bst


def bin_search(bin_search_tree, number, path=''):
    if bin_search_tree.value == number:
        return f'Число {number} обнаружено по пути: Корень {path}'

    if number < bin_search_tree.value and bin_search_tree.left != None:
        return bin_search(bin_search_tree.left, number, path=f'{path} - шаг влево')

    if number > bin_search_tree.value and bin_search_tree.right != None:
        return bin_search(bin_search_tree.right, number, path=f'{path} - шаг вправо')

    return f'Число {number} отсутствует в дереве'


bt = bst(height=5, is_perfect=False)
print(bt)

num = int(input('Введите число для поиска: '))
print(bin_search(bt, num))
