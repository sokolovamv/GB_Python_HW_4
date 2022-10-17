# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
import random
numbers = [random.randint(0, 10) for  i in range(random.randint(5, 10))]
print(f'Первоначальный список: {numbers}')
unique_numbers = list(set(numbers))
print(f'Список уникальных чисел: {unique_numbers}')