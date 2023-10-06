#09-25
#susikurti numpy masyva, kuris saugoti nuo 1 iki 10 sveikuosius skaicius
from bs4 import BeautifulSoup
import requests
import pandas as pd
import psycopg2
import numpy as np
#
# masyvas = np.arange(1, 11)
# # print(masyvas)
# #elementu suma
# suma = np.sum(masyvas)
# print(suma)

# #is vienmates formos padarytis dvimate (2 ant 5)
# dvimatis_masyvas = masyvas.reshape(2, 5)
# # print(dvimatis_masyvas)
#
# #atspaudinti visus lyginius skaicius nuliais
# masyvas[masyvas %2 == 0] = 0
# # print(masyvas)
#
# #masyve skaiciai didesni nei 5
# masyvas3 = masyvas[masyvas > 5]
# print(masyvas3)

#sugeneruoti 5 ant 5 masyva su atsitiktiniais sk nuo 1 iki 100
# masyvas = np.random.randint(1, 101, (5,5))
# print(masyvas)

#rasti max ir min skaiciu masyve (printe galime formatuoti pasirinktinai)
# max = np.max(masyvas)
# print(max)
# min = np.min(masyvas)
# print(min)
#
# #sukeisti masyva atvirkstine tvarka (reverse) (sukeicia eilutes vietomis)
# naujas_masyvas = np.flipud(masyvas)
# # print(naujas_masyvas)
# #sukeisti masyvo stulpelius atvirkstine tvarka
# pakeisti_st = masyvas[:,::-1]
# # print(pakeisti_st)
# #ARBA
# naujas_masyvas_st = np.fliplr(masyvas)
# # print(naujas_masyvas_st)

#sujungti du masyvus i viena horizontaliai
# masyvas1 = np.random.randint(1, 10, 10)
# masyvas2 = np.arange(1, 50, 5) #3 sk po kablelio - kas kiek imti
# print(masyvas1, '\n', masyvas2)
#
# masyvas3 = np.hstack((masyvas1, masyvas2))
# print(masyvas3)
#
# #padalinti i du blokus
# masyvas4 = np.split(masyvas3, 2)
# print(masyvas4)

# [!] Sukurkite masyvą nuo 0 iki 9 ir jį pertvarkykite į 3x3 masyvą;
# masyvas = np.arange(1, 10)
# print(masyvas)
# naujas_masyvas = masyvas.reshape(3, 3)
# print(naujas_masyvas)

# [!] Sukurkite 5x5 masyvą su atsitiktinėmis reikšmėmis ir raskite vidurkį kiekvieno stulpelio;
# masyvas1 = np.random.randint(1, 50, (5,5))
# print(masyvas1)
# vidurkiai = np.mean(masyvas1, axis = 0)
# print(vidurkiai)
# [!] Sukurkite 6x6 masyvą su skaičiais nuo 1 iki 36 ir transformuokite jį į 2D masyvą (matricą) 3x12;
# masyvas2 = np.random.randint(1, 37, (6,6))
# print(masyvas2)
# naujas = masyvas2.reshape(3, 12)
# print(naujas)
# [!] Sukurkite masyvą su atsitiktinėmis reikšmėmis nuo 0 iki 1 ir raskite jo visų elementų vidurkį. Toliau paverskite mažesnes reikšmes į 0 ir didesnes į 1.
# #jeigu norime skaiciu po kalbelio, rasome random.rand
# masyvas3 = np.random.rand(0, 2, (5, 5))
# print(masyvas3)
# [!] Sukurkite du masyvus pirmas_masyvas ir antras_masyvas, kiekvieną su 5 atsitiktinėmis reikšmėmis nuo 1 iki 10,
# ir sudėkite juos taip, kad naujas masyvas turėtų visų reikšmių kvadratus.

