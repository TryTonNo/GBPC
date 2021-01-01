while True:
    proceeds = input('Введите выручку фирмы: ')
    if len(proceeds.split('.')) == 2 or (len(proceeds.split('.')) == 1 and proceeds.isdigit()):
        proceeds = round(float(proceeds), 2)
        break
    else:
        print('Ошбика ввода. Выручка фирмы должна быть числом. Пожалуйста, повторите попытку ввода.')
while True:
    costs = input('Введите издержки фирмы: ')
    if len(costs.split('.')) == 2 or (len(costs.split('.')) == 1 and costs.isdigit()):
        costs = round(float(costs), 2)
        break
    else:
        print('Ошбика ввода. Издержки фирмы должны быть числом. Пожалуйста, повторите попытку ввода.')

if proceeds > costs:
    profit = proceeds - costs
    rez = f'Фирма работает в плюс. Она получает прибыль.' \
          f'\nРентабельность прибыли составляет: {round(profit / proceeds, 2)} '
    while True:
        count_emp = input('Введите количество сотрудников: ')
        if count_emp.isdigit() and len(count_emp.split('.')) == 1:
            rez += f'\nПрибыль на одного сотрудка составляет: {round(profit / int(count_emp), 2)}'
            break
        else:
            print('Количество сотрудников должно быть целым числом. Пожалуйста, повторите попытку ввода.')
else:
    rez = 'Фирма работает в убыток.'

print(rez)
