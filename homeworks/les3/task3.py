def my_func(a, b, c):
    """
    На входе ф-ция получает 3 числа. На выходе сумма 2х наибольших.
    :param a: Первое число
    :param b: Второе число
    :param c: Третье число
    :return: Сумма 2х наибольших
    """
    func_list = [a, b, c]
    m1 = func_list.pop(func_list.index(max(func_list), 0))
    m2 = func_list.pop(func_list.index(max(func_list), 0))
    return m1 + m2


print(my_func(3, 1, 5))
