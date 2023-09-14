import random
import string

# vardas = "Modestas"
# #print(vardas)
# skaicius = 25
# skaicius1 = '32'

#print("Mano sugalvotas skaicius " + str(skaicius))
#print-spausdina rezultata
#int - integer(skaicius), str - string(tekstas)

# true_or_false = False - boolienas
#print(type(true_or_false))

#fruits = ['apple', 'orange', 'kiwi', 'watermelon']
#lietuvos_pilietis = {
    #'id': 1,
    #'Vardas': 'Antanas',
    #'Amzius': 34,
    #'Miestas': 'Klaipeda'
#}
#print(lietuvos_pilietis)
#kaip atvaizduoti kad nebutu skliaustu ir kabuciu, va taip:
#print("Vardas:", lietuvos_pilietis["Vardas"])
#lietuvos_pilietis['Vardas'] = "Giedrius"
#print("Vardas:", lietuvos_pilietis["Vardas"])

#print(fruits[1])
#print(type(fruits))
#skaiciuojame nuo 0,1,2,3 is pradziu
#nuo galo - -1(watermelon), -2, kiwi, -3 orange ir tt
#fruits - kintamasis, vaisiai - reiksmes

# temperaturos = [20, 25, 22, 18, 12]
# suma = sum(temperaturos)
# print(suma)
#
# #apskaiciuoja kiek liste reiksmiu
# kiekis = len(temperaturos)
# print(kiekis)
#
# #vidurkis
# vidutine_temp = suma / kiekis
# print("Vidutine temperatura yra:", vidutine_temp)
#
# # sudetis = 5 + 5
# atimtis = 6 - 2
# dalyba = 15 / 3
# dalyba_be_liekanos = 15 // 3 - grazina tik sveika skaciu
# daugyba = 5 * 9
# laipsnis = 2 ** 3 - 2*2*2
# print(laipsnis)
# dalyba_liekana = 10 % 3 - rodo liekana po dalybos, t.y. dalybos liekana

# skaicius = 42
# if skaicius < 42:
# print("daugiau uz 42")
# elif skaicius == 42:
#     print("lygus")
# else:
#     print("Nelygus")

#
# sarasas = [1,2,3,4,5]
# for elementas in sarasas:
#     print("Elementas: ", elementas)
#
# for i in range(5,0,-1):
#     print(i)

#didziausias skaicius sarase
# skaiciai = [24, 11, 72, 34, 7, 84]
#
# didziausias_skaicius = skaiciai[0]
#
# for skaicius in skaiciai:
#     if skaicius > didziausias_skaicius:
#         didziausias_skaicius = skaicius
# print("Didziausias skaicius yra: ", didziausias_skaicius)

#svarbu tarpai po if, for,
# printas turi buti pradzioje
#
# skaicius = input("koks tavo vardas:")
# print(skaicius)
#
# skaicius = int(input("parasyk skaiciu")) - int - kai norime sveiko skaiciaus
# skaicius = float(input("parasyk skaiciu: ")) - float - kai norime skaiciaus po kablelio

# skaicius = int(input("ivesk skaiciu: "))
# suma = 0
# for i in range (1,skaicius + 1):
#     suma += i
# print("skaiciu_suma nuo 1 iki", skaicius, "yra", suma)
#for - ciklas, range funkscija - kai daug eiluciu

# 1. uzduotis: is saraso isfiltruoti lyginius skaicius
# sarasas = [2,5,11,34,25,9]
# lyginiai_skaiciai = []
# for skaicius in sarasas:
#     if skaicius %2 == 0:
#         lyginiai_skaiciai.append(skaicius)
# print("lyginai_skaiciai ",  lyginiai_skaiciai)

# 2. uzduotis: isspausdinti piramide su zvaigzdutemis
# eiluciu_skaicius = int(input("ivesk sveika skaiciu "))
# for eilute in range(1, eiluciu_skaicius + 1 ):
#     tarpas = eiluciu_skaicius - eilute
#     zvaigzdutes = 2 * eilute -1
#     print(" " * tarpas +  "*" * zvaigzdutes)

# 3. uzduotis: surasti pirminius skacius is intervalo [10;50] pirminiai skaiciai
# pradzia = 10
# pabaiga = 50
# print(f"pirminiai skaiciai tarp {pradzia} ir {pabaiga} yra: ")
# for skaicius in range(pradzia, pabaiga+1):
#     if skaicius > 1:
#         for daliklis in range(2, skaicius):
#             if (skaicius % daliklis)==0:
#                 break
#         else:
#             print(skaicius)

# 4. uzduotis: patikrinti zodzius ir saraso bei rasti ir atspausdinti zodzius kurie prasideda 'a'
# zodziai_is_a = ["as", "tu", "jis", "arba", "mes"]
# #apsirasom kintamaji
# raide = "a"
# #einame per visa sarasa ir tikriname (zodis - raktas)
# for zodis in zodziai_is_a:
#     if zodis[0].lower() == raide.lower():
#         print(zodis)

# 5. uzduotis: sudaryti ir isvesti daugybos lentele
#pirma reik isprintinti daugybos lentele

# print("daugybos lentele nuo 1 iki 10")
# for i in range(1, 11):
#     for j in range(1, 11):
#         rezultatas = i * j
#         print(f"{i} x {j} = {rezultatas}")
#     print()

# 6. uzduotis: patikrinti ar skaicius kuris ivede vartotojas yra neigiamas, teigiamas ar nulis
# skaicius = int(input("ivesk skaciu: "))
# if skaicius > 0:
#     print("ivestas skaicius teigiamas ")
# elif skaicius < 0:
#     print("ivestas skaicis neigiamas ")
# else:
#     print("ivestas skaicius lygu nulis ")

# 7. uzduotis: sukurti programele, kur fizz skaiciams kurie dalijasi is 3, buzz skaiciams kurie dalijasi is 5,
# ir fizzbuzz kurie dalijasi is 3 ir 5. (intervale nuo 1 iki 100)

# for skaicius in range(1,101):
#     if skaicius % 3 == 0 and skaicius %5 == 0:
#         print("fizzbuzz")
#     elif skaicius % 3 ==0:
#         print("fizz")
#     elif skaicius % 5 ==0:
#         print("buzz")
#     else:
#         print(skaicius)

# 8. uzduotis: sukurkite skaiciu atspejimo zaidima

# randint - atsitiktiniai sveiki skaiciai
# pasleptas_skaicius = random.randint(1, 100)
# bandymai = 0
# maksimalus_bandymu_skaicius = 10
# while bandymai < maksimalus_bandymu_skaicius:
#     spejimas = int(input("atspekite paslepta skaiciu nuo 1 iki 100: "))
#     bandymai += 1
#     if spejimas == pasleptas_skaicius:
#         print(f"sveikiname! atspejote skaiciu per {bandymai} bandymus")
#         break
#     elif spejimas < pasleptas_skaicius:
#         print("bandykite didedsni skaiciu")
#     else:
#         print("bandykite mazesni skaiciu")
# if bandymai >= maksimalus_bandymu_skaicius:
#     print(f"pasiekete maksimalu bandymu skaiciu. pasleptas skaicius buvo {pasleptas_skaicius}")

# 9. uzduotis: sukurti zodziu sarasa (zodyna), kuriame saugomi zodziai. reikia isvesti zodzius, kurie ilgesni
# nei 6 simboliai

# zodziai = ["kompiuteris", "stalas", "knyga", "telefonas", "langas", "ekranas", "gele"]
# zodynas = {}
# for zodis in zodziai:
#     zodynas[zodis] = len(zodis)
# for zodis, ilgis in zodynas.items():
#     if ilgis > 6:
#         print(f"{zodis}: {ilgis} simboliai")



# 1. Sukurkite žodyną ir trumpą tekstą. Atspasudinkite žodžius, kurie pasikartojo daugiau nei 3 kartus;
# trumpas_tekstas = [


# 2 .Sukurti sąrašą žodžių ir išvesti unikalius žodžius bei jų pasikartojimo dažnumą;


# 3. Sukurkite žodyną su studentų duomenimis ir atspausdinkite studentus, kurių vidurkis yra aukščiau 8.0;


# 4. Sukurti žodyną su knygų informacija ir surikiuoti knygas pagal metus ir pavadinimus.

# import string
# ilgis = 7
# simboliai = string.ascii_letters + string.digits + string.punctuation
# random_string = ''.join(random.choice(simboliai)for _ in range(ilgis))
# print("random_string", random_string)

# 1. Parašykite programą, kuri suskaičiuoja visų sveikujų skaičių nuo 1 iki n ėjimo sumą,
# kur n yra vartotojo įvestas skaičius.
# n = int(input("iveskite skaciu: "))
# if n <= 0:
#     print("ivestas skaicius turi buti sveikasis, bandykite dar karta")
# else:
#     suma = 0
#     for skaicius in range (1, n + 1):
#         suma += skaicius
#     print(f"suma nuo 1 iki {n} yra {suma}")

#2. Sukurkite programą, kurioje vartotojas gali įvesti mokinio pažymį (nuo 1 iki 10).
# Programa turi grąžinti mokinio vertinimą (pvz., "Neužtektinai", "Silpnai", "Vidutiniškai", "Gerai", "Puikiai").
# Naudokite "if" sąlygos sakinį;
# pazymis = int(input("iveskite mokinio vertinima: "))
#     if pazymis <= 9:
#         print("puikiai")
#     elif pazymis <= 7:
#         print("vidutiniskai")
#     elif pazymis <=5:
#         print("silpnai")
#     elif pazymis <= 2:
#         print("neuztektinai")
#     else:
#         pazymis = "netinkamas pazymis, iveskite pazymi nuo 1 iki 10"


#ARBA
# if pazymis < 1 or pazymis > 10:
#     vertinimas = "Netinkamas pazymis, iveskite pazymi nuo 1 iki 10"
# elif pazymis >= 9:
#     vertinimas = "Puikiai"
# else:
#     vertinimas = "neuztektinai"
# print(f"mokinio vertinimas: {vertinimas}")

# pazymys = int(input("iveskite mokinio vertinima: "))
# if pazymys >= 9 and pazymys <= 10:
#     print("Puikiai")
# elif pazymys >= 7 and pazymys < 9:
#     print("Gerai")
# elif pazymys >= 5 and pazymys < 7:
#     print("Vidutiniškai")
# elif pazymys >= 4 and pazymys < 5:
#     print("Silpnai")
# elif pazymys >= 1 and pazymys < 4:
#     print("Neužtektinai")
# else:
#     print("Netinkamas pažymys, įveskite pažymį nuo 1 iki 10.")

# pazymys = int(input("Įveskite mokinio pažymį nuo 1 iki 10: "))
#
# if pazymys >= 9 and pazymys <= 10:
#     vertinimas = "Puikiai"
# elif pazymys >= 7 and pazymys < 9:
#     vertinimas = "Gerai"
# elif pazymys >= 5 and pazymys < 7:
#     vertinimas = "Vidutiniškai"
# elif pazymys >= 4 and pazymys < 5:
#     vertinimas = "Silpnai"
# elif pazymys >= 1 and pazymys < 4:
#     vertinimas = "Neužtektinai"
# else:
#     vertinimas = "Netinkamas pažymys, įveskite pažymį nuo 1 iki 10."

# print(f"Mokinio vertinimas: {vertinimas}")
#3. Sukurkite programą, kuri leidžia vartotojui įvesti metus.
#Programa turi patikrinti, ar įvesti metai yra keliamieji (dalijasi iš 4) ir atspausdinti atitinkamą pranešimą.


# == reiskia kad 0 skaiciu po kablelio, (be liekanos)
# metai = int(input("Iveskite metus: "))
# if metai % 4 == 0:
#     print("Metai yra keliamieji")
# else:
#     print("Metai nera keliamieji, pasirinkite kita skaiciu.")

# 4. Turite žodyną, kuriame yra vardai ir amžius. Parašykite programą, kuri peržiūri žodyną ir išrenka tik tas poras,
# kuriose amžius yra didesnis arba lygus 18. Rezultatus patalpinkite naujame žodyne;

# zodynas = {
#     'Mantas': 12,
#     'Lina': 40,
#     'Ona': 17,
#     'Matas': 18,
#     'Gytis': 34,
#     'Dalia': 13
# }
# zodynas_naujas = {}
# for vardas, amzius in zodynas.items():
#     if amzius >= 18:
#         zodynas_naujas[vardas] = amzius
# print(zodynas_naujas)

# 5. Leiskite vartotojui įvesti kelias prekes ir jų kainas.
# Sukurkite sąrašą, kuriame prekės yra žodynai, kuriuose yra prekės pavadinimas ir kaina.
# Taip pat paskaičiuokite bendrą visų prekių kainą;
#append - apjungia abi reiksmes

# prekiu_krepselis = []
# while True:
#     preke = input("Nurodykite preke arba irasykite zodi baigti")
#     if not preke:
#         break
#     kaina = float(input("Iveskite prekes kaina: "))
#     prekes_info = {"pavadinimas": preke, "kaina": kaina}
#     prekiu_krepselis.append(prekes_info)
#
# krepselio_suma = sum((prekes_info["kaina"] for prekes_info in prekiu_krepselis))
# print("prekiu sarasas: ")
# for prekes_info in prekiu_krepselis:
#     print(f"pavadinimas: {prekes_info["pavadinimas"]}, kaina: {prekes_info["kaina"]}")
# print(f"bendra kaina: {krepselio_suma}")
#
#     prekiu_krepselis = []
#     while True:
#         preke = input("Nurodyte prekę arba įrašykite žodį baigti")
#         if not preke:
#             break
#         kaina = float(input("Įveskite prekės kainą: "))
#         prekes_info = {'pavadinimas': preke, 'kaina': kaina}
#         prekiu_krepselis.append(prekes_info)
#
#     Krepselio_suma = sum((prekes_info['kaina'] for prekes_info in prekiu_krepselis))
#     print("prekiu sarasas: ")
#     for prekes_info in prekiu_krepselis:
#         print(f"Pavadinimas: {prekes_info['pavadinimas']}, Kaina: {prekes_info['kaina']}")
#     print(f"Bendra kaina: {Krepselio_suma}")

#pasirenka varda pagal skaiciu (priminimas: skaiciuoja nuo 0), jeigu nieko nepasirenkame, grazina paskutini vardo
# vardai = ['Jonas', 'Petras', 'Marius', 'Laura']
# pirmas_vardas = vardai.pop(2)
# print(pirmas_vardas)

#insert - ikelia papildoma reiksme sarase, (pagal indeksavima)
#append - prideda paskutine reiksme i sarasa
# vardai.insert(1, 'Giedrius')
# print(vardai)

#sort- rusiuoja pagal abecele (pagal nutylejima)
# vardai.sort()
# print(vardai)

#pasalina pirma reiksme
# vardai.remove('Laura')
# print(vardai)


#trys sarasai
#() - tupple - negalima keisti reiksmiu, naudingas kai turime duomenis ir nenorime juose nieko keisti
#[] - sarasas - galima prideti, atimti, keisti ir tt

# vaisiai = ('obuolys', 'kriause', 'bananas', 'braske')
# vaisiai1 = ['obuolys', 'kriause', 'bananas', 'braske']

# vaisiai2 = vaisiai[0]
# print(vaisiai2)

# skaiciai = (3.14, 2.71)
# x, y = skaiciai
# print(x)
# print(y)

#enumarate - jo tikslas yra gauti tiek elementu, kiek turime objekte, pvz sarase
#startas - elementas nuo kurio pradedama skaciuoti (python indeksavimas prasideda nuo 0,
# bet sioje funkcijoje pradeda skaiciuoti standartiskai nuo 1.
# vaisiai = ['obuolys', 'kriause', 'bananas', 'braske']
# for indeksas, vaisius in enumerate(vaisiai, start=1):
#     print(f"{indeksas}. {vaisius}")


#kaip galima sukurti nauja faila
# r-read, w-write, a-append)
# with open("failo_pav.txt", "w", encoding="utf-8") as file:
#     content = file.write("kuriame nauja faila")

# append- prideda nauja teksta
# with open("failo_pav.txt", "a", encoding="utf-8") as file:
#     content = file.append(\n "papildomas tekstas")

# read- nuskaito teksta esanciame faile
# with open("failo_pav.txt", "r", encoding="utf-8") as file:
#     content = file.read()
#     print(content)

#kitos budas nuskaityti faile esanti teksta (be read funkcijos, o su for)
# with open("failo_pav.txt", "r", encoding="utf-8") as file:
#     for eilute in file:
#         print(eilute.strip())

#1. Sukurkite sąrašą temperatūros su temperatūromis.
#Patikrinkite kiekvieną temperatūrą sąraše ir išveskite "šilta" (jei temperatūra virš 20)
#arba "šalta" (jei temperatūra 20 ar mažiau).

# temperaturos = [9, 15, 27, 23, 20, 29]


# 2. Turite žodyną su studentų vardais ir jų pažymiais.
# Parašykite "for" ciklą, kuris išveda kiekvieno studento vardą ir jo pažymį.
#
# 3. Sukurkite tuščią sąrašą sarasas ir leiskite vartotojui įvesti skaičius.
# Naudojant "while" ciklą, pridėkite kiekvieną įvestą skaičių prie sąrašo.
# Ciklą nutraukite, kai vartotojas įveda 0.
#
# 4. Turite žodyną, kuriame saugomi gėrimų pavadinimai ir jų kainos.
# Vartotojas įveda gėrimo pavadinimą, o jūs patikrinkite, ar tokio pavadinimo gėrimas yra žodyne.
# Jei taip, išveskite jo kainą; jei ne, išveskite pranešimą "Gėrimas nerastas".
#
# 5. Patikrinkite, ar skaičiai sąraše yra lyginiai arba nelyginiai. Sukurkite du tuščius sąrašus:
# vienas lyginiams ir kitą nelyginiams skaičiams, išrūšiuokite lyginius ir nelyginius skaičius iš skaičiai sąrašo.


# funkcijos
# def pasisveikinimas(vardas):
#     sveikinimas = f"Sveiki, {vardas}"
#     return sveikinimas
# #return-grazina rezultata - privalomas, kad grazintu tai, ka atlieka ta funkcija
#
# vardas = input("Iveskite savo varda: ")
# sveikinimas = pasisveikinimas(vardas)
# print(sveikinimas)


#def-apibreziame funkcija
#ar_lyginis - funkcija
# (skaicius) - parametras

# def ar_lyginis(skaicius):
#     if skaicius %2== 0:
#         return True
#     else:
#         return False
#
# skaicius = 5
# if ar_lyginis(skaicius):
#     print(f"{skaicius} yra lyginis")
# else:
#     print (f"{skaicius} yra nelyginis")

# def suma(a,b):
#     rezultatas = a + b
#     return(rezultatas)
#
# x = 5
# y = 2
# sumos_rezultatas = suma(x,y)
# print(f"{x} + {y} = {sumos_rezultatas}")

# def vidurkis(skaiciai):
#     suma = sum(skaiciai)
#     avg = suma / len(skaiciai)
#     return avg
#
# sarasas = [23, 45, 67, 88, 95]
# rezultatas = vidurkis(sarasas)
# print(f"saraso vidurkis: {rezultatas}")

#1. patikrinti ar skaicius yra teigiamas ar neigiamas
# def ar_teigiamas(skaicius):
#     if skaicius > 0:
#         return True
#     else:
#         return False
# skaicius = -34
# if ar_teigiamas(skaicius):
#     print(f"{skaicius} yra teigiamas")
# else:
#     print(f"{skaicius} yra neigiamas")

#2. parasyti funkcija kuri suras didziausia reiksme sarase
# def didziausias_skaicius(sarasas):
#     didziausias = sarasas[0]
#     for i in sarasas:
#         if i > didziausias:
#             didziausias = i
#     return didziausias
# sk_sarasas = [2,54,34,67,25,11,48]
# didziausias = didziausias_skaicius(sk_sarasas)
# print(f"didziausias skaicius yra {didziausias}")

#3. parasyti funkcija kuri sujuncia du sarasus
# def sujungti_sarasai(sarasas1, sarasas2):
#     sujungtas_sarasas = sarasas1 + sarasas2
#     return sujungtas_sarasas
# a = [1,3,6,9]
# b= [56,87,23,90]
# sujungtas = sujungti_sarasai(a, b)
# print(sujungtas)

#4. funkcija, kuri suras didesni skaiciu nei nurodyta sarase
# def didesnis(sarasas, skaicius):
#     didis = [sk_1 for sk_1 in sarasas if sk_1 > skaicius]
#     return didis
# sarasas = [3, 56, 8, 123, 567]
# n = 9
# didesni_sk = didesnis(sarasas, n)
# print(f"sarase skaiciai didesni uz {n} yra {didesni_sk}")
#
# trumpas_tekstas = "mieste buvo ir Ona, ir Ana, ir Eva, bet vaikino Tomo ir vaikino Tado nebuvo,bei vaikino Vasios nebuvo"
# žodynas = {}
# zodziai = trumpas_tekstas.split()
# for zodis in zodziai:
#     zodis = zodis.strip(",.")
#     žodynas[zodis] = žodynas.get(zodis, 0) + 1
# for zodis, pasikartojimai in žodynas.items():
#     if pasikartojimai >=3:
#         print(f"pasikartojantis(-ys) Žodis(-iai) yra: {zodis}, pasikartojo {pasikartojimai} kartų")


# 1. Parašykite funkciją, kuri priimtų sąrašą studento pažymių ir grąžintų vidurkį;
# def vidurkis(skaiciai):
#     suma = sum(skaiciai)
#     avg = suma / len(skaiciai)
#     return avg
#
# pazymiu_sarasaas = [5,7,9,8,4,10,56,3]
# rezultatas = vidurkis(pazymiu_sarasas)
# print (f" Pazymiu vidurkis yra: {rezultatas}")
# #

# 2. Sukurkite funkciją pirminiai_skaiciai(n), kuri priima sveikąjį skaičių n ir grąžina visus pirminius skaičius nuo 2 iki n;
#
#
# 3. Sukurkite funkciją zodziu_kiekis(tekstas), kuri priima tekstą ir grąžina žodžių skaičių tekste. Žodžius galite laikyti atskirtais tarpais;
#
#
# 4. Sukurkite funkciją didziausias_elementas(sarasas), kuri priima sąrašą skaičių ir grąžina didžiausią elementą;
#
#
# 5. Sukurkite funkciją kvadrato_plotas(ilgis), kuri priima kvadrato kraštinės ilgį ir grąžina kvadrato plotą.
#
#
# 6. Sukurkite funkciją sarasas_suma(sarasas), kuri priima sąrašą skaičių ir suskaičiuoja jų sumą. Leiskite vartotojui įvesti sąrašą skaičių ir išvesti jų sumą;
#
#
# 7. Sukurkite funkciją, kuri priimtų skaičių sąrašą ir grąžintų visų sąrašo skaičių sandaugą.

#OBJEKTINIS PROGRAMAVIMAS

# sukuriamas klase
# class Zmogus:
#     # sukuriamas konstruktorius
#     def __init__(self, vardas, amzius):
#         self.vardas = vardas
#         self.amzius = amzius
#     # kuriami metodai
#     def sveikinimas(self):
#         return f"Sveiki, as esu {self.vardas} ir man yra {self.amzius} metu"
#
# # sukuriamas objektas

# zmogus1 = Zmogus("Migle", 30)
# zmogus2 = Zmogus("Antanas", 45)
# print(zmogus1.sveikinimas())
# print(zmogus2.sveikinimas())

# class Automobilis:
#     def __init__(self, marke, modelis):
#         self.marke = marke
#         self.modelis = modelis
#         self.greitis = 0
#     # 0 - pradine reiksme
#     def akseletatorius(self):
#         self.greitis += 10
#
#     def stabdis(self):
#         self.greitis -= 5
#
#     def info(self):
#         return f"{self.marke} {self.modelis}, greitis: {self.greitis} km/h"
#
# auto1 = Automobilis("Mazda", "323")
# auto1.akseletatorius()
# auto1.akseletatorius()
# auto1.akseletatorius()
# auto1.stabdis()
# print(auto1.info())

# 1. sukurti knygos klase, kuri turi pavadinima, autoriu ir leidimo metus

# class Knyga:
#
#     def __init__(self, pavadinimas, autorius, leidimo_metai):
#         self.pavadinimas = pavadinimas
#         self.autorius = autorius
#         self.leidimo_metai = leidimo_metai
#
#     def info(self):
#         return f"Knygos pavadinimas yra {self.pavadinimas}, autorius yra {self.autorius}, leidimo metai {self.leidimo_metai}"
#
# knyga1 = Knyga("'Mergina is miesto'", "Ona Petraite", 1999)
# print(knyga1.info())

# 2. sukurti pirkiniu krepseli kuris turi tam tikras prekes
# (class) klases pavadinimas visada didziaja raide
# class Preke:
    # def __init__(self, pavadinimas, kaina):
    #     self.pavadinimas = pavadinimas
    #     self.kaina = kaina
    #
    # def info(self):
    #     return f"Prekes pavadinimas yra {self.pavadinimas}, kaina {self.kaina} euru"

#sukuriame tevine klase
# class Krepselis:
#     def __init__(self):
#         self.prekes = []
#
#     def ideti_preke(self, preke):
#         self.prekes.append(preke)
#
#     def krepselio_info(self):
#         if not self.prekes:
#             print("Tokios prekes nera")
#         else:
#             print("Krepselio turinys: ")
#             for preke in self.prekes:
#                 print(preke.info())
#     def bendra_suma(self):
#         suma = sum(preke.kaina for preke in self.prekes)
#         return suma
#
# krepsys = Krepselis()
# preke1 = Preke("Obuolys", 0.30)
# preke2 = Preke("Pienas", 2.99)
# preke3 = Preke("Sokoladas", 4.5)
# preke4 = Preke("Kava", 10.70)
#
# krepsys.ideti_preke(preke1)
# krepsys.ideti_preke(preke2)
# krepsys.ideti_preke(preke3)
# krepsys.ideti_preke(preke4)
#
# krepsys.krepselio_info()
# print(f"Bendra suma: {krepsys.bendra_suma()} euru")

# 3. Sukurkite klasę "Saskaita", kuri turėtų šias savybes ir metodus:
#  * saskaitos_nr: sąskaitos numeris.
#  * balansas: sąskaitos balansas (numatytasis pradžioje yra 0).
#  * inesti(suma): metodas, kuris prideda nurodytą sumą prie sąskaitos balanso.
#  * isimti(suma): metodas, kuris sumažina sąskaitos balansą nurodyta suma, jei yra pakankamai lėšų, arba išveda pranešimą apie nepakankamą balansą.
#  * informacija(): metodas, kuris grąžina informaciją apie sąskaitą (sąskaitos numeris ir balansas).
# Sukurkite bent du objektus pagal šią klasę ir atlikite operacijas, tokiu kaip lėšų įnešimas ir išėmimas, bei gaukite sąskaitos informaciją.

# class Saskaita:
#     def __init__(self, saskaitos_nr, balansas = 0):
#         self.saskaitos_nr = saskaitos_nr
#         self.balansas = 0
#         print(f"Sveiki prisijunge prie savo banko saskaitos!")
#     def inesimo_suma(self, suma):
#         self.balansas += suma
#
#     def isemimo_suma(self, suma):
#         if self.balansas >= suma:
#             self.balansas -= suma
#             print (f" Jus isemete: {suma}")
#
#         else:
#             print("Nepakankamas likutis")
#     def info(self):
#         return f"Saskaitos numeris: {self.saskaitos_nr}, saskaitos balansas: {self.balansas}"
#
# saskaita1= Saskaita('LT110', 2000)
# saskaita1.isemimo_suma(125)
# print(saskaita1.info())
#
# Sukurkite klasę "Studentas", kuri turėtų šias savybes:
#     * vardas: studento vardas.
#     * pazymiai: sąrašas su studento pažymiais.
# Sukurkite klasę "Mokytojas", kuri turėtų šias savybes:
#     * vardas: mokytojo vardas.
#     * Mokytojo dėstoma tema: mokytojo dėstomas dalykas.
# Papildykite "Studentas" klasę metodu vidurkis(), kuris apskaičiuoja studento pažymių vidurkį.
# Papildykite "Mokytojas" klasę metodu ivertinimas(studentas, pazymys), kuris prideda studentui pažymį.
# Sukurkite objektus pagal "Studentas" ir "Mokytojas" klases, pridėkite pažymius ir vykdykite vidurkio apskaičiavimus bei pažymių pridėjimus.
#
# class Studentas:
#     def __init__(self, studento_vardas):
#         self.studento_vardas = studento_vardas
#         self.pazymiai = []
#
#     def prideti_pazymi(self, pazymys):
#         self.pazymiai.append(pazymys)
#     def vidurkis(self):
#         if not self.pazymiai:
#             return 0
#         return sum(self.pazymiai) / len(self.pazymiai)
#
# class Mokytojas:
#     def __init__(self, mokytojo_vardas, destomas_dalykas):
#         self.mokytojo_vardas = mokytojo_vardas
#         self.destomas_dalykas = destomas_dalykas
#     def ivertinimas(self, studentas, pazymys):
#         studentas.prideti_pazymi(pazymys)
#
# studentas1 = Studentas("Petras")
# mokytojas1 = Mokytojas("Jurgis", "matematika")
# mokytojas2 = Mokytojas("Ona", "biologija")
#
# mokytojas1.ivertinimas(studentas1, 6)
# mokytojas2.ivertinimas(studentas1, 9)
# print(f" Studentas {studentas1.studento_vardas}, vidurkis: {studentas1.vidurkis()}")

#Sukurkite klasę "Kava", kuri turėtų savybes "pavadinimas", "kaina", ir "talpa".
# Parašykite metodą, kuris patikrintų, ar ši kava yra tinkama tam tikram puodeliui, pagal jo talpą.

# class Kava:
#     def __init__(self, pavadinimas, kaina, talpa):
#         self.pavadinimas = pavadinimas
#         self.kaina = kaina
#         self.talpa = talpa
#     def ar_tinkama_puodeliui(self, puodelio_talpa):
#         if self.talpa <= puodelio_talpa:
#             return f"{self.pavadinimas} kava tinka puodeliui su talpa {puodelio_talpa} ml"
#         else:
#             return f"{self.pavadinimas} kava netinka puodeliui su talpa {puodelio_talpa} ml"
#
# kava1 = Kava("Latte", 2.99, 250)
# puodelio_talpa = 300
# print(kava1.ar_tinkama_puodeliui(puodelio_talpa))

# Klase knygynas, kuri turi savybe knygos (sarasas), parasyti metodys,
# kurie prides knygas i knygyna ir atspausdinti visu knygu sarasa

# class Knygynas:
#     def __init__(self):
#         self.knygos = []
#     def prideti_knyga(self, knyga):
#         self.knygos.append(knyga)
#     def knygos_paieska(self, pavadinimas):
#         for knyga in self.knygos:
#             if knyga["pavadinimas"] == pavadinimas:
#                 return knyga
#         return None
#     def knygu_sarasas(self):
#         if not self.knygos:
#             print("Knygynas tuscias")
#         else:
#             print("Knygyno knygu sarasas: ")
#         for knyga in self.knygos:
#             print(f"Pavadinimas: {knyga['pavadinimas']}, autorius: {knyga['autorius']}, metai: {knyga['metai']}")
# knygynas = Knygynas()
# knygynas.prideti_knyga({"pavadinimas": "Metu laikai", "autorius": "Ona Petraite", "metai": 1999})
# ieskoma_knyga = knygynas.knygos_paieska("Metu laikai")
# if ieskoma_knyga:
#     print(f"Knyga rasta: {ieskoma_knyga['pavadinimas']}")
# else:
#             print("Knyga nerasta")
# knygynas.knygu_sarasas()

# Sukurkite klasę "Prekybininkas", kuri turi atributus "vardas" (name) ir "prekės" (items) ( prekių sąrašas).
# Parašykite metodus, kurie leidžia pridėti prekes prie prekių sąrašo, pašalinti prekes ir paskaičiuoti prekių bendrą sumą;

# class Prekybininkas:
#     def __init__(self, vardas):
#         self.vardas = vardas
#         self.prekes = []
#     def prideti_preke(self, preke, kiekis = 1):
#         for _ in range(kiekis):
#             self.prekes.append(preke)
#     def pasalinti_preke(self, preke, kiekis = 1):
#         if preke in self.prekes:
#             for _ in range(kiekis):
#                 self.prekes.remove(preke)
#         else:
#             print("Nera tokios prekes")
#     def prekiu_suma(self):
#         suma = sum(preke[1] for preke in self.prekes)
#         return suma
#
# pardavejas = Prekybininkas("Jonas")
# preke1 = ("Obuoliai", 2.0)
# preke2 = ("Pomidorai", 2.5)
# preke3 = ("Uogos", 3.5)
#
# pardavejas.prideti_preke(preke1, 3)
# pardavejas.prideti_preke(preke2)
# pardavejas.prideti_preke(preke3, 3)
# suma = pardavejas.prekiu_suma()
# print(suma)
# pardavejas.pasalinti_preke(preke1, 2)
# pardavejas.pasalinti_preke("preke4")
# suma = pardavejas.prekiu_suma()
#
# print("Prekiu sarasas: ")
# for preke in pardavejas.prekes:
#     print(f"{preke[0]}: {preke[1]}")
# print(f"Bendra visu prekiu suma: {suma}")



# Sukurkite klasę "Darbuotojas" (Employee), kuri turi atributus "vardas" (name), "pareigos" (position), ir "atlyginimas" (salary).
# Parašykite metodus, kurie leidžia keisti darbuotojo pareigas ir atlyginimą;
# class Darbuotojas:
#     def __init__(self, vardas, pareigos, alga):
#         self.vardas = vardas
#         self.pareigos = pareigos
#         self.alga = alga
#     def pakeisti_alga(self, nauja_alga):
#         self.alga = nauja_alga
#     def pakeisti_pareigas(self, naujos_pareigos):
#         self.pareigos = naujos_pareigos
# darbuotojas1 = Darbuotojas("Jonas", "vairuotojas", 500)
# darbuotojas1.pakeisti_alga(1500)
# darbuotojas1.pakeisti_pareigas("vadybininkas")
# print(f"{darbuotojas1.vardas}), pareigos: {darbuotojas1.pareigos}, gaunama alga: {darbuotojas1.alga}")

# Sukurkite klasę "Skaičiuotuvas", kuri turi metodus "sudėti" (add), "atimti" (subtract), "
# dauginti" (multiply) ir "dalinti" (divide). Šie metodai priima du skaičius ir atlieka atitinkamą matematinę operaciją.
#
# class Skaiciuotuvas:
#     def add(self, a, b):
#         return a + b
#     def substract(self, a, b):
#         return a - b
#     def multiply(self, a, b):
#         return a * b
#     def divide(self, a, b):
#         if b == 0:
#             return "Dalyba is 0 negalima"
#         else:
#             return a / b
#
# a = 3
# b = 0
# a1 = Skaiciuotuvas()
# suma = a1.add(a, b)
# atimtis = a1.substract(a, b)
# dalyba = a1.multiply(a, b)
# daugyba = a1.divide(a, b)
# print(f" Suma yra {suma}, skirtumas yra {atimtis}, dalyba yra {dalyba}, daugyba yra {daugyba}")

# Sukurkite klasę "Klase", kuri turės savybę "pavadinimas" ir sąrašą "pamokos" (pamokų pavadinimai ir laikas).
# Sukurkite klasę "Mokykla", kuri turės sąrašą klasių. Parašykite metodą, kuris išveda mokyklos tvarkaraštį su visomis pamokomis.

# class Klase:
#     def __init__(self, pavadinimas):
#         self.pavadinimas = pavadinimas
#         self.pamokos = []
#     def sukurti_pamoka(self, pavadinimas, laikas):
#         self.pamokos.append((pavadinimas, laikas))
#     def tvarkarastis(self):
#         tvarkarastis = f"Klase: {self.pavadinimas} \n"
#         for pamoka in self.pamokos:
#             pavadinimas, laikas = pamoka
#             tvarkarastis += f"- {pavadinimas}, laikas: {laikas} \n"
#         return tvarkarastis
#
# class Mokykla:
#     def __init__(self, pavadinimas):
#         self.pavadinimas = pavadinimas
#         self.klases = []
#     def sukurti_klase(self, klase):
#         self.klases.append(klase)
#     def Tvarkarastis_galutinis(self):
#         galutinis = f"Mokykla: {self.pavadinimas} \n"
#         for klase in self.klases:
#             galutinis += klase.tvarkarastis()
#             return galutinis
#
# klase1 = Klase("Ziopliu 9A")
# klase1.sukurti_pamoka("Nosiakrap6tis", "8:00-8:45")
# klase1.sukurti_pamoka("Kalbagrauzis", "9:00-9:45")
#
# klase2 = Klase("Smalsučiai gudručiai 1B")
# klase2.sukurti_pamoka("Priešpiečiai", "10:00-10:45")
# klase2.sukurti_pamoka("Kalbagrauzis", "11:00-11:45")
#
# mokykla =Mokykla("Tinginių pantys")
#
# mokykla.sukurti_klase(klase1)
# mokykla.sukurti_klase(klase2)
#
# tvarkarastis = mokykla.Tvarkarastis_galutinis()
#
# print(mokykla.Tvarkarastis_galutinis())

# Sukurkite klasę "Žaislas", kuri turėtų savybes, tokias kaip "pavadinimas" ir "amžiaus rekomendacija".
# Tada sukurkite klasę "Vaikas", kuri turėtų vardą ir amžių. Tada sukurkite klasę "VaikasSuZaislu",
# kuri turėtų šio vaiko objektą ir žaislo objektą. Patikrinkite, ar vaiko amžius atitinka žaislo amžiaus rekomendaciją.
#
# class Zaislas:
#     def __init__(self, pavadinimas, amziaus_rekomendacija):
#         self.pavadinimas = pavadinimas
#         self.amziaus_rekomendacija = amziaus_rekomendacija
#
# class Vaikas:
#     def __init__(self, vardas, amzius):
#         self.vardas = vardas
#         self.amzius = amzius
#
# class VaikasSuZaislu:
#     def __init__(self, vaikas, zaislas):
#         self.vaikas = vaikas
#         self.zaislas = zaislas
#     def amziaus_tikrinimas(self):
#         if self.vaikas.amzius >= self.zaislas.amziaus_rekomendacija:
#             return f"{self.vaikas.vardas} gali zaisti su zaislu '{self.zaislas.pavadinimas}'"
#         else:
#             return f"{self.vaikas.vardas} negali zaisti su zaislu '{self.zaislas.pavadinimas}' del amziaus apribojimo"
#
# zaislas1 = Zaislas("Lego", 7)
# zaislas2 = Zaislas("meskinas", 3)
# zaislas3 = Zaislas("puzzle", 13)
# vaikas1 = Vaikas("Migle", 9)
# vaikas2 = Vaikas("Ona", 2)
# vaikas3 = Vaikas("Tomas", 15)
# vaikas_su_zaislu1 = VaikasSuZaislu(vaikas2, zaislas3)
# rezultatas = vaikas_su_zaislu1.amziaus_tikrinimas()
# print(rezultatas)

# Sukurkite programą, kuri leidžia vartotojui valdyti krepšinio komandą.
# Galite kurti klases, pvz., "Komanda", "Žaidėjas", "Treneris".
# Kiekvienas žaidėjas turėtų turėti savo statistiką(taiklumas,pozicija), o treneris - instrukcijas ir strategiją(komandos sudeti).
# Programa turi leisti vartotojui pridėti naujus žaidėjus, juos treniruoti ir valdyti komandos sudeti.

# class Treneris:
#     def __init__(self):
#         self.strategija = "ataka"
#     def keisti_strategija(self, nauja_strategija):
#         self.strategija = nauja_strategija
#     def strategijos_info(self):
#         return f"Naudojama strategija {self.strategija}"
# class Zaidejas:
#     def __init__(self, pavarde, pozicija):
#         self.pavarde = pavarde
#         self.pozicja = pozicija
#         self.taiklumas = 30
#     def upgrade(self):
#         self.taiklumas += 5
#         if self.taiklumas > 100:
#             self.taiklumas = 100
#     def zaidejo_info(self):
#         return f"{self.pavarde}, zaidejo pozicija: {self.pozicja}, jo taiklumas {self.taiklumas} %"
# class Komanda:
#     def __init__(self, pavadinimas):
#         self.komanda = []
#         self.pavadinimas = pavadinimas
#         self.treneris = Treneris()
#     def prideti_zaideja(self, zaidejas):
#         self.komanda.append(zaidejas)
#     def isimti_zaideja(self, zaidejas):
#         if zaidejas in self.komanda:
#             self.komanda.remove(zaidejas)
#     def komandos_informacija(self):
#         print(f"{self.pavadinimas}, komandos zaidejai: ")
#         for zaidejas in self.komanda:
#             print(zaidejas.zaidejo_info())
#     def strategijos_info(self):
#         print(self.treneris.strategijos_info())
#     def pasirinkti_treneri(self, treneris):
#         self.komanda.append(treneris)
#     def pakeisti_treneri(self, treneris):
#         if treneris in self.komanda:
#             self.komanda.remove(treneris)
#
# komanda = Komanda("Zalgiris")
# zaidejas1 = Zaidejas("Jasaitis", "puolejas")
# zaidejas2 = Zaidejas("Mazeikis", "saugas")
# zaidejas3 = Zaidejas("Petraitis", "atsarginis")
# komanda.prideti_zaideja(zaidejas1)
# komanda.prideti_zaideja(zaidejas2)
# komanda.prideti_zaideja(zaidejas3)
# zaidejas1.upgrade()
# zaidejas1.upgrade()
# zaidejas3.upgrade()
# komanda.komandos_informacija()
# komanda.strategijos_info()

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
duomenys = {'Vardas': ['Jonas', 'Ieva', 'Petras', 'Ona'],
            'Amzius': [25, 28, 22, 30]
            }
df = pd.DataFrame(duomenys)
#pasiimti tik vardus
vardai = df['Vardas']
#jeigu norime rezultato liste, rasome
vardai = df['Vardas'].to_list()
print("Vardai: ")
print(vardai)
#
# #prideti nauja stulpeli i DataFrame
# df['Lytis'] = ['Vyras', 'Moteris', 'Vyras', 'Moteris']
# print('Atnaujintas dataframe su nauju stulpeliu: ')
# print(df)

import matplotlib.pyplot as plt
#matplotlib - atvaizduoja grafika

# plt.figure(figsize=(8,5)) #nurodome asies dydi
# plt.bar(df['Vardas'], df['Amzius'], color = 'blue') #sukuriame stulpelini grafika
# plt.xlabel('Vardas') # X asies pavadinimas
# plt.ylabel('Amzius') # Y asies pavadinimas
# plt.title('Amzius pagal vardus') #grafiko pavadinimas
# plt.show() #rodome grafika


df.head() #atvaizduoja eiluciu kieki nuo priekio
df.tail() # atvaizduoja nuo galo (paskutines pirmas eilutes)

