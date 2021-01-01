while True:
    n = input('Введите число: ')
    if n.isdigit():
        n = int(n)
        break
    else:
        print('Вы ввели не число. Пожалуйста, введите число.')

rez = f'{n} + {str(n)*2} + {str(n) * 3} = {n + int(str(n) * 2) + int(str(n) * 3)}'

print(rez)
