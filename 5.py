# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# функция формирования списка из строки
def list_of_polynom(polynom):
    return polynom.split("+")

# функция, которая выделяет коэффициенты многочлена
def find_digit(term):
    digit_of_term = []
    for i in range(len(term)):
        digit_of_term.append(term[i])
        # если нет коэффициента перед х возвращаем 1
        if term[0] == 'x':
            return 1
        # если есть коэффициент, ищем его
        elif term[i + 1] == '*' or term[i + 1] == 'x':
            break
    return int("".join(digit_of_term))

# функция нахождения суммы полиномов    
def sum_of_polynom(poly_1, poly_2):
    total_list = []
    for i in range(len(poly_1)):
        for j in range(len(poly_2)):
            # рассматриваем x в первой степени
            if poly_1[i][-1] == 'x' or poly_2[j][-1] == 'x':
                # если данная степень есть в обоих многочленах
                if poly_1[i][-1] == poly_2[j][-1]:
                    new_coef = find_digit(poly_1[i]) + find_digit(poly_2[j])
                    total_list.append(f'{new_coef}*{poly_1[i][-1]}')
                # если данная степень только в первом многочлене
                elif  poly_1[i][-1] != poly_2[j][-1] and poly_1[i] not in " ".join(total_list):
                    total_list.append(poly_1[i])
                # если данная степень только во втором многочлене
                elif  poly_1[i][-1] != poly_2[j][-1] and poly_2[j] not in " ".join(total_list):
                    total_list.append(poly_2[j])
            # рассматриваем x в степени больше 1
            # если данная степень есть в обоих многочленах
            elif poly_1[i][-2::] == poly_2[j][-2::]:
                new_coef = find_digit(poly_1[i]) + find_digit(poly_2[j])
                total_list.append(f'{new_coef}*{poly_1[i][-3::]}') 
            # если данная степень только в первом многочлене
            elif poly_1[i][-2::] not in " ".join(poly_2) and poly_1[i][-2::] not in " ".join(total_list):
                total_list.append(poly_1[i])
            # если данная степень только во втором многочлене
            elif poly_2[j][-2::] not in " ".join(poly_1) and poly_2[j][-2::] not in " ".join(total_list):
                total_list.append(poly_2[j])
            # рассматриваем константы
            # если данная степень есть в обоих многочленах
            elif poly_1[i].isdigit() and poly_2[j].isdigit():
                new_coef = int(poly_1[i]) + int(poly_2[j])
                total_list.append(str(new_coef))
            # если данная степень только в первом многочлене
            elif poly_1[i].isdigit() and (poly_1[i] + ' ') not in " ".join(total_list):
                total_list.append(poly_1[i])
            # если данная степень только во втором многочлене
            elif poly_2[j].isdigit() and (poly_2[j] + ' ') not in " ".join(total_list):
                total_list.append(poly_2[j])
    return (" + ".join(total_list) + ' = 0')

# для данных многочленов задача выполняется, но до ума она не доведена, все сроки прошли, поэтому сдаю, что есть...
with open('file_1.txt', 'w') as file:
    file.write('2*x^6+5*x^5+4*x^4+2*x')
with open('file_2.txt', 'w') as file:
    file.write('23*x^6+x^5+3*x^3+5')

with open('file_1.txt','r') as file:
    polynom_1 = file.readline()
    list_of_poly_1 = list_of_polynom(polynom_1)

with open('file_2.txt','r') as file:
    polynom_2 = file.readline()
    list_of_poly_2 = list_of_polynom(polynom_2)

with open('sum_polynoms.txt', 'w') as file:
    file.write(sum_of_polynom(list_of_poly_1, list_of_poly_2))

