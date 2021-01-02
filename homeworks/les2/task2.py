my_list = input('Введите значения для списка: ').split()
print(my_list)
for i in range(len(my_list) - 1):
    if i % 2 == 0 and i != len(my_list) - 1:
        my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
print(my_list)

