import math
import random
# try:
#     a = int(input())
#     b = int(input())
#     result = a / b
#     print(result)
# except Exception:
#     print('Error')
# except ValueError:
#   print('Brak liczby')
# except ZeroDivisionError:
#   print('Error')
# else:
#   print(result)

# a = [x**2 for x in range(10)]
# print(a)
# l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# l2 = []
# for i in l1:
#    l2.append(i**2)
# print(l2)
# b = [3**y for y in range(6)]
# print(b)
# c = [x for x in a if x % 2 == 1]
# print(c)
# d = [(i, j) for i in l1 for j in l2]
# print(d)
#
# l3 = []
# for i in l1:
#     for j in l2:
#         l3.append((i,j))
# print(l3)
#
# s1 = {1:2, 2:3, 3:4}
# s2 = {v: k for k, v in s1.items()}
# print(s2)

# def rownanie_kwadratowe(a, b, c):
#     delta = b ** 2 - 4*a*c
#     if delta<0:
#         print('brak pierwiastkow')
#         return 0
#     elif delta == 0:
#         x = -b/(2*a)
#         print('jeden pierwiastek')
#         return x
#     elif delta > 0:
#         x1 = (-b + delta**(1/2))/(2*a)
#         x2 = (-b - delta**(1/2))/(2*a)
#         print('dwa pierwiastki')
#         return (x1,x2)
#
# print(rownanie_kwadratowe(a=6, b=1, c=3))
# print(rownanie_kwadratowe(a=1, b=2, c=1))
# print(rownanie_kwadratowe(a=1, b=4, c=1))

# def dlugosc_odcinka(x1=1, x2=2, y1=3, y2=4):
#     return math.sqrt((x2-x1)**2 + (y2-y1)**2)
#
# print(dlugosc_odcinka())
# print(dlugosc_odcinka(2,4,5,7))
# print(dlugosc_odcinka(x1=1,x2=5,y1=6,y2=7))

# plik = open('tekst.txt','r')
# plik.seek(0)
# znaki = plik.read(10)
# linia = plik.readline()
# linie = plik.readlines()
# plik.write('aaaa')
# plik.close()

# with open('tekst.txt','r') as plik:
#     znaki = plik.readlines()

# print('znaki')
def czy_prostokatny(a,b,c):
    if a>b and a>c:
        max = a
    if b>a and b>c:
        max = b
    if c>b and c>a:
        max = c
    if max == a:
        if b**2 + c**2 == a**2:
            print('Jest prostokatny')
            return 0
        else:
            print('Nie jest prostokatny')
            return 0
    if max == b:
        if a**2 + c**2 == b**2:
            print('Jest prostokatny')
            return 0
        else:
            print('Nie jest prostokatny')
            return 0
    if max == c:
        if b**2 + a**2 == c**2:
            print('Jest prostokatny')
            return 0
        else:
            print('Nie jest prostokatny')
            return 0


def pole_trapezu(a=1,b=1,h=1):
    pole = (a+b)*h/2
    return pole


def iloczyn_ciagu(a=1,b=4,ile=10):
    iloczyn = a
    for i in range(ile):
        iloczyn *= b
    return iloczyn


def main():
    A = {1-x for x in range(1,11)}
    B = {4**x for x in range(8)}
    C = {x for x in B if x % 2 == 0}
    lista1 = [random.randrange(1, 1000) for i in range(1,11)]
    lista2 = [x for x in lista1 if x % 2 == 0]
    slownik1 = {'ziemniak':'kg','ogorek':'sztuki','pomidor':'sztuki','marchewka':'kg'}
    slownik2 = {warzywo:jednostka for warzywo, jednostka in slownik1.items() if jednostka == 'sztuki'}
    try:
        x = float(input('Podaj liczbę: '))
        print(math.sqrt(x))
    except ValueError:
        print('Podano liczbe ujemną.')


main()

