# 1 UZDUOTIS, 09.21
# Apskaičiuokite kiekvieno produkto mėnesinį pardavimų sumažėjimą per metus.
# Sukurkite Matplotlib grafiką, kuriame būtų pateikti šie mėnesiniai sumažėjimai kiekvienam produktui (x ašis - mėnesiai, y ašis - sumažėjimas, produkto pavadinimas - linijos pavadinimas).
# Pridėkite pavadinimus ašims ir bendrą pavadinimą grafikui.


import pandas as pd
import matplotlib as pdb
import matplotlib.pyplot as plt
# data = pd.read_csv('/Users/kamila/Downloads/prekybos_duomenys.csv')
# df = pd.DataFrame(data)
# print(df)
#
# df['Data'] = pd.to_datetime(df['Data'])
# df['Metai'] = df['Data'].dt.year
# df['Menuo'] = df['Data'].dt.month
# df['Diena'] = df['Data'].dt.day
#
# pagal_produkta = df.groupby(['Menuo', 'Produktas'])['Pardavimai'].sum()
# print(pagal_produkta)
#
# products = df['Produktas']
# result = pd.DataFrame(columns = ['Produktas', 'Metai', 'Menuo', 'Sumazejimas'])
# for product in products:
#     product_df = df[df['Produktas'] == product]
#     for year in product_df['Metai'].unique():
#         for month in range(1,13):
#             if product_df[(product_df['Metai'] == year ) & (product_df['Menuo'] == month)].shape[0] > 0:
#                 sales = product_df[(product_df['Metai'] == year ) & (product_df['Menuo'] == month)]['Pardavimai'].sum()
#                 if month > 1:
#                     previous_year = year
#                     previous_month = month - 1
#                 else:
#                     previous_year = year - 1
#                     previous_month = 12
#                 previous_sales = \
#                 product_df[(product_df['Metai'] == [previous_year]) & (product_df['Menuo'] == previous_month)]['Pardavimai'].sum()
#                 decrease = [previous_sales - sales]
#                 result = pd.concat([result, pd.DataFrame([[product, year, month, decrease]], columns = result.columns)], ignore_index = True)
# print(result)
#
# plt.plot(result['Produktas'], result['Sumazejimas'], label='linija', color='blue', linestyle ='--', marker = 'o')
# plt.xticks(rotation=90)
# plt.legend()
# plt.xlabel('Mėnesiai')
# plt.ylabel('sumažėjimas')
# plt.title('Pardavimų mažėjimas')
# plt.show()

# 2 UZDUOTIS
# Išspausdinkite pirmas 5 eilutes;
# Filtruokite automobilius pagal jų kainą (pvz., kaina mažesnė nei 10 000). Išspausdinkite šiuos automobilius;
# Suskirstykite automobilius pagal gamintoją ir susumuokite kiekvieno gamintojo automobilių kiekius.
# Atvaizduokite stulpelinėje diagramoje automobilių kiekius;

# data = pd.read_csv('/Users/kamila/Downloads/automobiliai.csv')
# df = pd.DataFrame(data)
# print(df.head(5))

# 3 UZDUOTIS
# URL: https://coinmarketcap.com
# Naudokite Beautiful Soup, kad galėtumėte „web scraping" funkcionalumą, kad gautumėte kriptovaliutos kainų duomenis iš populiarios kriptovaliutų rinkos svetainės.
# Išgaukite kainų, laiko ir kitus susijusius duomenis iš svetainės.
# Įkelkite gautus duomenis į Pandas DataFrame.
# Atliekant duomenų tvarkymą, galite konvertuoti datą į tinkamą formatą, ištrinti dublikatus arba tvarkyti trūkstamas reikšmes.
# Atlikite analizę, kad gautumėte statistiką apie kriptovaliutos kainų kitimą.
# Paskaičiuokite vidutines, minimalias ir maksimalias kainas, taip pat kitas statistikos vertes.
# Sukurkite linijinį grafiką, kuris atvaizduoja kriptovaliutos kainos kitimą laike (x ašis - laikas, y ašis - kaina).
# Taip pat galite sukurti stulpelinį grafiką, kuris rodo kainos svyravimus tarp skirtingų kriptovaliutų.

# from bs4 import BeautifulSoup
# import requests
# import pandas as pd
# import psycopg2
# url = 'https://coinmarketcap.com'
# response = requests.get(url)
# print(response.status_code)
#
#     soup = BeautifulSoup(response.content, 'html.parser')
#     #imame visus elementus is bloko, kuriame yra produktai
#     product_elements = soup.find_all('div', class_='GRID_ITEM')
#     print(product_elements)

# NUMPY
import numpy_biblioteka as np
# masyvas = np.array([1,2,3,4,5])
# masyvas2 = np.array([6,2,9,4,7])
# suma = np.sum(masyvas)
# vidurkis = np.mean(masyvas)
# # print(f'Suma: {suma}, vidurkis: {vidurkis}')
# mediana = np.median(masyvas)
# st_nuokrypis = np.std(masyvas)
# print(f'Mediana: {mediana}, standartinis nuokrypis: {st_nuokrypis}')
# min = np.min(masyvas)
# max = np.max(masyvas)
#
# suma2 = masyvas + masyvas2
# print(suma2)

#MATRICA
# matrica = np.array([[1,2,3], [4,5,6], [7,8,9]])
# print(matrica)
#
# sum = np.sum(matrica)
# print(sum)

# matrica = np.random.randint(1,11, (4,4))
# print(matrica)
# vidurkis = np.mean(matrica)
# print(vidurkis)
# vidurkis_matricos_stulpeliu = np.mean(matrica, axis=0) #axis 0 yra stulpelis, 1 yra eilute
# vidurkis_matricos_eiluciu = np.mean(matrica, axis=1)
# print(vidurkis_matricos_stulpeliu, vidurkis_matricos_eiluciu)

# studentu_pazymiai = np.array([[7, 8, 9], [6, 4, 10], [10, 9, 10], [8, 8, 7]])
# #vidurkis kiekvieno studento
# studentu_vidurkiai = np.mean(studentu_pazymiai, axis = 1).round(2)
# medianos = np.median(studentu_pazymiai, axis = 1)
# print(f'Studentu vidurkiai: {studentu_vidurkiai}, medianos: {medianos}')
#
# for i in range(len(studentu_vidurkiai)):
#     print(f'Studentas {i+1}: vidurkis {studentu_vidurkiai[i]}, mediana: {medianos[i]}')
#

#arg nurodo vietos indeksa
# masyvas3 = np.random.randint(1,51,(1,1))
# max_sk = np.argmax(masyvas3)
# min_sk = np.argmin(masyvas3)
# print(masyvas3, '\n', max_sk, min_sk)

# masyvas = np.array([1, 2, 3, 4, 5])
# daugiau_uz_tris = masyvas[masyvas > 3]
# print(daugiau_uz_tris)
