import math
import random


def zad1():
    print(round((math.e ** 4 - math.log2(34)) ** (1/3),2))
    print(round((math.log(20,math.e) + math.cos(45) + math.e) ** (1/3),2))
    print(round((math.log(20,3) + math.sin(45) * (5/8)) ** (1/4),2))
    print(round(math.log(23,3) + (math.sin(34) + 5) ** (1/3),2))
    print(round((math.log2(32) + math.pi + math.sin(56)) ** (1/4),2))


def zad2(n):
    if n <= 10:
        for i in range(1,n+1):
            print('A' * i)
            print('\n')
    else:
        print('Za wysoka wieza')


def zad3(n):
    if n <= 10:
        for i in range(1,n+1):
            print(end=" " * (n-i))
            print('A' * (2*i-1))
            print('\n')
    else:
        print('Za wysoka pyramida')


def zad5(n):
    lista = []
    for i in range(n):
        lista2 = []
        for j in range(n):
            lista2.append(random.randrange(0,100))
        lista.append(lista2)
    for i in range(len(lista)):
        print(sum(lista[i]))

def main():
    zad5(4)


main()