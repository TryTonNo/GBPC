my_str = input('Введите строку: ')
for ind, word in enumerate(my_str.split()):
    if len(word) > 10:
        print(ind, word[:10])
    else:
        print(ind, word)
