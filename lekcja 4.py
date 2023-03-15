import math
import random



def zad1():
    A = [x+1 for x in range(10)]
    print("A:",A)
    B = [4**x for x in range(8)]
    print("B:",B)
    C = [x for x in B if x % 2 == 0]
    print("C:",C)


def zad2():
    lista1 = []
    for i in range(10):
        x = random.randint(1,100)
        lista1.append(x)
    print("lista 1: ",lista1)
    lista2 = [i for i in lista1 if i % 2 == 0]
    print("lista 2:",lista2)

def zad3():
    slownik = {"kinder country":"sztuki",
               "banany":"kg",
               "pwio":"sztuki",
               "jabłka":"kg"}
    lista = [i for i, j in slownik.items() if j == "sztuki"]
    print(lista)


def zad4(a,b,c):
    if (a**2) + (b**2) == (c**2):
        return True
    return False


def zad5(a=1, b=1, h=1):
    p = ((a+b)*h)/2
    return p


def zad6(a=1, b=4, ile=10):
    suma = 1
    for i in range(ile):
        suma = a*suma
        a = a*b
    return suma

def zad7(*argument):
    suma = 1
    iloczyn = 4
    for i in argument:
        suma = suma*i*iloczyn
    return suma



def zad8(**lista_zakupow):
    zakupy = []
    suma = 0
    for k in lista_zakupow:
        zakupy.append(k)
        suma = lista_zakupow[k] + suma
    return zakupy, suma


def zad9(x):
    try:
        print(math.sqrt(x))
    except:
        print("BŁĄD! ujemna wartość")

