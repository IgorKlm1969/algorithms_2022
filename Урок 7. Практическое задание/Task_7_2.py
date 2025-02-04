"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.
Решите задачу тремя способами:
1) с помощью сортировки, которую мы не рассматривали на уроке (Гномья, Шелла,
Кучей)
сделайте замеры на массивах длиной 10, 100, 1000 элементов

"""


from random import randint
from timeit import timeit

def median_sort_shell(my_list_2):
    my_array = my_list_2.copy()
    stp_incr = len(my_array) // 2

    while stp_incr:
        for i, element in enumerate(my_array):
            while i >= stp_incr and my_array[i - stp_incr] > element:
                my_array[i] = my_array[i - stp_incr]
                i -= stp_incr
            my_array[i] = element
        stp_incr = 1 if stp_incr == 2 else int(stp_incr * 5 / 11)

    return my_array[len(my_array) // 2]


m_3 = (5, 50, 500)

test_list = tuple([randint(0, 100) for _ in range(m * 2 + 1)] for m in m_3)


print('\n\nФункция на основе сортировки Шелла:')
for test in test_list:
    print(f'\nМассив из {len(test)} элемента(-ов): {median_sort_shell(test)}')
    print(f'Проверка встроенной функцией statistics  median: {median(test)}')
    print(f'Время выполнения: {timeit("median_sort_shell(test[:])", globals=globals(), number=1000)}')
    # print(f'Время выполнения: {timeit("median(test)", globals=globals(), number=1000)}')

"""
Функция на основе сортировки Шелла:

Массив из 11 элемента(-ов): 38
Проверка встроенной функцией statistics  median: 38
Время выполнения: 0.006427800000000872

Массив из 101 элемента(-ов): 55
Проверка встроенной функцией statistics  median: 55
Время выполнения: 0.08081070000000068

Массив из 1001 элемента(-ов): 50
Проверка встроенной функцией statistics  median: 50
Время выполнения: 1.5554209000000014


   
Здесь видно, что быстрее всего с задачей справляются встроенный алгоритм statistics.median, и с применением 
сортировки Шелла. 

Алгоритм на основе разбиения и равенства массивов использует  полный обход 
по всем элементам массива с выполнением повторного обхода по всем элементам,т.е. сложность этого алгоритма будет O(N^2).
Алгоритм,  использующий исключение максимальных элементов имеет сложность O(N^2), но обходит только
половину массива.

"""
