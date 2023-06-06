import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# zadanie 1

# x = np.linspace(-3, 7, 35)
# print(x)
# f = ((x**2)/(np.tan(x)))+(5*x)
# plt.plot(x, f, label='f = x^2/np.tan(x) + 5x')
# plt.xlabel("x")
# plt.ylabel("wartości funkcji")
# plt.title("wykres f = x^2/np.tan(x) + 5x")
# plt.xlim(-3, 7)
# plt.legend()
# plt.savefig("im_nazw_zad1b.png")
# plt.show()


# zadanie 2
#
# x1 = np.arange(4, 10)
# f1 = np.sqrt(x1)
# x2 = np.arange(0, 10+0.1, 0.1)
# f2 = np.cos(x2) + 0.4
#
# # wykres sqrt(x)
# plt.subplot(2, 1, 1)
# plt.bar(x1, f1, label='f(x) = √x')
# plt.xlabel("x")
# plt.ylabel("wyniki funkcji")
# plt.title("Wykres słupkowy funkcji")
# plt.legend()
#
# # wykres cos(x) + 0.4
# plt.subplot(2, 1, 2)
# plt.plot(x2, f2, 'go', label='cos(x) + 0.4')
# plt.xlabel("x")
# plt.ylabel("cos(x) + 0.4")
# plt.title("Wykres cos(x) + 0.4")
# plt.legend()
#
# plt.subplots_adjust(hspace=1.2)
# plt.savefig("im_naz_zad2b.png")
# plt.show()
#
#
# # zadanie 3

# df = pd.read_csv('glass.data')
# new_df = df[df["Refractive index"] < 1.51766]
# # new_df = pd.DataFrame(new_df.groupby("Type of glass").size())
# # print(new_df)
# # ilosc = list(new_df.iloc[:, 0])     # wyciąganie konkretnej kolumny z dataframe
# # index = np.arange(1, 7)
# # plt.bar(index, ilosc)
#
# grupa = new_df.groupby("Type of glass").size()
# grupa.plot.bar()
# plt.xticks(rotation=0)
#
# plt.savefig("im_naz_zad3b.png")
# plt.show()
#
#
# # zadanie 4

# df = pd.read_csv("glass.data")
# df = df.groupby('Type of glass')['Aluminum'].sum()
# df.plot(kind='pie', subplots=True, autopct='%.2f %%', fontsize=14, figsize=(6, 6))
# plt.legend()
# plt.pie()
# plt.title("zużycie Aluminium")
# plt.savefig('im_naz_zad4b.png')
# plt.show()

df = pd.read_csv('glass.data', header=0, sep=',', decimal='.')
print(df)
grupa = df.groupby('Type of glass').agg('Aluminum').sum()
wedges, texts, autotext = plt.pie(x=grupa, labels=grupa.index, autopct=lambda pct: "{:.1f}%".format(pct),
                                  textprops=dict(color='black'))
plt.legend(title='klasy')
plt.show()
