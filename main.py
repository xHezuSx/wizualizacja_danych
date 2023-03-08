import numpy
import pandas
import matplotlib
import math

lista = [1, 2, 3]

# dodać elementy na wybrane miejsce
zad1 = lista
zad1.insert(3, 2)
print(zad1, "dodać elementy na wybrane miejsce")

# dodać kilka elementów
zad2 = lista
zad2a = lista
zad2.extend(zad2a)
print(zad2, "dodać kilka elementów")

# usunąć element z listy o danej pozycji
zad3 = lista
zad3.remove(2)
print(zad3, "usunąć element z listy o danej pozycji")

# usunąć element z listy o danej wartości
zad4 = lista
zad4.pop(2)
print(zad4,"usunąć element z listy o danej wartości")

# reverse list
print(lista[::-1],"odwrócić liste")

# sorting
lista.sort()
print(lista, "sortowanie\n\n\n")

# DICTS
slownik = {"a": 0, "b": 1, "c": 2, "d": 3}
print(slownik)


# dodanie
slownik["e"] = 4
print(slownik)

# usuwanie
slownik.pop("a")
print(slownik)

# klucze
print(slownik.keys())

# wartosci
print(slownik.values())

# wydobycie

print(slownik.get("c"))

# Words


print("moja liczba to {} a ty masz {} zębów".format(12, 6))

instrukcja1 = "123"
instrukcja2 = "321"

warunek1 = True
warunek2 = False
if warunek1:
    print(instrukcja1)
    print(instrukcja2)
elif warunek2:
    print("to i tak sie nie wykona")
else:
    print("to też się nie wykona\n\n\n")


# x = int(input("podaj wartość: "))
# y = int(input("podaj wartość: "))
# if(x == y):
#     print("liczy są równe")
# else:
#     print("liczby są różne")

# loops

for i in range(len(lista)):
    print(lista[i], end=' ')
else:
    print("loops end here")


# licznik = 0
# while licznik != len(lista):
#     print(lista[licznik], end=" ")
#     licznik += 1

liczby = [1, 2, 2, 2, 3, 4, 5, 2]
# x = int(input("podaj liczbe całkowitą: "))
# i = 0
# while x != len(liczby):
#     if x - liczby[i] == 0:
#         print("{} - {} = 0".format(liczby[i], x))
#         break
#     i += 1
print("\n\n\n\n")
i = 0
while i < len(liczby):
    if liczby[i] == 2:
        liczby.pop(i)
    else:
        i += 1

print(liczby)







