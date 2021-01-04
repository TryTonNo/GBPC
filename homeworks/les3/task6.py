def int_func(my_str: str):
    if len(my_str.split()) > 1:
        new_list = my_str.split()
        for i in range(len(new_list)):
            new_list[i] = new_list[i].title()
        my_str = ' '.join(new_list)
    else:
        my_str = my_str.title()
    return my_str

# def int_func(my_str: str):
#     return my_str.title()

print(int_func('title'))
print(int_func('title it is mine'))