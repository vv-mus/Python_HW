from random import randint


rand_list = [randint(0, 10) for i in range(10)]
new_list = [el for el in rand_list if rand_list.count(el) == 1]
print(f'Исходный список: {rand_list}')
print(f'Новый список: {new_list}')
