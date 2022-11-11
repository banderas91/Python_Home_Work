# 4 – Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

with open('file.txt', 'r') as f:
    content = f.readlines()
content = [line.rstrip('\n') for line in content]
print(content)

n = int(input('Укажите число: '))
k = 0
mult = 1
for i in range(-n, n+1):
    print(i, end=' ')
    for j in content:
        if k == int(j):
            mult *= int(i)
            break
    k += 1
print('\n', mult)
