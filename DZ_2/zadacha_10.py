#5 – Реализуйте алгоритм перемешивания списка.


import random
lst = random.sample(range(1, 100), 10)
print("Исходный список = " + str(lst))
shfl = random.sample(lst, len(lst))
print("Перемешанный список = " + str(shfl))



