var_a = 1
var_b = 'a'
var_c = 'z1'
rez = f'var_a = {var_a}\nvar_b = {var_b}\nvar_c = {var_c}'
print(rez)

while True:
    var_a = input('Введите число: ')
    if var_a.isdigit():
        break
    else:
        print('Вы ввели не число. Введите, пожалуйста, число.')
while True:
    var_b = input('Введите число: ')
    if var_b.isdigit():
        break
    else:
        print('Вы ввели не число. Введите, пожалуйста, число.')
while True:
    var_c = input('Введите число: ')
    if var_c.isdigit():
        break
    else:
        print('Вы ввели не число. Введите, пожалуйста, число.')
var_d = input('Ввидите строку: ')
var_e = input('Ввидите строку: ')

rez = f'var_a = {var_a}\nvar_b = {var_b}\nvar_c = {var_c}\nvar_d = {var_d}\nvar_e = {var_e}'

print(rez)