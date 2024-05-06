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
    popularne_imiona = df1.groupby(['Rok', 'Plec', 'Imie']).agg({'Liczba': 'sum'}).groupby(['Rok', 'Plec']).agg({'Liczba': 'max'})
    print(popularne_imiona)
    for i in range(2000, 2018, 1):
        liczba1 = popularne_imiona['Liczba'].where(('Rok' == i) & ('Plec' == 'K'))
        liczba2 = popularne_imiona['Liczba'].where(('Rok' == i) & ('Plec' == 'M'))
        print(df1[(df1.Rok == i) & (df1.Liczba == liczba1)])
        print(df1[(df1.Rok == i) & (df1.Liczba == liczba2)])




main()
