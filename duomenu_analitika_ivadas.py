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

