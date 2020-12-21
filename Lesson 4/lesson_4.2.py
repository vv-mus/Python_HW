from random import randint


rand_list = [randint(-1000, 1000) for i in range(10)]
new_list = [rand_list[el] for el in range(1, len(rand_list)) if rand_list[el] > rand_list[el - 1]]
print(f'Исходный список: {rand_list}')
print(f'Новый список: {new_list}')
