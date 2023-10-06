# #09-18
# from bs4 import BeautifulSoup
# import requests
# import pandas as pd
# import psycopg2
#
# #duomenis perkeliame i duomenu baze
# def create_and_insert_product():
#     connection = psycopg2.connect(
#         host="localhost",
#         port=5432,
#         database="varleproducts",
#         user="postgres",
#         password="gulbiu12"
#     )
#
#     #kursorius pasiema connectiona
#     cursor = connection.cursor()
#     create_table_query = """
#         CREATE TABLE IF NOT EXISTS varle_products (
#         id SERIAL PRIMARY KEY,
#         name VARCHAR(255),
#         price DECIMAL(10,2),
#         quantity INT)
#     """
#
#     # cursor.execute(create_table_query)
#     # print("Table created successfully!")
#      connection.commit() - gal reikes sito ir cia
#1 step isitikinti ar gauname tinkama rezultata (turi buti 200)
#     url = 'https://www.varle.lt/nesiojami-kompiuteriai/nesiojami-kompiuteriai/'
#2 step
#     response = requests.get(url)
#3 step
#     # print(response.status_code)
#
#     soup = BeautifulSoup(response.content, 'html.parser')
#     #imame visus elementus is bloko, kuriame yra produktai
#     product_elements = soup.find_all('div', class_='GRID_ITEM')
#     print(product_elements)
#
# #sukuriame clean sarasa, i kuri desime produktus (be div, li zymu ir tt)
# #imame kiekvieno produkto elementa (pavadinima, kaina, kieki)
#     product_data = []
#     for product_element in product_elements:
# #sukuriame naujus kintamuosius
#         product_name = product_element.find('div', class_='product-title').text.strip()
#         product_price = float(product_element.find('span', class_='price-value').text.strip().replace('€', ''))
#         product_quantity = product_element.find('b').text.strip()[:1]
#     # print(f"Adding products to the list: {product_name}")
#     #     product_data.append((product_name, product_price, product_quantity))
#     #     insert_query="INSERT INTO varle_products (name, price, quantity) VALUES (%s, %s, %s)"
#     #     cursor.execute(insert_query, (product_name, product_price, product_quantity))
#     # print("Products inserted into the list successfully!")
#
#     #connection commit reikalingas kad atsirastu duomenys (lentele) duomenu bazeje
#       connection.commit()
#
# #aprasome stulpelius
#     select_query = "SELECT * FROM varle_products"
#     cursor.execute(select_query)
#     rows = cursor.fetchall()
#     df = pd.DataFrame(rows, columns=['id', 'name', 'price', 'quantity'])
#     print(df)
#
# if __name__ == '__main__':
#     create_and_insert_product()

#09-19
from bs4 import BeautifulSoup
import requests
import pandas as pd
import psycopg2
#
# #savaites dienos ir temperaturos
# url = 'http://www.meteo.lt/en/miestas?placeCode=Vilnius'
# response = requests.get(url)
# print(response.status_code)
#
# #objektas
# soup = BeautifulSoup(response.content, 'html.parser')
#
# forecast = soup.find_all('div', class_='forecast-day')
# week_days = soup.find_all('span', class_='date')
# day_temperature = soup.find_all('span', class_='big up-from-zero')[1::2] #ima kas antra temp, t.y. tik dienos temperatura
# # print(week_days, day_temperature) - pasitikrinimas
# #filtruojame tik savaites dienas
# filtered_week_days = [week_day.get_text().split(',')[0] for week_day in week_days] #skiriame kableliu
# #filtruojame temperaturas
# day_temperatures = []
# for temperature in day_temperature:
#     temp_text = temperature.get_text().replace('°C', '')
#     temp_value = int(temp_text[:-1]) #-1 reiskia kad nuo galo imtu
#     day_temperatures.append(temp_value)
# print(day_temperatures)
#
# #is gautu duomenu pasidarome dataframe
# #weekday - raktas, i ji idedame reiksmes
# data = {'weekday': filtered_week_days, 'temperature': day_temperatures}
# df = pd.DataFrame(data)
# print(df)
# #randame max ir min temperaturas
# max_temperature = df['temperature'].max()
# min_temperature = df['temperature'].min()
#
# import matplotlib.pyplot as plt
# #12 - ilgis(aukstis), 5 - plotis
# plt.figure(figsize=(12,5))
# plt.bar('Auksciausia temperatura', max_temperature, color = 'yellow')
# plt.bar('Zemiausia temperatura', min_temperature, color = 'blue')
# plt.ylabel('temperatura °C')
# plt.title('Auksciausia ir zemiausia temperatura Vilniuje')
# plt.show()
# #vidutine temp
# vidutine_temp = df['temperature'].mean()
# print(vidutine_temp)

# #nauja uzd: sukurti duomenu rinkini(listas) su procentais ir pavadinimais
# import matplotlib.pyplot as plt
# #apsirasome procentus kaip lista
# proc = [90, 10, 45, 60, 70]
# pasiekimai = ['matematika', 'istorija', 'fizika', 'anglu', 'biologija']
# spalvos = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen', 'pink']
# ex = (0.1, 0, 0, 0, 0)
# plt.pie(proc, explode=ex, labels=pasiekimai, colors=spalvos, autopct='%1.1f%%', startangle=160) #nurodo kiek sk po kalbelio(siuo atveju vienas)
# plt.title('Pasiekimu diagrama')
# plt.axis('equal') #uztikrina kad diagrama butu apskritimas
# plt.show()

#09-20
# import matplotlib.pyplot as plt
# x = [5,8,6,4,5]
# y = [4,3,2,9,7]
# z = [4,3,2,9,7]
#
# # linijinis grafikas
# plt.plot(x, y, label = 'linija', color = 'blue', linestyle = '--', marker = 'o')
# plt.plot( x, z, label = 'linija2', color = 'red', linestyle = '--', marker = 'o')
# plt.legend()
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Grafine vizualizacija')
# plt.show()

#taskai
# plt.scatter(x, y, label = 'taskai', color = 'red', marker = 's')
# plt.scatter(z, y, label = 'burbulai', color = 'blue', marker = 'o')
# plt.legend()
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Grafine vizualizacija')
# plt.show()

#histograma
# x = [1,2,3,4,3,2,1,0]
# plt.hist(x, bins = 5, color = 'pink', alpha = 0.7, edgecolor = 'black')
# # plt.legend()
# plt.xlabel('x')
# plt.title('Grafine vizualizacija')
# plt.show()

#pakopos - duomenu pokyciai nuo vieno tasko iki kito tasko
# x = [1,2,3,4,5]
# y = [10,15,7,12,9]

# plt.step(y, z, label = 'pakopos', color = 'red', where = 'mid')
# plt.fill_between(y, z, color = 'grey', alpha = 0.5)
# plt.text(4, 6, 'svarbus taskas', fontsize = 12, color = 'blue')
# plt.axhline(y = 3, color = 'green', linestyle = '--', label = 'horizontali')
# plt.axvline(x = 5, color = 'orange', linestyle = '--', label = 'vertikali')
# plt.clf()

# subplot - dvi eilutes ir vienas stulpelis (dvi linijos viena po kita grafike)
# x = [1,2,3,4,5]
# y = [10,15,7,12,9]
# plt.subplot(2,1,1)
# plt.plot(x, y, label = 'linija1')
# plt.title('Grafine vizualizacija')
# plt.legend()
# plt.subplot(2,1,2)
# plt.plot(x, [i**2 for i in y], label = 'linija2', color = 'green') #kelia kvardratu
# plt.legend()
# plt.xlabel('z')
# plt.ylabel('y')
# plt.savefig('grafikas.png') #issaugoja kaip paveiksleli
# plt.show()

#1 UZDUOTIS
# a. Įkelkite CSV failą, kuris turi duomenis apie prekių pardavimus.
# b. Išveskite pirmas 5 eilutes iš duomenų rinkinio, kad pamatytumėte, kaip atrodo duomenys.
# c. Apskaičiuokite vidutinę prekių kainą ir vidutinį pardavimų kiekį.
# d. Pateikite grafiką, kuriame būtų pavaizduota prekių pardavimų kiekio kitimas laiko atžvilgiu.

import pandas as pd
import matplotlib as pdb
import matplotlib.pyplot as plt
# data = pd.read_csv('/Users/kamila/Downloads/sales_data.csv', encoding='iso-8859-1')
# df = pd.DataFrame(data)
# print(df)
# result = df.head(5)
# print(result)
# vidutine_kaina = df['PRICEEACH'].mean().round(2)
# print(vidutine_kaina)
# vidutinis_pard_kiekis = df['QUANTITYORDERED'].mean().round(2)
# print(vidutinis_pard_kiekis)
#
# df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'])
# df['Metai'] = df['ORDERDATE'].dt.year
# df['Mėnuo'] = df['ORDERDATE'].dt.month
# df['Diena'] = df['ORDERDATE'].dt.day
# print(f'\n', df)
# Mėn_suma = df.groupby(['Metai', 'Mėnuo', 'Diena'])['QUANTITYORDERED'].sum()
# Mėn_suma.plot(kind= 'line', color='skyblue')
# plt.xticks(rotation = 90)
# plt.xlabel('Data')
# plt.ylabel('Pardavimai')
# plt.title('pardavimų skaičius laiko atžvilgiu')
# plt.show()

#random DB sukurimas
import random
# data = {
#     'id': [i+1 for i in range (50)],
#     'vardas': [random.choice(['Ona', 'Ina', 'Ana']) for _ in range (50)],
#     'alga': [random.randint(1000, 1500) for _ in range (50)]
# }
#
# df = pd.DataFrame(data)
# df.to_csv('atlyginimai.csv', index = False)

#2 UZDUOTIS su datos generavimu
# a. Sukurkite du sąrašus: vienas su laiko žymėmis (mėnesiais nuo sausio iki gruodžio) ir kitas su kas mėnesį parduotų prekių kiekiu.
# b. Pavaizduokite šiuos duomenis linijiniame grafike. Pridėkite ašių pavadinimus ir pavadinimą grafiko viršuje.
# c. Pridėkite legenda, kurioje būtų nurodyta, ką reiškia ši linija.

# from datetime import datetime, timedelta
# data = {'Stulpelis_id': [i+1 for i in range (10)],
#         'Data': [(datetime(2023, 1, 1) + timedelta(days=random.randint(0,364))).strftime('%Y-%m-%d') for _ in range (10)],
#         'Pardavimai': [random.randint(5, 150) for _ in range (10)]
# }
# df = pd.DataFrame(data)
# print(df)
#
# plt.plot('Data', label = 'Menesiai', color = 'blue', linestyle = '--', marker = 'o')
# plt.plot( 'Pardavimas', label = 'Parduotu prekiu kiekis', color = 'red', linestyle = '--', marker = 'o')
# plt.legend()
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Grafine vizualizacija')
# plt.show()





# Įkelkite kitą CSV failą su duomenimis apie studentų egzaminų rezultatus.
# b. Pateikite histogramą, kuri atvaizduotų studentų matematikos egzaminų rezultatus.
# c. Nustatykite tinkamą stulpelių (bins) skaičių, kad histograma būtų aiški ir informatyvi.
# d. Pridėkite ašių pavadinimus ir pavadinimą grafiko viršuje.
# Duomenų grupavimas ir pie grafikas:
# a. Grupuokite studentų egzaminų duomenis pagal lytį (vyrus ir moteris).
# b. Apskaičiuokite vidutinius rezultatus kiekvienoje grupėje.
# c. Pateikite pie grafiką, kuriame būtų rodoma, kiek procentų vyrų ir moterų pasiekė aukštesnius nei vidutinius rezultatus.
# a. Sukurkite tris linijinius grafikus viename paveiksle (subplots). Kiekvienas grafikas turėtų atvaizduoti skirtingus duomenų rinkinius (pavyzdžiui, kainas skirtinguose miestuose).
# b. Kiekvienam grafikui priskirkite ašių pavadinimus, pavadinimus ir legendas.
# c. Pateikite visus tris grafikus viename paveiksle.

# import csv
# data2 = pd.read_csv('/Users/kamila/Downloads/egzaminai.csv')
# df = pd.DataFrame(data2)











