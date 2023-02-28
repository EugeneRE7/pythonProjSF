# На вход подается последовательность чисел через пробел, затем любое число.
# Можно выполнить проверку соответствия вводимых данных.
# 1. Преобразование введенной последовательности в список.
# 2. Сортировка списка по возрастанию элементов (определить функцию).
# 3. Устанавливается номер позиции элемента, который меньше
# введенного числа, а следующий за ним больше или равен этому числу.
# При установке позиции элемента воспользоваться алгоритмом двоичного поиска (реализовать так же отдельной функцией).
# 14 13 12 11 10 9 8 7 6 5 4 3 2 1
# 6.9 -10.1 -100 23 -10.5 10 -5.4
def sort_list(nlist):
    # nlist = sorted(numList)
    for i in range(len(nlist)):
        for j in range(len(nlist) - i - 1):
            if nlist[j] > nlist[j + 1]:
                nlist[j], nlist[j + 1] = nlist[j + 1], nlist[j]
    return nlist


def pos_idx_less(nlist, n, lft, rht):
    if lft > rht:
        return False
    mid = int((lft + rht) // 2)
    if nlist[mid] < n <= nlist[mid+1]:
        return mid  # mid-индекс, nlist[mid]-элемент
    elif n <= nlist[mid]:
        return pos_idx_less(nlist, n, lft, mid - 1)
    else:
        return pos_idx_less(nlist, n, mid + 1, rht)


def pos_idx_more_or_equal(nlist, n, lft, rht):
    if lft > rht:
        return False
    mid = int((lft + rht) // 2)
    if nlist[mid-1] < n <= nlist[mid]:
        return mid  # mid-индекс, nlist[mid]-элемент
    elif n < nlist[mid]:
        return pos_idx_more_or_equal(nlist, n, lft, mid - 1)
    else:
        return pos_idx_more_or_equal(nlist, n, mid + 1, rht)


try:
    numList = list(map(float, input('Введите числа через пробел: ').split()))
except ValueError as error:
    print(error)
    print('Нарушен формат ввода числовых значений!')
else:
    try:
        num = float(input('Введите любое число: '))
    except ValueError as error:
        print(error)
        print('Нарушен формат ввода числового значения! \n'
              'Либо введено более одного числа!')
    else:
        numList = sort_list(numList)
        print('Упорядоченный массив:\n', numList)
        if num <= numList[0] or num > numList[-1]:
            print('Массив не содержит значений, удовлетворяющих обоим условиям сравнения с введенным числом. \n'
                  'Либо введено число, выходящее за рамки массива!')
        else:
            print(pos_idx_less(numList, num, 0, len(numList)),
                  '- позиция элемента, который меньше введенного числа')
            print(pos_idx_more_or_equal(numList, num, 0, len(numList)),
                  ' - позиция элемента, который больше или равен введенному числу')
