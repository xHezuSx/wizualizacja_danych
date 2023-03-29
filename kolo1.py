# kolo:
# try except
# funckja
# wczytanie i operacja na pliku
# list comprehention / operacja na liście
# jakiś wzorek matematyczny

import math

# zad 1
def zad1():
    try:
        a = int(input("a: "))
        b = int(input("b: "))
        ans = (a**2) + (a*b) + (b**2)
        with open('kolo1_1.txt', 'w') as f:
            f.write(str(ans))
            print("wynik zapisano pomyślnie")
    except:
        print("nieprawidłowy typ danych lub nie poprawna ścieżka do pliku")


# zad 2
def zad2(list1, list2):
    list3 = []
    for i in range(len(list1)):
        k = list2[i] + list1[i]
        list3.append(k)
    return list3

list1= [1,2,3]
list2 = [2,3,4, 5]

# zad 3
def zad3():
    with open('kolo1_2.txt', 'r', encoding='utf-8') as f:
        txt = f.read()
        txt = txt[99:135]
        counter = 0
        upper = ""
        for i in txt:
            if i.isupper():
                upper += i
                counter += 1
        if counter == 0:
            print("brak wielkich liter w zmiennej")
        else:
            print(upper)
            print("ilość:",counter)


# zad 4
def zad4():
    lista = [1,2,3,4,5]
    a = 3
    lista2 = [i for i in lista if i > a]
    print(lista2)


# zad 5
def zad5():
    matematyka = (math.exp(3) + (math.cos(39)) ** 2) ** (1 / 5) + ((3 / 5)) ** 3 + math.pi
    print(matematyka)
