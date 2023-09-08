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
# sudetis = 5 + 5
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

temperaturos = [9, 15, 27, 23, 20, 29]


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