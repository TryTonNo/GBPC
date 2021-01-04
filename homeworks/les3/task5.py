def is_digit(string):
    if string.isdigit():
        return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False


def summa(rez=0):
    l1 = input('Введите числа через пробел: ').split()
    for elem in '[@_!#$%^&*()<>?/\|}{~:]':
        try:
            if type(specialSymb) != type(list()):
                specialSymb = []
        except NameError:
            specialSymb = []
        specialSymb.append(elem)
    for elem in l1:
        ex = 0
        if elem in specialSymb:
            ex = 1
            break
        elif elem.isdigit():
            rez += int(elem)
        elif is_digit(elem):
            rez += float(elem)
        # else:
        #     print(f'Элемент {elem} не является числом.')
    print(rez)
    if ex == 0:
        return summa(rez)
    else:
        return 0

summa()