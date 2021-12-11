
__author__ = 'Пронин Алексей Андреевич'

"""
3.Склонение слова
Реализовать склонение слова «процент» во фразе «N процентов». 
Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:
1 процент
2 процента
3 процента
4 процента
5 процентов
6 процентов
...
100 процентов
"""

for num in range(1, 101):
    if (10 < num < 21) or (num % 10 in [0, 5, 6, 7, 8, 9]):
        print(num, 'процентов')
    elif num % 10 == 1:
        print(num, 'процент')
    elif num % 10 in [2, 3, 4]:
        print(num, 'процента')


