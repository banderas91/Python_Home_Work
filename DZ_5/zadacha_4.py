# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open('input_task_04.txt', 'w') as file:
    file.write(input('Напишите текст необходимый для сжатия: '))

with open('input_task_04.txt', 'r') as file:
    s = file.readline()
print(f"Изначальный текст: {s}")


def coding(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res


def dec(txt):
    res = ''
    for i in range(0, len(txt), 2):
        res += txt[i + 1] * int(txt[i])
    return res


print(f"Текст после кодировки: {coding(s)}")
with open('encode_task_04.txt', 'w') as file:
    file.write(coding(s))

print(f"Текст после дешифровки: {dec(coding(s))}")
with open('decode_task_04.txt', 'w') as file:
    file.write(dec(coding(s)))
