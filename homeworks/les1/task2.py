while True:
    time_s = input('Введите время в секундах: ')
    if time_s.isdigit():
        time_s = int(time_s)
        break
    else:
        print('Вы неправильно произвели ввод. Пожалуйста, введите секунды.')

if time_s >= 3600:
    hours = time_s // 3600
else:
    hours = 0

if time_s >= 60:
    minutes = (time_s - int(hours) * 3600) // 60
else:
    minutes = 0

seconds = time_s - (int(hours) * 3600 + int(minutes) * 60)

if hours < 10:
    hours = '0' + str(hours)
if minutes < 10:
    minutes = '0' + str(minutes)
if seconds < 10:
    seconds = '0' + str(seconds)

rez = f'{hours}:{minutes}:{seconds}'

print(rez)
