__author__ = 'Пронин Алексей Андреевич'

"""
Задание 2:
* (вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): 
реализовать корректную работу с числительными, начинающимися с заглавной буквы — результат тоже должен быть с заглавной.

Например:
>>> num_translate_adv("One")
"Один"
>>> num_translate_adv("two")
"два"
"""


def num_translate_adv(num):
    dic_translate = {'zero': 'ноль'
        , 'one': 'один'
        , 'two': 'два'
        , 'three': 'три'
        , 'four': 'четыре'
        , 'five': 'пять'
        , 'six': 'шесть'
        , 'seven': 'семь'
        , 'eight': 'восемь'
        , 'nine': 'девять'
        , 'ten': 'десять'
                     }
    if num[0].isupper():
        print(dic_translate.get(num.lower()).capitalize())
    else:
        print(dic_translate.get(num))


num_translate_adv(input('Введите, пожалуйста, текст для перевода: '))
