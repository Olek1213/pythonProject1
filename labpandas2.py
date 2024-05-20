import pandas as pd
import numpy as np

def main():
    # zad1
    imiona = pd.ExcelFile('imiona.xlsx')
    df1 = pd.read_excel(imiona)
    print(df1)

    # zad2
    print(df1[df1['Liczba'] > 1000])
    print(df1[df1['Imie'] == 'ALEKSANDER'])
    print(df1.groupby(['Rok']).agg({'Liczba': ['sum']}))
    print(df1[(df1.Rok >= 2000) & (df1.Rok <= 2005)])
    print(df1.groupby(['Plec']).agg({'Liczba': ['sum']}))

    popularne_imiona = df1.groupby(['Rok', 'Plec']).agg({'Liczba': 'max'})
    for i in range(18):
        liczba1 = int(popularne_imiona.iloc[2*i])
        liczba2 = int(popularne_imiona.iloc[2*i+1])
        print(f'{2000 + i} {str(df1[df1.Liczba == liczba1]['Imie'])}')
        print(f'{2000 + i} {str(df1[df1.Liczba == liczba2]['Imie'])}')

    # zad3
    zamowienia = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal='.')
    print(zamowienia)
    print(zamowienia.groupby(['Sprzedawca']).agg({'Utarg': ['count']}))
    print(zamowienia.sort_values(by='Utarg', ascending=False).head(5))
    print(zamowienia.groupby(['Sprzedawca']).agg({'idZamowienia': ['count']}))
    print(zamowienia.groupby(['Kraj']).agg({'idZamowienia': ['count']}))
    print(zamowienia)
    zamowienia2 = zamowienia
    zamowienia2['Rok'] = zamowienia2['Data zamowienia'].astype(str).str[0:4]
    print(zamowienia2[(zamowienia2.Kraj == 'Polska') & (zamowienia2.Rok == '2005')].agg('idZamowienia').count())
    print(zamowienia2[zamowienia2.Rok == '2004'].agg('Utarg').mean())
    zamowienia2004 = zamowienia2[zamowienia2.Rok == '2004']
    zamowienia2004.to_csv('zamowienia_2004', index=False)
    zamowienia2005 = zamowienia2[zamowienia2.Rok == '2005']
    zamowienia2005.to_csv('zamowienia_2005', index=False)


main()
