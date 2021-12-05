
__author__ = 'Пронин Алексей Андреевич'

"""
4. Дан список, содержащий искажённые данные с должностями и именами сотрудников:
['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

a)Известно, что имя сотрудника всегда в конце строки. Сформировать и вывести на экран фразы вида: 'Привет, Игорь!' 
b)Подумать, как получить имена сотрудников из элементов списка, как привести их к корректному виду.
Можно ли при этом не создавать новый список?
"""

data_lst = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
# Пункт а
for d in data_lst:
    print(f'Привет, {d.split()[-1].title()}!')
# Пукнт b
for d in data_lst:
    i = data_lst.index(d)
    name = d.split()[-1].title()
    d = d.split()[:-1]
    d.append(name)
    d = ' '.join(d)
    data_lst[i] = d
print(data_lst)
