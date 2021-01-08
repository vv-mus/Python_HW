class Matrix:
    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        return '\n'.join(map(str, self.lists))

    def __add__(self, other):
        m = []
        for i in range(len(self.lists)):
            m.append([])
            for j in range(len(self.lists[0])):
                m[i].append(self.lists[i][j] + other.lists[i][j])
        return Matrix(m)


matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
sum_matrix = matrix_1 + matrix_2
print(f'Матрица № 1:\n{matrix_1}')
print(f'Матрица № 2:\n{matrix_2}')
print(f'Результат сложения матриц:\n{sum_matrix}')
