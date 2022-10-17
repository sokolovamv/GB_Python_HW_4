# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

import random

# запись в файл с перезаписью
def write_file(text):
    with open('file.txt', 'w') as file:
        file.write(text)

# создание ненулевого списка коэффициентов
def create_random_list(degree):
    random_list = [random.randint(0, 101) for  i in range(degree + 1)]
    while sum(random_list) == 0:
        random_list = [random.randint(0, 101) for  i in range(degree + 1)]
    return random_list

# создание списка полинома
def polynom(coefficients):
    polynom_list = []
    for i in range(len(coefficients)):
        if i == len(coefficients) - 2 and coefficients[i] != 0:
          polynom_list.append(f'{coefficients[i]}*x')
        elif i == len(coefficients) - 1 and coefficients[i] != 0:
            polynom_list.append(f'{coefficients[i]}')
        elif coefficients[i] != 0:
            polynom_list.append(f'{coefficients[i]}*x^{str(k - i)}')
    return polynom_list

k = int(input('Введите натуральное число: '))
while k < 1:
    k = int(input('Введите натуральное число: '))  

coeff_list = create_random_list(k)
text_for_file = " + ".join(polynom(coeff_list)).replace(' 1*', ' ') + ' = 0' # перевод списка в строку
# проверка на первый коэффициент
if text_for_file[0:2] == '1*':
    text_for_file = text_for_file.replace('1*', '')
write_file(text_for_file)