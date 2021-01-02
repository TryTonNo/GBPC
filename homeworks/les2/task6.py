my_products = []
while True:
    z = int(input(' 1 - Добавить товар;\n'
                  ' 2 - Вывеси список продуктов и их характеристики;\n'
                  ' 3 - Выполнить анализ данных;\n'
                  ' 0 - Выход;\n'
                  'Выберите пункт меню: '))
    if z == 0:
        break
    elif z == 1:
        serial_number_product = len(my_products) + 1
        name_product = input('Введите наименование продукта: ')
        cost_product = round(float(input('Введите цену продукта: ')), 2)
        count_product = int(input('Введите количество продукта в наличии: '))
        unit_product = input('Введите единицу измерения продукта: ')
        my_dict = {'Наименование': name_product, 'Цена': cost_product,
                   'Количество': count_product, 'Ед. измерения': unit_product}
        my_products.append((serial_number_product, my_dict))
    elif z == 2:
        for product in my_products:
            print(product)
    elif z == 3:
        new_dict = {}
        for product in my_products:
            for key, val in product[1].items():
                if key not in new_dict.keys():
                    new_dict[key] = []
                new_dict[key].append(val)
                new_dict[key] = list(set(new_dict[key]))
        for key, val in new_dict.items():
            print(f'{key}: {val}')