# **задача5 HARD необязательная.** 
# Сгенерировать массив случайных целых чисел размерностью m*n (размерность вводим с клавиатуры) , 
# причем чтоб количество элементов было четное. Вывести на экран красивенько таблицей. 
# Перемешать случайным образом элементы массива, причем чтобы каждый гарантированно переместился на другое место  
# и выполнить это за m*n / 2 итераций. То есть если массив три на четыре, то надо выполнить не более 6 итераций. 
# И далее в конце опять вывести на экран как таблицу.
from random import randint
import random
def fill_array(): #Заполнение массива сдучайными числами, проверяется, чтобы количество элементов было четно
    n = int(input('Введите количество строк массива: '))
    m = int(input('Введите количество строк в массиве: ')) 
    if n % 2 == 0 or m % 2 == 0:
        array = [[randint(-10, 10) for j in range(m)] for i in range(n)]
    else: 
        print('какое то из чисел должно быть четным')
        n = int(input('Введите количество строк массива: '))
        m = int(input('Введите количество строк в массиве: ')) 
        array = [[randint(-10, 10) for j in range(m)] for i in range(n)]
    return array
def print_array(array): # Печать массива
    for e in array:
        print(e)
def change_array_in_list(array): # Двумерный массив преобразуем в одномерный
    list = []
    for i in range(len(array)):
        for j in range(len(array[i])):
            list.append(array[i][j])
    return list
def change_list(array): # меняем элементы одномерного массива случайным образом, не повторяясь
    index_list = []
    for i in range(len(array)): index_list.append(i) # Создаем список индексов
    k = 0                           # Счетчик итераций
    while k < len(array)/2:
        i = random.choice(index_list)
        j = random.choice(index_list)
        while i == j:                       # Проверяем, чтобы индексы не совпадали
            j = random.choice(index_list)
        tem = array[i]                          # Меняем элементы местами
        array[i] = array[j]
        array[j] = tem
        k += 1
        index_list.remove(i)            # Удаляем использованные индексы из списка индексов
        index_list.remove(j)
    return array

def list_in_mas(array, n, m):       # Обратно преобразуем измененный одномерный массив в двумерный
    new_mas = []
    k = 0
    for i in range(n):
        str = []
        for j in range(k, k + m):
            str.append(array[j])
        new_mas.append(str)
        k += m
    return new_mas
try:
    mas = fill_array()
    print_array(mas)
    list_mas = change_array_in_list(mas)
    new_list_mas = change_list(list_mas)
    new_mas = list_in_mas(new_list_mas, len(mas), len(mas[0]))
    print('Новый массив')
    print_array(new_mas)
except: print('Wrong')