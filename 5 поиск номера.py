import re

a= '5 поиск номера.txt'

with open(a,'r',encoding='utf-8') as f:
    a= f.read()
    # a2= f.readlines()

out = re.findall(r'7(?:\s?)\((?:\s?)[4|Ч](?:\s?)9(?:\s?)5(?:\s?)\)(?:\s?)7(?:\s?)[4|Ч](?:\s?)[0|O|О](?:[\s~\-\=]+)6(?:\s?)6(?:[\s~\-\=]{,4})6(?:\s?)5',a)

# print(len([item for item in a2 if item != '\n'])) --- проверка на то сколько номеров есть впринципе (50)
print(out)
print(len(out))