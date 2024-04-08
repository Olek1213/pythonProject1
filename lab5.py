import numpy as np

# a = np.array([0, 1])
# print(a)
#
# a = np.arange(2)
# print(a)
# print(type(a))
#
# print(a.dtype)
# a = np.array(['a', 'b', 'c', 1, 2, 3])
# print(a)
# print(a.dtype)

# b = a.astype('float')
# print(b)
# print(b.dtype)
# print(b.shape)

# m = np.array((np.arange(2), np.arange(2)))
# print(m)
# print(m.shape)
#
# zera = np.zeros((5, 5))
# jedynki = np.ones((4, 4))
# print(zera)
# print(jedynki)
# print(zera.dtype)
# print(jedynki.dtype)
#
# pusta = np.empty((2, 2))
# print(pusta)
# poz_1 = pusta[1, 1]
# poz_2 = pusta[0, 1]
# print(poz_1)
# print(poz_2)
#
# liczby = np.arange(1, 2, 0.1)
# print(liczby)
#
# liczby_lin = np.linspace(1, 2, 5, endpoint=False)
# print(liczby_lin)

# z = np.indices((5, 3))
# print(z)
# print(z.shape)
# print(z[0, 2, 1])

# x, y = np.mgrid[0:5, 0:5]
# print(x)
# print(y)

# mat_diag_k = np.diag([a for a in range(5)], -1)
# print(mat_diag_k)

# z = np.fromiter(range(5), dtype='int32')
# print(z)
#
# znaki = b'abcdef'
# zn1 = np.frombuffer(znaki, dtype='S1')
# print(zn1)
# zn2 = np.frombuffer(znaki, dtype='S2')
# print(zn2)

# znaki = 'abcdef'
# zn3 = np.array(list(znaki))
# zn4 = np.array(list(znaki), dtype='S1')
# zn5 = np.array(list(b'abcdef'))
# zn6 = np.fromiter(znaki, dtype='S1')
# zn7 = np.fromiter(znaki, dtype='U1')
# print(zn3)
# print(zn4)
# print(zn5)
# print(zn6)
# print(zn7)

# mat = np.ones((2, 2))
# mat_1 = np.ones((2, 2))
# mat = mat + mat_1
# print(mat)
# print(mat - mat_1)
# print(mat*mat_1)
# print(mat/mat_1)
# mat_1 = np.array([[4, 5], [6, 3]])
# print(mat*mat_1)
# print(mat/mat_1)

# a = np.arange(10)
# print(a)
# s = slice(2, 7, 2)
# print(a[s])
# s = range(2, 7, 2)
# print(a[s])
# print(a[2:7:2])
# print(a[1:])
# print(a[2:5])

# mat = np.arange(25)
#
# mat = mat.reshape((5, 5))
#
# print(mat[1:])
# print(mat[:, 1])
# print(mat[:, -1:])
# print(mat[2:5, 1:3])
# print(mat[:, range(2, 6, 2)])
# print('')

# x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
# print(x)
# rows = np.array([[0, 0], [3, 3]])
# cols = np.array([[0, 2], [0, 2]])
# y = x[rows, cols]
# print(y)

def zad3(n):
    a = np.arange(1, n*n+1)
    return a.reshape(n, n)


def zad4(podstawa, ile):
    a = np.logspace(base=podstawa, start=1, stop=ile, num=ile, dtype='int32')
    return list(a)


def zad5(dlugosc):
    a = np.arange(dlugosc)
    a = a[::-1]
    return np.diag(a)


def zad7(n):
    tablica = np.diag([2 for a in range(n)])
    for i in range(1,n):
        tablica += np.diag([2*(i+1) for a in range(n-i)],i)
        tablica += np.diag([2 * (i+1) for a in range(n - i)],-1*i)
    return tablica


def zad8(tablica,kierunek):
    w = np.shape(tablica)[0]
    k = np.shape(tablica)[1]
    if kierunek == '-':
        if w % 2 == 1:
            print('Nie mozna podzielic')
        else:
            return tablica[:int(w/2),:], tablica[int(w/2):,:]
    if kierunek == '|':
        if k % 2 == 1:
            print('Nie mozna podzielic')
        else:
            return tablica[:,:int(k/2)], tablica[:,int(k/2):]


def zad9():
    fibonacci = []
    fibonacci.append(1)
    fibonacci.append(1)
    for i in range(23):
        fibonacci.append(fibonacci[-1]+fibonacci[-2])
    return np.reshape(fibonacci,(5,5))


def main():
    a = np.arange(0, 45, 3)
    print(a)

    lista = [1.2, 2.3, 3.4, 4.5]
    print(np.array(lista, dtype='int64'))

    print(zad3(4))

    print(zad4(2,4))

    print(zad5(5))

    napis1 = np.array(list('pies'))
    napis2 = np.array(list('ptak'))
    napis3 = np.array(list('pole'))
    wykreslanka = np.diag(napis3)
    wykreslanka[0,:]=napis1
    wykreslanka[:,0] = napis2
    print(wykreslanka)

    # print(zad7(3))
    # print(zad9())
    a = np.array([[1,2],[3,4],[5,6],[7,8]])
    print(a)
    print(zad8(a,'-'))


main()
