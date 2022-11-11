# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности,
# список повторяемых и убрать дубликаты из заданной последовательности.

# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10] и [1, 3, 5] и [1, 2, 5, 3, 10]

from random import randint

lst = [randint(1, 10) for _ in range(15)]
print("Оригинальный список : ",  lst)


rez = []
for el in lst:
    if lst.count(el) == 1:
        rez.append(el)
print("Список уникальных элементов : ", rez)


visited = set()
dup = {x for x in lst if x in visited or (visited.add(x) or False)}

print("Дубликаты", dup)
# через списки дубликаты выводятся несколько раз, поэтому вариант через с множеством

li = []
for i in lst:
    if i not in li:
        li.append(i)
print("Список после удаления дубликатов : ", str(li))
