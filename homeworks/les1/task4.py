n = int(input('Введите целое положительное число: '))
if n < 0:
    n *= -1
if n != 0:
    m = int(n % 10)
    n /= 10
while n > 0:
    if m < n % 10:
        m = int(n % 10)
    n /= 10
print(m)
