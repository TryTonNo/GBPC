__author__ = 'Пронин Алексей Андреевич'

# Задание 1: Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration
# в секундах:
# a)до минуты: <s> сек;
# b)до часа: <m> мин <s> сек;
# c)до суток: <h> час <m> мин <s> сек;
# *d) в остальных случаях: <d> дн <h> час <m> мин <s> сек.

# Примеры:
# duration = 53
# 53 сек
# duration = 153
# 2 мин 33 сек
# duration = 4153
# 1 час 9 мин 13 сек
# duration = 400153
# 4 дн 15 час 9 мин 13 сек

# Вариант после просмотра 2 урока
while True:
    duration = int(input('Для выхода из программы введите 0, иначе значение больше 0: '))
    days = duration // 86400
    new_duration = duration % 86400
    hours = duration // 3600
    new_duration = new_duration % 3600
    minutes = new_duration // 60
    seconds = new_duration % 60
    if duration < 0:
        print("Отрицательного времени не существует! Попробуйте еще раз.")
    elif duration == 0:
        print("Инициализирован выход из программы.\nСпасибо за участие в тестировании.")
        break
    # пукт a
    elif duration < 60:
        print(seconds, 'ceк')
    # пункт b
    elif duration < 3600:
        print(minutes, 'мин', seconds, 'сек')
    # пункт с
    elif duration < 86400:
        print(hours, 'час', minutes, 'мин', seconds, 'сек')
    # пункт d
    else:
        print(days, 'дн', hours, 'час', minutes, 'мин', seconds, 'сек')

"""
#Варинат до просмотра 2 урока
duration = int(input('Пожалуйста, введите число больше 0: '))
if duration <= 0:
    print('Убедитесь, что Вы ввели число больше 0!')
# пукт a
elif duration < 60:
    print(str(duration) + ' сек')
# пункт b
elif duration < 3600:
    minutes = duration // 60
    seconds = duration - minutes * 60
    print(str(minutes) + ' мин ' + str(seconds) + ' сек')
# пункт с
elif duration < 86400:
    hours = duration // 3600
    new_duration = duration - hours * 3600
    minutes = new_duration // 60
    new_duration -= minutes * 60
    seconds = new_duration
    print(str(hours) + ' час ' + str(minutes) + ' мин ' + str(seconds) + ' сек')
# пункт d
else:
    days = duration // 86400
    new_duration = duration - days * 86400
    hours = new_duration // 3600
    new_duration = new_duration - hours * 3600
    minutes = new_duration // 60
    new_duration -= minutes * 60
    seconds = new_duration
    print(str(days) + ' дн ' + str(hours) + ' час ' + str(minutes) + ' мин ' + str(seconds) + ' сек')"""
