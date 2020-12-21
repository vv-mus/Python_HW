def fact(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
        yield i, factorial


n = int(input('Введите число: '))
print(fact(n))
for el in fact(n):
    print(f'{el[0]}! = произведение {list(range(1, el[0] + 1))} = {el[1]}')
