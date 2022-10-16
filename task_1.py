# Задача 1 Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
from random import randint


def sum_element(array):
    sum = 0
    for i in range(1, len(array)):
        if i%2 == 1:
            sum += array[i]
        else: sum = sum
    return sum
try:
    n = int(input('Введите количество элементов в списке: '))
    list = [randint(-20, 20) for i in range(n)]
    print(list)
    print(f'Сумма элементов на нечетных местах равна: {sum_element(list)}')
except: print('Введите число')