import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# plt.plot([1, 2, 3, 4])
# plt.ylabel('jakies liczby')
# plt.show()

# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro-')
# plt.axis((0, 6, 0, 20))
# plt.show()

# t = np.arange(0., 5., 0.2)
# plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
# plt.legend(labels=['liniowa', 'kwadratowa', 'szescienna'])
# plt.show()

# x = np.arange(0, 10, 0.1)
# s = np.sin(x)
#
# plt.plot(x, s, label='sin(x)')
# plt.xlabel('x')
# plt.ylabel('sin(x)')
# plt.title('Wykres sin(x)')
# plt.legend()
# plt.show()

# data = {'a': np.arange(50),
#         'c': np.random.randint(0, 50, 50),
#         'd': np.random.randn(50)}
# data['b'] = data['a'] + 10 * np.random.randn(50)
# data['d'] = np.abs(data['d']) * 100
# plt.scatter('a', 'b', c='c', s='d', data=data)
# plt.xlabel('wartosc a')
# plt.ylabel('wartosc b')
# plt.show()


def main():
    # zad 1
    # x1 = np.arange(1, 20, 1)
    # plt.plot(x1, 1/x1, 'b-', label='1/x')
    # plt.xlabel('x')
    # plt.ylabel('f(x)')
    # plt.axis((1, 20, 0, 1))
    # plt.legend()
    # plt.show()

    # zad 2
    # x2 = np.arange(1, 20, 1)
    # plt.plot(x2, 1 / x2, 'g>:', label='f(x) = 1/x')
    # plt.xlabel('x')
    # plt.ylabel('f(x)')
    # plt.axis((0, 20, 0, 1))
    # plt.title('Wykres funkcji f(x) dla x [1, 20]')
    # plt.legend()
    # plt.show()

    # zad 3
    # x3 = np.arange(0., 30., 0.1)
    # plt.plot(x3, np.sin(x3), 'b-', label='sin(x)')
    # plt.plot(x3, np.cos(x3), 'r-', label='cos(x)')
    # plt.xlabel('x')
    # plt.ylabel('f(x)')
    # plt.legend()
    # plt.show()

    # zad 4
    # a = pd.read_csv('iris.data', sep=',')
    # print(a)
    # data = {'a': a['5.1'], 'b': a['3.5']}
    # data['c'] = np.random.randint(0, 50, 149)
    # data['d'] = np.abs(data['a']-data['b'])
    # plt.scatter('a','b', c='c', s='d', data=data)
    # plt.show()

    # zad 5
    plik = pd.ExcelFile('imiona.xlsx')
    imiona = pd.read_excel(plik)
    plt.subplot(1,3,1)
    wykres1 = imiona.groupby(['Plec']).agg({'Liczba': ['sum']})
    etykiety = ['K', 'M']
    wartosci = list(wykres1.agg('Liczba').sum())
    plt.bar(x=etykiety, height=wartosci, color=['red', 'blue'])
    plt.xlabel('Plec')
    plt.ylabel('Liczba')
    plt.subplot(1,3,2)
    wykres2_m = imiona[imiona['Plec'] == 'M'].groupby(['Rok']).agg({'Liczba': 'sum'})
    wykres2_k = imiona[imiona['Plec'] == 'K'].groupby(['Rok']).agg({'Liczba': 'sum'})
    plt.plot(wykres2_m.index.values, wykres2_m['Liczba'], 'b-', label='mezczyzni')
    plt.plot(wykres2_k.index.values, wykres2_k['Liczba'], 'r-', label='kobiety')
    plt.legend()
    plt.xlabel('Rok')
    plt.subplots_adjust(wspace=0.6)
    plt.subplot(1,3,3)
    wykres3 = imiona.groupby(['Rok']).agg({'Liczba': 'sum'})
    etykiety3 = wykres3.index.values
    wartosci3 = list(wykres3['Liczba'])
    plt.bar(x=etykiety3, height=wartosci3, color='blue')
    plt.xlabel('Rok')
    plt.show()




main()
