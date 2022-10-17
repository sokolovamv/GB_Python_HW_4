# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
def prime_factors(number):
    prime_factors_list = []  
    flag = False
    for i in range(2, number + 1):
        if not number % i:
            for j in range(2, i):
                if not i % j:
                    flag = True
                    break
            if not flag:
                prime_factors_list.append(i)
    return prime_factors_list

print(f'Простые множители введенного Вами числа: {prime_factors(int(input("Введите число: ")))}')