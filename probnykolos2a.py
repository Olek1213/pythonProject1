import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
    # zad 1
    # x = np.arange(10)
    # plt.plot(x, (x**2 + 4)/(2**x), label='f(x)=(x^2+4)/(2^x)')
    # plt.xlabel('x')
    # plt.ylabel('f(x)')
    # plt.title('Wykres funkcji f(x)')
    # plt.legend()
    # plt.show()

    # zad 2
    # plt.subplot(1,3,1)
    # x1 = np.linspace(-3,3,100)
    # y1 = x1 ** 2 + 5
    # plt.plot(x1, y1, label='x^2+5')
    # plt.xlabel('x')
    # plt.xlim(-3,3)
    # plt.xticks((-3,0,3))
    # plt.ylabel('wartości funkcji')
    # plt.title('wykres funkcji f(x)=x^2+5')
    # plt.legend(loc='upper center')
    # plt.subplot(1,3,3)
    # x2 = np.linspace(-3,3,60)
    # y2_1 = x2 ** 2 + 5
    # y2_2 = -1 * x2 ** 2 + 4 * x2
    # plt.plot(x2, y2_1, 'ro', label='x^2+5')
    # plt.plot(x2, y2_2, 'go', label='-x^2+4x')
    # plt.xlim(-3,3)
    # plt.xticks((-3, 0, 3))
    # plt.xlabel('x')
    # plt.ylabel('wartości funkcji')
    # plt.title('wykres dwóch funkcji')
    # plt.legend(loc='lower right')
    # plt.savefig('Aleksander_Luty_zad2.png')
    # plt.show()

    # zad 3
    # plik = pd.read_csv('automobile.csv',sep=';')
    # punkt1 = plik.sample(n=100, replace=False)
    # print(punkt1)
    # punkt2 = punkt1.groupby(['Car model']).agg({'Price': ['mean']})
    # print(punkt2)
    # punkt2.plot(kind='pie', subplots=True, autopct='%.0f %%', fontsize=14, legend=False)
    # plt.title('Srednie ceny samochodow')
    # plt.show()

    # zad 4
    plik = pd.read_csv('automobile.csv', sep=';')
    ceny = plik.groupby(['Car model']).agg({'Price': ['mean']})
    ceny.plot(kind='bar', xlabel='Marki samochodow', ylabel='Srednia cen', legend=False, )
    plt.title('Srednie ceny samochodow')
    plt.show()


main()