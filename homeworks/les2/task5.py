my_list = [8, 3, 3, 2, 5]
my_list.sort(reverse=True)

while True:
    new_elem = input('Введите новый элемент рейтинга: ')
    if new_elem.isdigit():
        new_elem = int(new_elem)
        break
    else:
        print('Ошибка ввода, пожалуйста, попробуйте снова.')

for elem in my_list:
    if new_elem > elem:
        my_list.insert(my_list.index(elem), new_elem)
        break
    elif new_elem == elem:
        if (my_list.index(elem) == len(my_list) - 1) or \
                (my_list.index(elem) + my_list.count(elem) - 1 == len(my_list) - 1):
            my_list.append(new_elem)
        else:
            my_list.insert(my_list.index(elem) + (my_list.count(elem) - 1), new_elem)
        break

print(my_list)
