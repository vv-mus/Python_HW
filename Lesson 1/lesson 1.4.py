n = int(input('Введите число: '))
max = 0
rem = 0
while n > 0:
    rem = n % 10
    if rem >= max:
        max = rem
    n //= 10
print(f'Максимальная цифра в числе: {max}')