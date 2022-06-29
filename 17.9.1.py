
# проверяемая последовательность чисел, введенная через пробел
sequence_of_numbers =list(map( int, input('Введите через пробел : \n').split()))
print('sequence_of_numbers', sequence_of_numbers, type(sequence_of_numbers))

# 1. Преобразование введённой последовательности в список
element = int(input('Введите любое произвольное число: \n'))
print('element', element, type(element))
array = sequence_of_numbers + [element]
print('array', array, type(array))

# 2.Сортировка списка по возрастанию элементов в нем


for i in range(len(array)):  # проходим по всему массиву
    idx_min = i  # сохраняем индекс предположительно минимального элемента
    for j in range(i, len(array)):
        if array[j] < array[idx_min]:
            idx_min = j
    if i != idx_min:  # если индекс не совпадает с минимальным, меняем
        array[i], array[idx_min] = array[idx_min], array[i]

print(array)


# # 3.Установка позиции элемента алгоритмом двоичного поиска. Реализован отдельной функцией.
def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находим середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)
# запускаем алгоритм на левой и правой границе

print(binary_search(array, element, 0, len(array)-1))