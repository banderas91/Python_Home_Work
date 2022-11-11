# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.2

from random import uniform

n = int(input('Введите размер строки '))
res = []
for i in range(n):
    f = uniform(0, 9)
    res.append(round(f, 2))

print(res)

dif = []
for i in range(len(res)):
    dif.append(res[i] % 1)

print(round(max(dif) - min(dif), 2))
