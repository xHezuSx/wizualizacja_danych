import math
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# zadanie 1
# Za pomocą bibliotek matplotlib utwórz wykres liniowy funkcji f(x)=(x^2+3x)/5 + sin(x) dla
# wartości x z przedziału [-3,5], wartości x zmieniają się co 0.3. Dodaj odpowiednie etykiety do
# osi wykresu, tytuł linii, legendę oraz tytuł wykresu. Dodatkowo wyświetl oba wektory
# przekazywane na wykres. Ustaw zakres oś x na granice przedziału

# x = np.arange(-3, 5 + 0.3, 0.3)
# y = ((x ** 2) + 3 * x) / 5 + np.sin(x)
# plt.plot(x, y, 'r', label='(x^2+3x)/5 + sin(x)')
# print(x)
# print(y)
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.xlim(-3, 5)
# plt.suptitle("zadanie 1")
# plt.title('Wykres liniowy funki')
# plt.legend()
# plt.savefig('Dawid_Kaczynski_zad1.png')
# plt.show()

# zadanie 2

# fig, axs = plt.subplots(2,1)
# x = np.arange(-1, 1+0.1, 0.1)
# y = np.cos(x) * np.sin(x)
# y2 = np.cos(x) - np.tan(x)
# axs[0].plot(x, y, label ='cos(x)*sin(x)')
# axs[0].plot(x, y2,'orange', label ='cos(x)-tan(x)')
# axs[0].set_xlabel('x')
# axs[0].set_ylabel('Wynik funkcji')
# axs[0].set_title('Wykres dwóch funkcji')
# axs[0].legend(loc='upper right')
# axs[0].set_xlim(-1, 1)
# # √
# x2 = np.arange(1, 4+1, 1)
# y2 = (x2**2)/np.sqrt(x2)
# axs[1].plot(x2, y2, '>y',  label ='f(x) = x^2/√x')
# axs[1].set_xlabel('x')
# axs[1].set_ylabel('Wynik funckji')
# axs[1].set_title('Wykres funkcji')
# axs[1].legend(loc='upper left')
#
# plt.subplots_adjust(hspace= 1.5)
#
# plt.savefig('Dawid_Kaczynski_zad2.png')
# plt.show()


# zadanie 3

# plik = pd.read_csv('glass.data')
# df = plik[plik['Type of glass'].isin([6,7])]
# df = df.groupby("Type of glass").size()
# # print(pd.DataFrame(df))
# plt.pie(df, labels=df.index, autopct='%.1f%%')
# plt.legend(loc='lower left', title="index")
# plt.savefig("Dawid_Kaczynski_zad3.png")
# plt.show()


# zadanie 4
# plik = pd.read_csv('glass.data')
# sns.set()
# df = plik[["Sodium","Magnesium","Aluminum","Silicon","Potassium","Calcium","Barium", "Iron","Type of glass"]].groupby('Type of glass').size()
# sns.barplot(x=df.index, y=df, errorbar=None)
# sns.set_style("whitegrid")
# plt.xlabel('type of glass')
# plt.ylabel("ilość typu szkła")
# plt.title("wykres słupkowy szkła")
# plt.savefig("im_nazw_zad4C.png")
# plt.show()



