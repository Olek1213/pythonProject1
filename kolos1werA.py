def zad3(nazwa_pliku):
    with open(nazwa_pliku) as plik:
        a = plik.readlines()
        lista = []
        lista_maks = []
        for i in range(len(a)):
            lista.append(a[i].split(' '))
        for i in range(len(lista[0])):
            kolumna = []
            for j in range(len(lista)):
                kolumna.append(lista[j][i])
            lista_maks.append(max(kolumna))
    return lista_maks


def main():
    print(zad3('liczby.txt'))


main()