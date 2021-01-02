while True:
    my_month = input('Введите номер месяца: ')
    if my_month.isdigit():
        my_month = int(my_month)
        break
    else:
        print('Вы ввели не месяц. Пожалуйста, повторите попытку ввода.')

seasons = {'Зима': [1, 2, 12], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}
for season in seasons:
    if my_month in seasons[season]:
        print(season)
        break
