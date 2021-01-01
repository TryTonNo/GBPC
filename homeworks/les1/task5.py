while True:
    proceeds = input('Введите выручку фирмы: ')
    if proceeds.isdigit():
        # Я знаю, что isdigit не пропустит число с плавающей точкой, но пилить функцию,
        # если мы ее еще не проходили не считаю правильным.
        proceeds = round(float(proceeds), 2)
        break
    else:
        print('Выручка фирмы должна быть числом. Пожалуйста, повторите попытку ввода.')
while True:
    costs = input('Введите издержки фирмы: ')
    if costs.isdigit():
        costs = round(float(costs), 2)
        break
    else:
        print('Издержки фирмы должны быть числом. Пожалуйста, повторите попытку ввода.')

if proceeds > costs:
    profit = proceeds - costs
    rez = f'Фирма работает в плюс. Она получает прибыль.' \
          f'\nРентабельность прибыли составляет: {round(profit / proceeds, 2)} '
    while True:
        count_emp = input('Введите количество сотрудников: ')
        if count_emp.isdigit():
            rez += f'\nПрибыль на одного сотрудка составляет: {round(profit / int(count_emp), 2)}'
            break
        else:
            print('Количество сотрудников должно быть целым числом. Пожалуйста, повторите попытку ввода.')
else:
    rez = 'Фирма работает в убыток.'

print(rez)
