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
