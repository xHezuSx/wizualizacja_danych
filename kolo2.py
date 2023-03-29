import math

# zad 1
def zad1():
    with open('kolo2_1', 'r', encoding='utf-8') as f:
        x = f.read()
        x = x[40:71]
        counter = 0
        for i in x:
            if i == 'A':
                counter += 1
        if counter == 0:
            print("nie znaleziono 'A' w tekście")
        else:
            print("znaleziono ", str(counter))


# zad 2
def zad2():
    lista1 = [1.32, 2.32, 3.32, 4, 5.32]
    lista2 = [i for i in lista1 if isinstance(i, float)]
    print(lista1)
    print(lista2)


# zad 3
def zad3(lista):
    a1 = lista[0]
    for i in range(len(lista)):
        lista.append(lista[i] + a1)
    return lista

lista1 = [1,2,3.21,12]
#print(zad3(lista1))


# zad 4
def zad4():
    matematyka = ((math.sin(56)) ** 2) + (((4 ** 2) / 25) + math.log(85, 3)) ** (1/4)
    print(round(matematyka, 2))


# zad 5
def zad5():
    try:
        n = int(input("n: "))
        wyn = 0
        for i in range(n):
            wyn += (i+1)
        with open('kolo2_2.txt', 'w') as f:
            f.write(str(wyn))
            print("operacja udana")
    except:
        print("nieprawidłowe dane wejściowe")
