#knygu kainu palyginimas

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from bs4 import BeautifulSoup
import requests
import psycopg2

# url = 'https://vaga.lt/grozine-literatura'
# response = requests.get(url)
# # print(response.status_code)
# soup = BeautifulSoup(response.content, 'html.parser')
# #pasitikrinti ar uzkrauna duomenis
# # print(soup) arba print(response.content)
#
# knygos_content = soup.find_all('div', class_ = 'product-item-container')
# # pavadinimas = soup.find_all('div', class_ ='lupa-search-results-product-title lupa-search-results-product-element')
# # autorius = soup.find_all('div', class_ = 'lupa-search-result-product-details-section')
# # kaina = soup.find_all('div', class_ = 'lupa-element-group-card-bottom')
# # print(knygos_content)
#
# knygu_sarasas = []
# for knygos in knygos_content:
#     pavadinimas = knygos.find('p', class_= 'name').text.strip()
#     kaina = float(knygos.find('div', class_ = 'price price-align-wrapper').text.strip('€').replace(',', '.'))
#     autorius = knygos.find('p', class_ = 'Autorius').text.strip()
#
#     knygu_sarasas.append((pavadinimas, kaina, autorius))
#
# #kad grazinti duomenis reikia sukurti dataframe su stulpeliais
# df = pd.DataFrame(knygu_sarasas, columns = ['Pavadinimas', 'Kaina', 'Autorius'])
# # print(df)
#
# #rasti didziausia ir maziausia kaina, vidurki, mediana
# max = np.max(df['Kaina'])
# min = np.min(df['Kaina'])
# vidurkis = np.mean(df['Kaina']).round(2)
# mediana = np.median(df['Kaina'])
# print(f'Kainu statistika: \n Maksimali kaina: {max}, \n Minimali kaina: {min}, \n Kainu vidurkis: {vidurkis}, \n Mediana: {mediana}')
#
# #atvaizduojame grafike
# sns.set(style = 'whitegrid')
# sns.histplot(data = df, x = 'Kaina', kde = True)
# plt.ylabel('Knygu skaicius')
# plt.show()

####
#2 uzd
# url = 'https://www.metacritic.com/browse/movie/'
# response = requests.get(url)
# print(response.status_code)
# soup = BeautifulSoup(response.content, 'html.parser')
# #pasitikrinti ar uzkrauna duomenis
# # print(soup) arba print(response.content)



