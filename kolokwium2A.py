import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# zadanie 1

# x = np.arange(5, 10+0.15, 0.15)
# funckja = np.tan(x) + (np.cos(x)/2)
# plt.plot(x, funckja, label='f(x) = tan(x) + cos(x)/2')
# plt.xlabel("x")
# plt.ylabel("f(x)")
# plt.xlim(5, 10)
# plt.suptitle("zadanie 1")
# plt.legend()
# plt.title("wykres f(x)=tan(x)+cos(x)/2")
# plt.savefig("zadanie1.png")
# plt.show()

# KONIEC
#
# zadanie 1 chatGPT

# def f(x):
#     return np.tan(x) + np.cos(x) / 2
#
# # Przedział x
# start = 5
# end = 10
#
# # Kroki wartości x
# step = 0.15
#
# # Generowanie wektora x
# x = np.arange(start, end + step, step)
#
# # Obliczanie wartości funkcji f(x)
# y = f(x)
#
# # Utworzenie wykresu liniowego dla f(x)
# plt.plot(x, y, label='f(x) = tan(x) + cos(x)/2')
#
# # Utworzenie wektorów dla wyświetlenia
# vector_x = np.array([start, end])
# vector_y = f(vector_x)
#
# # Utworzenie wykresu dla wektorów
# plt.plot(vector_x, vector_y, 'ro-', label='Wektory')
#
# # Dodanie etykiet do osi wykresu
# plt.xlabel('x')
# plt.ylabel('f(x)')
#
# # Ustawienie zakresu osi x na granice przedziału
# plt.xlim(start, end)
#
# # Dodanie legendy
# plt.legend()
#
# # Dodanie tytułu linii
# plt.title('Wykres funkcji f(x) oraz wektory')
#
# # Dodanie tytułu wykresu
# plt.suptitle('Wykres liniowy funkcji f(x) = tan(x) + cos(x)/2')
#
# # Wyświetlenie wykresu
# plt.show()

# KONIEC


# zadanie 1 STAROSTA


# x = np.arange(5, 10, .15)
# y = np.tan(x)+(np.cos(x)/2)
# plt.plot(x, y, label='f(x)=tan(x)+cos(x)/2')
# plt.xlabel('x')
# plt.xlabel('f(x)')
# plt.xlim(5, 10)
# plt.title('Wykres funkcji f(x)')
# plt.show()


# zadanie 2


# fig, axes = plt.subplots(2,2, figsize=(10, 8))
# x1 = np.arange(0., 10+0.15, 0.15)
# f1 = np.sin(x1) + 0.4
# axes[0, 0].plot(x1, f1, '-.r', label='sin(x)+0.4')
# axes[0, 0].set_title("Wykres sin(x)+0.4")
# axes[0, 0].set_xlabel("x")
# axes[0, 0].set_ylabel('sin(x) + 0.4')
# axes[0, 0].set_xticks([0, 2.5, 5, 7.5, 10])
# axes[0, 0].set_yticks([-0.5, 0, 0.5, 1])
# axes[0, 0].legend()
#
# x2 = np.arange(1, 6)
# f2 = (x2+5)/2
# axes[1, 1].bar(x2, f2, label="f(x)=(x+5)/2")
# axes[1, 1].set_xlabel("x")
# axes[1, 1].set_ylabel("wyniki funkcji")
# axes[1, 1].set_title("Wykres słupkowy funkcji")
# axes[1, 1].set_xticks([1, 2, 3, 4, 5])
# axes[1, 1].set_yticks([0, 1, 2, 3, 4, 5])
# axes[1, 1].legend()

# wyłączenie wykresów drugiego i trzeciego 2 układzie 2x2
# axes[0, 1].axis("off")
# axes[1, 0].axis("off")
# plt.savefig("zadanie2.png")
# plt.show()


# zadanie 2 STAROSTA bardzo dobrze zrobione


# x1 = np.arange(0, 10, .25)
# x2 = np.arange(1, 6)
# y1 = np.sin(x1)+0.4
# y2 = (x2+5)/2
#
# plt.subplot(2, 2, 1)        # <- wykres 1
# plt.plot(x1, y1, 'r-.', label='sin(x)+0.4')
# # plt.xticks([0, 2.5, 5, 7.5, 10])
# # plt.yticks([-0.5, 0, 0.5, 1])
# plt.xlabel('x')
# plt.ylabel('sin(x)+0.4')
# plt.legend(loc='lower left')
# plt.title("Wykres sin(x)+0.4")
#
# plt.subplot(2, 2, 4)        # <- wykres 2
# plt.bar(x2, y2, label='f(x)=(x+5)/2')
# plt.xticks([1, 2, 3, 4, 5])
# # plt.yticks([0, 1, 2, 3, 4, 5])
# plt.xlabel('x')
# plt.ylabel('wykres funkcji')
# plt.legend(loc='upper left')
# plt.title("Wykres słupkowy funkcji")
# plt.savefig("im_naz_zad2.png")
# plt.show()


# zadanie 3


# tabelka = pd.read_csv('glass.data', header=0, sep=',', decimal='.')
# print(tabelka)
# a = tabelka[tabelka.Magnesium > 3.6]
# new_df = a.groupby("Type of glass")
# grupa = tabelka.groupby("Type of glass").size()
# plt.pie(grupa, labels=grupa.index, autopct='%.1f%%')
# plt.legend(labels=grupa.index, loc='lower left', title="index szkła")
# plt.savefig("im_naz_zad3.png")
# plt.show()


# zadanie 4


df = pd.read_csv('glass.data')
sns.set()
plot = sns.barplot(x='Type of glass', y='Sodium', data=df,
                   estimator=np.sum, hue='Type of glass', dodge=False, errorbar=None)
sns.set_style('whitegrid')
plot.set(title="wykres słupkowy")
plt.savefig("im_naz_zad4.png")
plt.show()


