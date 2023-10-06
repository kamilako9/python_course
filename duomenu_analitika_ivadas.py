#DUOMENU ANALITIKOS IVADAS
#importuojame bibliotekas
import pandas as pd
# #sukuriame sarasa su duomenimis
# duomenys = {'Vardas': ['Jonas', 'Ieva', 'Petras', 'Ona'],
#             'Amzius': [25, 28, 22, 30]
#             }
# #sukuriame DataFrame is saraso
#DataFrame - kai norime sukurti keleta st.
# df = pd.DataFrame(duomenys)
# print(df)
# #filtruokime duomenis pagal amziu
# jaunesni = df[df['Amzius'] < 25]
# print(jaunesni)
# #skaiciuokime vidutini amziu
# vidutinis_amzius = df['Amzius'].mean()
# #mean - skaiciuoti vidurki
# print(f"Vidutinis amzius yra {vidutinis_amzius}")

# Series - kai norime sukurti viena stulpeli
# temperaturos =[24.5, 25.2, 23.8, 26.0, 22.5]
# sr = pd.Series(temperaturos)
# print(sr)
# #rikiuoti didejimo tvarka
# serija_rikiavimas = sr.sort_values()
# print(serija_rikiavimas)
# #rikiuoti mazejimo tvarka
# serija_rikiavimas = sr.sort_values(ascending = False)
# print(serija_rikiavimas)
# #isprintinti pirma elementa
# print(f"Pirmas elementas: {sr[0]}")

# DataFrame pavyzdziai
# duomenys = {'Vardas': ['Jonas', 'Ieva', 'Petras', 'Ona'],
#             'Amzius': [25, 28, 22, 30]
#             }
# df = pd.DataFrame(duomenys)
# #pasiimti tik vardus
# vardai = df['Vardas']
# #jeigu norime rezultato liste, rasome
# vardai = df['Vardas'].to_list()
# print("Vardai: ")
# print(vardai)
#
# #prideti nauja stulpeli i DataFrame
# df['Lytis'] = ['Vyras', 'Moteris', 'Vyras', 'Moteris']
# print('Atnaujintas dataframe su nauju stulpeliu: ')
# print(df)

# df.head() #atvaizduoja eiluciu kieki nuo priekio
# df.tail() # atvaizduoja nuo galo (paskutines pirmas eilutes)

#GRAFIKO SUKURIMAS
import matplotlib.pyplot as plt
#matplotlib - atvaizduoja grafika

# plt.figure(figsize=(8,5)) #nurodome asies dydi
# plt.bar(df['Vardas'], df['Amzius'], color = 'blue') #sukuriame stulpelini grafika
# plt.xlabel('Vardas') # X asies pavadinimas
# plt.ylabel('Amzius') # Y asies pavadinimas
# plt.title('Amzius pagal vardus') #grafiko pavadinimas
# plt.show() #rodome grafika

# data = {'Miestas': ['Vilnius', 'Kaunas', 'Kaunas', 'Vilnius'],
#         'Lytis': ['Vyras', 'Vyras', 'Moteris', 'Vyras'],
#         'Amzius': [25, 25, 22, 30]
#         }
# df = pd.DataFrame(data)
# vidutinis_amzius_pagal_miesta = df.groupby('Miestas')['Amzius'].mean()
# print(vidutinis_amzius_pagal_miesta)
#rezultatas - sugrupavome pagal miesta ir apskaiciavome vidutini amziu pagal miesta

#UZDUOTYS
# Sukurkite Pandas DataFrame(4 miestai ir ju populiacija).
# Filtravimas ir paieška:
# a. Filtruokite miestus, kurių populiacija yra didesnė nei 200 000 žmonių.
# b. Raskite miestą, turintį mažiausią populiaciją.
# Duomenų grupavimas ir agregavimas:
# a. Pridėkite stulpelį "Šalis" prie ankstesnio DataFrame, kuriame nurodoma, kuri šalis priklauso kiekvienam miestui (pvz., "Lietuva").
# b. Grupuokite duomenis pagal "Šalis" stulpelį ir apskaičiuokite bendrą populiaciją kiekvienai šaliai.
# Duomenų rikiavimas:
# Rikiuokite miestus pagal populiaciją mažėjimo tvarka.

# miestai = {'Miestas': ['Vilnius', 'Varsuva', 'Ryga', 'Minskas'],
#            'Populiacija': [300000, 600000, 50000, 80000],
#            }
# df = pd.DataFrame(miestai)
# print(df)
# populiacija_didesne_nei = df[df['Populiacija'] > 200000]
# print(populiacija_didesne_nei)
# min_populiacija = df[df['Populiacija'] == df['Populiacija'].min()]
# print(f"Maziausia populiacija: {min_populiacija}")
#
# # df['Salis'] = ['Lietuva', 'Lenkija', 'Latvija', 'Baltarusija']
# # print('Atnaujintas dataframe su nauju stulpeliu salys: ')
# # print(df)
# # bendra_populiacija = df.groupby('Salis')['Populiacija'].sum()
# # print(bendra_populiacija)
# #
# # rikiavimas = df.sort_values(ascending = False)
# # print(rikiavimas)
#
# #pasalinti miesta
# df1 = df[df['Miestas']!= 'Minskas']
# print(df1)
# #pakeisti Vilniaus populiacija
# # su funkcija loc - pasiekiame duomenis
# df.loc[df['Miestas'] == 'Vilnius', 'Populiacija'] = 10000
# print(df)
# #padidinti Vilniaus populiacija
# df.loc[df['Miestas'] == 'Vilnius', 'Populiacija'] += 10000
# print(df)

#  * Sukurkite Pandas duomenų lentelę su 5 eilutėmis ir 3 stulpeliais.
#    * Pavadinkite stulpelius "Vardas", "Amžius" ir "Miestas".
#    * Įtraukite naują eilutę į lentelę su duomenimis: "Jonas", 30, "Vilnius".
#    * Išspausdinkite pirmas 3 eilutes iš lentelės.
#    * Išspausdinkite stulpelį "Amžius" visų eilučių atveju.
#    * Atrinkite visus žmones, kurių amžius yra mažesnis nei 25.
#    * Sukurkite naują stulpelį "Gimimo metai" pagal esamą stulpelį "Amžius".
#    Paskaičiuokite gimimo metus pagal 2023 metus.
#    * Ištrinkite eilutę su "Jonas" iš lentelės.
#    * Išsaugokite lentelę į CSV failą pavadinimu "duomenys.csv".
#    * Nuskaitykite duomenis iš "duomenys.csv" failo į naują Pandas lentelę.
#    * Atrinkite visus žmones, gyvenančius Vilniuje.
# zmones = {'Vardas': ['Ieva', 'Ona', 'Tomas', 'Petras'],
#           'Amzius': [14, 34, 8, 76],
#           'Miestas': ['Kaunas', 'Plunga', 'Palanga', 'Vilnius']
#            }
# df = pd.DataFrame(zmones)
# print(df)
# df = df[df['Vardas']== 'Jonas']
# print(df)

# #09-18
# from bs4 import BeautifulSoup
# import requests
# import pandas as pd
# import psycopg2
# def create_and_insert_product():
#     connection = psycopg2.connect(
#         host="localhost",
#         port=5432,
#         database="products",
#         user="postgres",
#         password="gulbiu12"
#     )
#
#     cursor = connection.cursor()
#
#     create_table_query = """
#         CREATE TABLE IF NOT EXISTS varle_products (
#         id SERIAL PRIMARY KEY,
#         name VARCHAR (255),
#         price DECIMAL (10,2),
#         quantity INT)
#     """
#
#     cursor.execute(create_table_query)
#     print("Table created successfully!")
#     #
#     #
#     #
#     url = 'https://www.varle.lt/nesiojami-kompiuteriai/nesiojami-kompiuteriai/'
#     response = requests.get(url)
#     print(response.status_code)
#
#     soup = BeautifulSoup(response.content, 'html.parser')
#     product_elements = soup.find_all('div', class_='GRID_ITEM')
#     # print(product_elements)
#     product_data = []
#     for product_element in product_elements:
#         product_name = product_element.find('div', class_='product-title').text.strip()
#         product_price = float(product_element.find('span', class_='price-value').text.strip().replace('€', ''))
#         product_quantity = product_element.find('b').text.strip()[:1]
#         # print(f"Adding products to the list: {product_name}")
#         product_data.append((product_name, product_price, product_quantity))
#         insert_query="INSERT INTO varle_products (name, price, quantity) VALUES (%s, %s, %s)"
#         print("Products inserted into the list successfully!")
#         connection.commit()
#     #
#         # connection.close()
#     # df = pd.DataFrame(product_data, columns=['name', 'price', 'quantity'])
#
#     select_query = "select * from"
#
#     cursor.execute()
# if __name__ == '__main__':
#     create_and_insert_product()











