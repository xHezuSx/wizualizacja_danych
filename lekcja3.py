import math
# zad 1
print("e^10:  ", math.exp(10))
print("to dziwne i duże: ", (math.log(5 + (math.sin(8)) ** 2)) ** (1 / 6))
print("zaokrąglenie w dół: ", math.floor(3.55))
print("zaokrąglenie w górę: ", round(4.80))

# zad 2
imie = "JAKUB"
nazwisko = "ŻAKOWSKI"
imie = imie.lower()
nazwisko = nazwisko.lower()
print(imie.capitalize(), nazwisko.capitalize())

# zad 3
piosenka = "Little star Feels like you fell right on my head Gave you away to the wind I hope it was worth it in the end You and my guitar I think you may be my only friend I gave it all to see you shine again I hope it was worth it in the end I hope it was worth it in the end"
print(piosenka.count("I"))

# zad 4
dowolna_zmienna_lancuchowa = "qwerty123"
print("druga:",dowolna_zmienna_lancuchowa[1], "\nostatnia", dowolna_zmienna_lancuchowa[-1])

# zad 5
print(piosenka.split())

# zad 6
napis = "napis"
zmiennoprzecinkowy = 5.11
szensstacie = 0xAAA
print(napis, zmiennoprzecinkowy, '{0:X}'.format(szensstacie))

# zad 7
sporty = ["piłka", "koszykówka", "siotkówka", "uno", "cs:go", "valorant"]
sporty = sporty[::-1]
print(sporty)
pozycja = sporty.index("valorant")
sporty.pop(pozycja)
sporty.insert(len(sporty),"valorant")
print(sporty)

# zad 8
slownik = {"p.s":"post scriptum",
           "itp":"i temu podobne",
           "itd":"i tak dalej"}

# zad 9
gry = {"minecraft" : "survival",
       "the wither 3" : "RPG",
       "cs:go":"naparzanka"}
j=0
for i in gry:
    j += 2
print("liczba elementów w grach to:", j)

# zad 10

x = input("podaj jakies zdanie: ")
print("litery 'a', wystąpiło: ", x.count("a"))

# zad 11

a = input("wpisz pierwszą liczbe całkowta: ")
b = input("wpisz druga liczbe całkowta: ")
c = input("wpisz ttrzecia liczbe całkowta: ")

a = int(a)
b = int(b)
c = int(c)

if(a>= b and a >= c):
    print(a, "jest największe spośród podanych liczb" )
elif b>=c and b>=a:
    print(b,"jest największą spośród podanych liczb")
else:
    print(c, "jest najlepsza spośród podanych liczb")

# zad 12

lista_liczb = [1,2.3,12,4.2]
lista_liczb2 = []
for i in lista_liczb:
    lista_liczb2.append(i**2)
del lista_liczb
print(lista_liczb2)

# zad 13

parzyste = []
i = 0
while i < 10:
    i += 1
    x = input("podaj liczbe całkowitą: ")
    x = int(x)
    if x % 2 == 0:
        parzyste.append(x)

print(parzyste)