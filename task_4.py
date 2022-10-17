# Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное. Нельзя использовать готовые функции.
def devision_on_two(num):
    list_num = []
    while num != 0:
        list_num.append(num % 2)
        num = num // 2
    return list_num
def list_on_str(array):
    new_list = array[::-1]
    str_num = ''
    for i in new_list:
        str_num = str_num + str(i)
    return str_num
try:
    number = int(input('Введите число: '))
    if number > 0:
        binary_num = devision_on_two(number)
        sing = ''
    else: 
        number *= -1
        binary_num = devision_on_two(number)
        sing = '-'
    print(f'В двоичное системе это будет: {sing}{list_on_str(binary_num)}')
except: print('Введите целое число!')

