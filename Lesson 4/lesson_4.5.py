from functools import reduce


def multiplication(prev_el, el):
    return prev_el * el


new_list = [el for el in range(100, 1001, 2)]
print(f'Результат произведения всех четных чисел от 100 до 1000:\n{reduce(multiplication, new_list)}')
