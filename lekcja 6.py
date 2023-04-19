import numpy as np
import math as m

def zad1():
    matriks1 = np.array([1,2,3])
    matriks2 = np.array([4,5,6])
    wyn = matriks2 * matriks1
    print(wyn)


def zad2():
    matriks1 = np.array([[1,2,3],
                         [4,5,6],
                         [7,-8,9]])

    matriks2 = np.array([[1,2,3,4],
                         [5,6,7,8],
                         [9,10,11,12],
                         [13,14,15,16]])

    rzad1 = matriks1.min(axis=0)
    rzad2 = matriks2.min(axis=0)
    columna1 = matriks1.min(axis=1)
    columna2 = matriks2.min(axis=1)
    print(rzad1, rzad2, columna1, columna2)



def zad3():
    matriks1 = np.array([1, 2, 3])
    matriks2 = np.array([4, 5, 6])
    print(matriks1.dot(matriks2))


def zad4():
    matriks1 = np.array([1,2,3])
    matriks2 = np.array([m.pi, m.e, -128.34])
    print(matriks1*matriks2)


def zad5():
    matriks = np.array([[1,2,3],
                       [4,5,6]])
    a = np.sin(matriks)
    print(a)


def zad6():
    matriks = np.array([[1, 2, 3],
                        [4, 5, 6]])
    b = np.cos(matriks)
    print(b)


def zad7(m1, m2):
    print(m1+m2)


def zad8():
    matriks = np.array([[1,2,3],
                        [4,5,6],
                        [7,8,9]])
    for i in matriks:
        print(i)


def zad9():
    matriks = np.arange(9).reshape(3, 3)
    for i in matriks.flat:
        print(i)


def zad10():
    matriks = np.arange(81).reshape(9, 9)
    print(matriks)
    matriks = matriks.reshape(1, 81)
    print(matriks)
    matriks = matriks.reshape(81,1)
    print(matriks)
    matriks = matriks.reshape(27, 3)
    print(matriks)
    matriks = matriks.reshape(3, 27)
    print(matriks)

def zad11():
    matriks = np.arange(12).reshape(3, 4)
    kob1 = matriks.reshape(4, 3)
    kob2 = matriks.reshape(2, 6)
    kob1 = np.ravel(kob1)
    kob2 = np.ravel(kob2)
    print(kob1)
    print(kob2)

