import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# zadanie 1

# x = np.linspace(-3, 5, 25)
# f = (8*(x**2)/4) + np.cos(x)
# print(x)
# print(f)
# plt.plot(x, f, label='8*x^2/4 + np.cos(x)')
# plt.xlabel("x")
# plt.ylabel("wartości f(x)")
# plt.title("wykres (8*(x**2)/4) + np.cos(x)")
# plt.xlim(-3, 5)
# plt.legend()
#plt.savefig("im_naz_zad1C.png")
# plt.show()


# zadanie 2

# x1 = np.arange(-3, 3+0.1, 0.1)
# f1 = (x1**2)+5
# x2 = np.arange(-3, 3+0.1, 0.1)
# f2 = (x2**2) + 5
# f3 = (-x2**2) + 4*x2
#
# plt.subplot(1, 2, 1)        # <- wykres 1
# plt.plot(x1, f1, label='x^2+5')
# plt.xlim(-3, 3)
# plt.xticks([-3, 0, 3])
# plt.subplots_adjust(wspace=1)
# plt.title("wykre f(x)")
# plt.xlabel('x')
# plt.ylabel("wartości funkcji")
# plt.legend(loc='upper center')
#
# plt.subplot(1, 2, 2)        # <- wykres 2
# plt.plot(x2, f2, 'ro', label='x^2+5')
# plt.plot(x2, f3, 'go', label='-x^2+4x')
# plt.legend()
# plt.title('wykres dwóch funkcji')
# plt.xlabel("x")
# plt.ylabel("wartości funkcji")
# plt.xlim(-3, 3)
# plt.xticks([-3, 0, 3])
# plt.savefig("im_naz_zad2C.png")
# plt.show()


# zadanie 3

# plik = pd.read_csv("glass.data")
# df = plik.sample(n=100, replace=False)
# df = df.groupby("Type of glass").agg('Aluminum').sum()
# plt.pie(df, labels=df.index, autopct='%.2f%%')
# plt.legend()
# plt.savefig("im_naz_zad3C.png")
# plt.show()


# zadanie 4

plik = pd.read_csv("glass.data")
df = plik[["Sodium","Magnesium","Aluminum","Silicon",
           "Potassium","Calcium","Barium", "Iron","Type of glass"]].groupby('Type of glass').sum()

print(df)
sns.set()
sns.barplot(df, errorbar=None, label=df.columns)
sns.set_style("whitegrid")
plt.xlabel('type of glass')
plt.ylabel("ilość typu szkła")
plt.title("wykres słupkowy szkła")
plt.legend()
plt.savefig("im_naz_zad4C.png")
plt.show()


