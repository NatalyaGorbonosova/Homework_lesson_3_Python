# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import randint
def mult_par_list(array):
    list_mult = []
    if len(array) % 2 == 0:
        for i in range(len(array)//2):
            list_mult.append(array[i]*array[ - 1 - i])
    else:
        for i in range(len(array)//2):
            list_mult.append(array[i]*array[- 1 - i])
        list_mult.append(array[(len(array)//2)]**2)
    return list_mult
try:
    n = int(input('Введите количество элементов в списке: '))
    list = [randint(-10, 10) for i in range(n)]
    print(list)
    list_new = mult_par_list(list)
    print(list_new)
except: print('Введите натуральное число!')