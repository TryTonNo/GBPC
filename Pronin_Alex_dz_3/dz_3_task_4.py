__author__ = 'Пронин Алексей Андреевич'

"""
Задание 4:
* (вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате «Имя Фамилия» и
возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари,
реализованные по схеме предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы.

Например:
>>>thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
{
    "А": {
        "П": ["Петр Алексеев"]
    }, 
    "С": {
        "И": ["Иван Сергеев", "Инна Серова"], 
        "А": ["Анна Савельева"]
    }
}
Как поступить, если потребуется сортировка по ключам?
"""


def thesaurus_adv(*args):
    my_notebook = {}
    for Name_Surname in args:
        name = Name_Surname.split()[0]
        surname = Name_Surname.split()[1]
        if surname[0] not in my_notebook.keys():
            my_notebook[surname[0]] = {name[0]: [Name_Surname]}
        else:
            if name[0] not in my_notebook[surname[0]].keys():
                my_notebook[surname[0]][name[0]] = [Name_Surname]
            else:
                my_notebook[surname[0]][name[0]].append(Name_Surname)
    print(my_notebook)


thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
