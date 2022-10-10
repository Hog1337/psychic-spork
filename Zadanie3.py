import numpy as np
import timeit as ti
import copy

def minor(a, i, j):
    m = list(copy.deepcopy(a))
    del m[i]
    for i in range(len(a[0]) - 1):
        del m[i][j]
    return m

def invmat(a):
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(len(a)):
        for j in range(len(a[0])):
            tmp = minor(a, i, j)
            result[i][j] = (-1)**(i+j) * np.linalg.det(tmp) / np.linalg.det(a)
    return result

def transpose(razmer, a):
    n = int(razmer[2])
    trans_a = [[0 for j in range(len(a))] for i in range(len(a[0]))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            trans_a[j][i] = a[i][j]
    return trans_a


a = []
i, j, k = 3, 3, 0
while k < i:
    print('введите строку')
    a1 = list(map(int, input().split(" ")))
    if len(a1) > j:
        print('Длинна строки не может быть больше заданного размера')
        print('введите строку')
        a1 = list(map(int, input().split(" ")))
    k += 1
    a.append(a1)
mat = a
transMatrix = transpose('3x3', mat)
start_time = ti.default_timer()
a = invmat(transMatrix)
time1 = ti.default_timer() - start_time

start_time = ti.default_timer()
    b = np.linalg.inv(mat)
time2 = ti.default_timer() - start_time

print('Функция', time1)
print('Numpy', time2)