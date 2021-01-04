def my_func_first(x: int, y: int):
    return float(x ** y)


def my_func_second(x: int, y: int):
    if y == 0:
        return 1
    elif y == -1:
        return 1 / x
    elif y <= -2:
        rez = x
        for i in range(y*(-1) - 1):
            rez *= x
            # print(f'Шаг {i}: {rez}')
        return float(1 / rez)

n, m = (2, -10)
a = my_func_first(n, m)
b = my_func_second(n, m)
print(a==b)
print(my_func_first(n, m))
print(my_func_second(n, m))
