def my_func_1(a,n):
    return a ** n
def my_func_2(a,n):
    res = 1
    if n == 0:
        return 1
    for i in range(abs(n)):
        res *= a
    if n < 0:
        return 1 / res
    else:
        return res
a = int(input('Введите число: '))
n = int(input('Введите степень: '))
print('Результат функции my_func_1:', my_func_1(a,n))
print('Результат функции my_func_2:', my_func_2(a,n))
