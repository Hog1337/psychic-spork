import copy
def minor(a, i, j):
    m = copy.deepcopy(a)
    del m[i]
    for i in range(len(a[0]) - 1):
        del m[i][j]
    return m

def matrix_transpon(razmer, a):
    n = int(razmer[2])
    trans_a = [[0 for j in range(len(a))] for i in range(len(a[0]))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            trans_a[j][i] = a[i][j]
    return trans_a

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

def matrix_multiply(a, b):
    length = len(a)
    c = [[0 for i in range(length)] for i in range(length)]
    for i in range(length):
        for j in range(length):
            for k in range(length):
                c[i][j] += a[i][k] * b[k][j]
    return c


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
    mat = matrix_input(razmer)
    mat_trans = matrix_transpon(razmer, mat)
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
    i = 0
    while i < len(a) - 1:
        print(a[i], a[i + 1])
        i += 2
    y = int(input())
    razmer = razmery[y]
    mat2 = matrix_input(razmer)

    result = matrix_multiply(mat1, mat2)
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
    for i in c: print(i)
    if razmer=='2x2':
        det = c[0][0]*c[1][1] - c[0][1]*c[1][0]
        if det!=0:
            rank = 2
        else:
            for l in '123456789':
                if l in c:
                    rank = 1
                    break
                else:
                    rank = 0

    elif razmer=='3x3':
        det = c[0][0] * c[1][1] * c[2][2] + c[0][1] * c[1][2] * c[2][0] + c[0][2] * c[1][0] * c[2][1] \
        - c[0][2] * c[1][1] * c[2][0] - c[0][0] * c[1][2] * c[2][1] - c[0][1] * c[1][0] * c[2][2]
        if det!=0: rank = 3
        else:
            for i in range(3):
                for j in range(3):
                    m = minor(c, i, j)
                    det = m[0][0] * m[1][1] - m[0][1] * m[1][0]
                    if det!=0:
                        rank = 2
                        break
                    else:
                        for k in '123456789':
                            if k in c:
                                rank = 1
                                break
                            else: rank = 0
    print(rank)