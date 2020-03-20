''' Case study The generation of proposals
Developers: Arkhipova A.(55%)
            Revtova L.(67%)
'''
import random

line = ''
x = ''
predl = 0
symbol_1 = '0123456789 ,.!?'
letter = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
letter_b = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
with open("rf.txt", encoding='utf-8') as f:
    text = f.readlines()
    for i in text:
        t = i.count('.')
        vos = i.count('!')
        vop = i. count('?')
        predl = predl + t + vos + vop
        t = 0
        vos = 0
        vop = 0
    for i in text:
        x = x + i + ' '
for i in x:
    if i in symbol_1 or i in letter:
        line = line + i

new_list = line.split()
copy_list = new_list
c = []
dictionary = {}

for i in range(len(new_list)):
    for j in range(len(copy_list)-1):
        if new_list[i] == copy_list[j]:
            c.append(copy_list[j+1])
    dictionary[new_list[i]] = c
    c = []

dict_up = {}
for key, value in dictionary.items():
    for i in key:
        if i in letter_b:
            dict_up[key] = value
            
start_words = []
kol = int(input('Выберите количество предложений от 1 до ' + str(predl)))
osnov = ''
for j in range(kol):
    for k in dict_up.keys():
        start_words.append(k)
    if len(start_words) == 0:
        break
    if len(start_words) == 1:
        rand = 0
    else:
        rand = random.randint(0, len(start_words) - 1)
    start_word = start_words[rand]
    new_text = start_word
    slov = random.randint(5, 8)
    copy_list = dictionary[start_word]

    for i in range(slov - 1):
        if len(copy_list) == 0:
            break
        if len(copy_list) == 1:
            rand_2 = 0
        else:
            rand_2 = random.randint(0, len(copy_list) - 1)
        second = copy_list[rand_2]
        new_text = new_text + ' ' + second
        copy_list = dictionary[second]

    symbol_end = '.!?'
    for m in symbol_end:
        if m in new_text[:-1]:
            new_text = new_text.replace(m, '')
    if new_text[-1] not in symbol_end and new_text[-1] != ',':
        new_text = new_text + '.'
    elif new_text[-1] == ',':
        new_text = new_text[:-1] + '.'
    new_text = new_text.capitalize()
    osnov += new_text + ' '
    new_text = ''
print(osnov)
