__author__ = 'Пронин Алексей Андреевич'

"""
Задание 5:
Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого):
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
        Например:
>>> get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]
Документировать код функции.

Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках 
(когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?
"""

from random import choice, randrange


def get_jokes(n, replay=True):
    """Составление n-ного количество шуток из 3-ех списков слов."""

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    max_count_joke = min(len(nouns), len(adverbs), len(adjectives))
    jokes = []
    if replay:
        for i in range(n):
            jokes.append(' '.join([choice(nouns), choice(adverbs), choice(adjectives)]))
    else:
        words = {'nouns': nouns, 'adverbs': adverbs, 'adjectives': adjectives}
        for i in range(n):
            joke = ''
            for k in words.keys():
                if joke == '':
                    joke = words[k].pop(randrange(len(words[k])))
                else:
                    joke += ' ' + words[k].pop(randrange(len(words[k])))
            jokes.append(joke)
            if words['nouns'] == [] or words['adverbs'] == [] or words['adjectives'] == []:
                print(f'Больше {max_count_joke} шуток составить нельзя')
                break
    print(jokes)


print('Повтор слов разрешен')
get_jokes(int(input("Введите, пожалуйста, желаемое количество шуток: ")))
print('Без повтора слов')
get_jokes(int(input("Введите, пожалуйста, желаемое количество шуток от 1 до 5: ")), replay=False)

