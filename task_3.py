# Задача 3. Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
import random
def list_fractional_part(array):
    list_fraction = []
    for i in array:
        if i > 0: list_fraction.append(round(i % 1, 3))
        else: list_fraction.append(round((i*(-1)) % 1, 3))
    return list_fraction
def find_max(array):
    max = array[0]
    for i in array:
        if i > max: max = i
    return max
def find_min(array):
    min = array[0]
    for i in array:
        if i < min: min = i
    return min
try:
    n = int(input('Введите количество элементов в списке: '))
    list = [round(random.uniform(-5, 5), 3) for i in range(n)]
    print(list)
    list_of_fraction = list_fractional_part(list)
    print(f'Разница между наибольшей и наименьшей дробно части равна: {find_max(list_of_fraction) - find_min(list_of_fraction)}')
except: print('Введите натуральное число!')