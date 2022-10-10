def matrix_input(razmer):
    #j - колво строк i - столбцов
    a = []
    i, j, k = int(razmer[0]), int(razmer[2]), 0
    while k<i:
        print('введите строку')
        a1 = list(map(int, input().split(" ")))
        if len(a1)>j:
            print('Длинна строки не может быть больше заданного размера')
            print('введите строку')
            a1 = list(map(int, input().split(" ")))
        k+=1
        a.append(a1)
    return a

from numpy import *

razmery = {1:'1x2', 2: '2х1', 3: '1х3', 4 : '3х1', 5: '2х2', 6: '3х3'}
print('Выберите функцию:')
a = ['1. Транспонирование', '2. Умножение', '3. Определение ранга']
for i in a: print(i)
x = int(input())
if x == 1:
    print('Выберите размер матрицы:')
    a = ['1', '1x2', '2','2х1', '3','1х3', '4','3х1', '5','2х2', '6','3х3']
    i = 0
    while i<len(a)-1:
        print(a[i], a[i+1])
        i+=2
    y = int(input())
    razmer = razmery[y]
    mat = array(matrix_input(razmer))
    mat_trans = mat.transpose()
    for i in mat_trans: print(i)

if x == 2:
    print('Выберите размер матрицы:')
    a = ['1', '1x2', '2', '2х1', '3', '1х3', '4', '3х1', '5', '2х2', '6', '3х3']
    i = 0
    while i<len(a)-1:
        print(a[i], a[i+1])
        i+=2
    y = int(input())
    razmer = razmery[y]
    mat1 = matrix_input(razmer)
    print('Выберите размер матрицы:')
    a = ['1', '1x2', '2', '2х1', '3', '1х3', '4', '3х1', '5', '2х2', '6', '3х3']
    y = int(input())
    i = 0
    while i < len(a) - 1:
        print(a[i], a[i + 1])
        i += 2
    razmer = razmery[y]
    mat2 = matrix_input(razmer)

    result = matmul(mat1, mat2)
    for i in result: print(i)

if x == 3:
    print('Выберите размер матрицы:')
    a = ['1', '2х2', '2', '3х3']
    i = 0
    while i<len(a)-1:
        print(a[i], a[i+1])
        i+=2
    y = int(input())
    razmer = '2x2' if y==1 else '3x3'
    c = matrix_input(razmer)
    rank = linalg.matrix_rank(c)
    print(rank)