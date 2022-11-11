# Напишите программу, удаляющую из текста все слова, в которых присутствуют все буквы "абв".

line = "Не получить аб3eв априввыыыб вовсе  - не страшно, быцвувцыцвва но лишиться полученного  обидно"

words = line.split(' ')

new_words = []
for word in words:
    if not (('а' in word) and ('б' in word) and ('в' in word)):
        new_words.append(word)
txt = ' '.join(new_words)
print(txt)
