def divisions(a: int, b: int):
    try:
        return a / b
    except ZeroDivisionError as e:
        return e

a = int(input('Введите делимое: '))
b = int(input('Введите делитель: '))
rez = f'Результат выражения {a} / {b} = {divisions(a, b)}'
print(rez)