import sys


def zad1():
    zdanie = input('Podaj zdanie: ')
    slowa = 1
    for i in zdanie:
        if i == ' ':
            slowa += 1
    return slowa


def zad2():
    sys.stdout.write('Podaj liczbę całkowitą: ')
    a = int(sys.stdin.readline())
    sys.stdout.write('Podaj liczbę całkowitą: ')
    b = int(sys.stdin.readline())
    sys.stdout.write('Podaj liczbę całkowitą: ')
    c = int(sys.stdin.readline())
    d = (a ** b) + c
    return d


def zad3():
    slowo = input('Podaj slowo: ')
    if slowo == slowo[::-1]:
        return 'Slowo jest palindromem'
    else:
        return 'Slowo nie jest palindromem'


def zad4():
    liczba = int(input('Podaj liczbę: '))
    czy_pierwsza = 1
    for i in range(2, liczba):
        if liczba % i == 0:
            czy_pierwsza = 0
    if czy_pierwsza == 1:
        return 'Liczba jest pierwsza'
    else:
        return 'Liczba nie jest pierwsza'


def zad5():
    ilosc = 0
    for i in range(1, 1001):
        suma = 0
        for j in range(1, i):
            if i % j == 0:
                suma += j
        if i == suma:
            ilosc += 1
    return ilosc


def zad6():
    lista = [1, 1.5, 2, 2.5, 3]
    for i in range(len(lista)):
        lista[i] = lista[i] ** 2
    return lista


def zad7():
    n = 0
    lista1 = []
    while n < 10:
        a = int(input('Podaj liczbę: '))
        lista1.append(a)
        n += 1
    lista2 = []
    for i in lista1:
        if i % 2 == 0:
            lista2.append(i)
    return lista2


def zad8():
    lista = [2, 'cos', 3, 'nic', 2, 'cos', 4]
    slownik = {}
    for i in lista:
        if i in slownik.keys():
            slownik[i] += 1
        else:
            slownik[i] = 1
    lista2 = []
    for i in slownik:
        if type(i) == int or type(i) == float:
            continue
        else:
            lista2.append(i)
    for i in lista2:
        del slownik[i]
    return slownik


def main():
    # print(f'Ilosc slow w podanym zdaniu wynosi {zad1()}')
    # print(f'a^b+c={zad2()}')
    # print(zad3())
    # print(zad4())
    # print(f'Liczb doskonalych mniejszych od 1001 jest {zad5()}')
    # print(zad6())
    # print(f'Liczby parzyste z podanych to: {zad7()}')
    print(zad8())

main()