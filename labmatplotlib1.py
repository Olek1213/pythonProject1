import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ts = pd.Series(np.random.randn(1000))
# ts = ts.cumsum()
# print(ts)
# ts.plot()
# plt.show()

# data = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],
#         'Stolica': ['Bruksela', 'New Delhi', 'Brasilia', 'Warszawa'],
#         'Kontynent': ['Europa', 'Azja', 'Ameryka Południowa', 'Europa'],
#         'Populacja': [11190846, 1303171035, 207847528, 39675467]}
# df = pd.DataFrame(data)
# print(df)
#
# grupa = df.groupby(['Kontynent']).agg({'Populacja': ['sum']})
# print(grupa)
# # grupa.plot(kind='bar', xlabel='Kontynent', ylabel='Mld', legend=True, title='Populacja z podziałem na kontynenty')
# wykres = grupa.plot.bar()
# wykres.set_ylabel('Mld')
# wykres.set_xlabel('Kontynent')
# wykres.tick_params(axis='x', labelrotation=0)
# wykres.legend()
# wykres.set_title('Populacja z podziałem na kontynenty')
# # plt.xticks(rotation=0)
# plt.savefig('wykres.png')
# plt.show()

# df = pd.read_csv('dane.csv', header=0, sep=';', decimal='.')
# print(df)
# grupa = (df.groupby(['Imię i nazwisko']).
#          agg({'Wartość zamówienia': ['sum']}))
# grupa.plot(kind='pie', subplots=True, autopct='%.2f %%',
#            fontsize=20, figsize=(6, 6), colors=['red', 'green'])
# # wykres = grupa.plot.pie(subplots=True, autopct='%.2f %%',
# # fontsize=20, figsize=(6, 6))
# plt.legend(loc='lower right')
# plt.title('Suma zamówienia dla sprzedawcy')
# plt.show()

# ts = pd.Series(np.random.randn(1000))
# ts = ts.cumsum()
#
# df = pd.DataFrame(ts, columns=['wartości'])
# print(df)
#
# df['Średnia krocząca'] = df.rolling(window=50).mean()
# df.plot()
# plt.legend()
# plt.show()

def main():
    df1 = pd.ExcelFile('imiona.xlsx')
    imiona = pd.read_excel(df1)
    print(imiona)

    # zad1
    imiona1 = imiona.groupby(['Rok']).agg({'Liczba': ['sum']})
    imiona1.plot(kind='line', title='Liczba urodzonych dzieci dla kazdego roku')
    plt.show()

    # zad2
    imiona2 = imiona.groupby(['Plec']).agg({'Liczba': ['sum']})
    imiona2.plot(kind='bar')
    plt.show()

    # zad3
    imiona3 = imiona[(imiona.Rok >= 2013)].groupby(['Plec']).agg({'Liczba': 'sum'})
    imiona3.plot(kind='pie', subplots=True)
    plt.show()

    # zad4
    zamowienia = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal='.')
    zamowienia1 = zamowienia.groupby(['Sprzedawca']).agg({'idZamowienia': ['count']})
    zamowienia1.plot(kind='bar')
    plt.show()




main()
