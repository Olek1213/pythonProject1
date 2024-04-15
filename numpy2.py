import numpy as np


def zad1():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    c = np.array([0, 0, 0])
    for i in range(len(a)):
        c[i] = a[i]*b[i]
    return c


def zad2():
    a = np.arange(9).reshape((3, 3))
    b = np.arange(16).reshape((4, 4))
    print(a)
    print(a.min(axis=0))
    print(a.min(axis=1))
    print(b)
    print(b.min(axis=0))
    print(b.min(axis=1))
    return ''


def zad3():
    a = np.array([[1, 2, 3]])
    b = np.array([[4, 5, 6]])
    if np.shape(a)[1] == np.shape(b)[0]:
        return a.dot(b)
    else:
        return 'Nie mozna obliczyc iloczynu tych tablic'


def zad4():
    a = np.array([1, 2, 3])
    b = np.array([1.2, 2.3, 3.4])
    c = np.array([a[i]*b[i] for i in range(len(a))])
    return c


def zad5():
    x = np.array([[1, 2, 3], [4, 5, 6]])
    a = np.sin(x)
    return a


def zad6():
    x = np.array([[10, 11, 12], [13, 14, 15]])
    b = np.cos(x)
    return b


def zad7():
    return zad5()+zad6()


def zad8():
    x = np.arange(9).reshape((3, 3))
    for i in range(np.shape(x)[0]):
        print(f'{i+1} rzad = {x[i, :]}')
    return ''


def zad9():
    x = np.arange(9).reshape((3, 3))
    for i in x.flat:
        print(i)
    return ''


def zad10():
    a = np.arange(81).reshape((9, 9))
    return a.reshape((3, 27))
    # Mozliwe rozmiary to pary liczb calkowitych, ktorych iloczyn jest rowny 81


def zad11():
    x = np.arange(12)
    a = x.reshape((3, 4))
    b = x.reshape((4, 3))
    c = x.reshape((2, 6))
    for i in a.flat:
        print(i)
    print(' ')
    for i in b.flat:
        print(i)
    print(' ')
    for i in c.flat:
        print(i)
    return ''
def main():
    print(zad1())
    print(zad2())
    print(zad3())
    print(zad4())
    print(zad5())
    print(zad6())
    print(zad7())
    print(zad8())
    print(zad9())
    print(zad10())
    print(zad11())


main()

