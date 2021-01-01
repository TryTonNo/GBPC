n = int(input('Введите число: '))
# Можно так
print(n + n * 11 + n * 111)
# А можно так
print(n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n)))
