import random
# zad 1
def zad1():
    with open('lekcja5.txt', 'w', encoding='utf-8') as zad1:
        for i in range(5):
            x = random.randint(0,30)
            x *= 2
            zad1.write(str(x))
# zad 2

def zad2():
    with open('lekcja5.txt', 'r', encoding='utf-8') as zad2:
        x = zad2.readline()
        print(x)



# zad 3
def zad3():
    with open('lekcja5.txt', 'w', encoding='utf-8') as zad3:
        n = input("ile linii tekstu piszemy?")
        for i in range(int(n)):
            x = input("twój tekst w linii "+str(i+1)+": ")
            zad3.write(x)
            zad3.write("\n")

# zad 4
class NaZakupy():
    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed
    def wyswietl_produkt(self):
        print(self.nazwa_produktu, self.jednostka_miary, self.cena_jed)
    def ile_produktu(self):
        print(self.ilosc, self.jednostka_miary)
    def ile_kosztuje(self):
        cena = self.cena_jed * self.ilosc
        print(cena, "zł")

# kartofle = NaZakupy("kartofel", 10, "kg", 2.5)
# kartofle.wyswietl_produkt()
# kartofle.ile_produktu()
# kartofle.ile_kosztuje()


# zad 5
class CiagArytmetyczny():
    roznica = 5
    a1 = 1
    an = 10
    wyrazy = []
    def __init__(self, roznica, a1, an):
        self.roznica = roznica
        self.a1 = a1
        self.an = an
    def wyswitel_dane(self):
        print("różnica:", self.roznica, "\na1:", self.a1, "\nan:", self.an)
    def pobierz_elementy(self):
        x = int(input("wpiszuję tyle wartości: "))
        for i in range(x):
            x = float(input("element nr "+str(i+1)+":"))
            self.wyrazy.append(x)
    def pobierz_parametry(self):
        self.roznica = float(input("różnica: "))
        self.a1 = float(input("pierwszy wyraz: "))
        self.an = float(input("ostatni wyraz: "))
    def policz_sume(self):
        suma = self.a1
        for i in range(int(self.an)):
            suma += self.roznica
        print(suma)
    def policz_elementy(self):
        if self.a1 != None and self.roznica != None:
            x = 0
            for i in self.wyrazy:
                x = i
            print(x)

#ciag1 = CiagArytmetyczny(10, 10 ,10)
# ciag1.wyswitel_dane()
#ciag1.pobierz_elementy()
# ciag1.pobierz_parametry()
# ciag1.policz_sume()
#ciag1.policz_elementy()

class Robaczek():
    def __init__(self, x=0, y=0, krok=10):
        self.x = x
        self.y = y
        self.krok = krok
    def w(self, liczba_krokow):
        self.y += liczba_krokow*self.krok
    def s(self, liczba_krokow):
        self.y -= liczba_krokow*self.krok
    def d(self, liczba_krokow):
        self.x += liczba_krokow*self.krok
    def a(self, liczba_krokow):
        self.x -= liczba_krokow*self.krok
    def gdzie_jestem(self):
        print("x:", self.x, "\ny:", self.y)


robaczek = Robaczek()
robaczek.w(1)
robaczek.s(2)
robaczek.d(1)
robaczek.a(3)
robaczek.gdzie_jestem()













