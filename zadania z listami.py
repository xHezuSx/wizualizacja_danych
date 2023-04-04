# Zadanie 1
# Napisz metodę, która sprawdzi, czy podana wartość val znajduje się w liście liczb digits. Szkielet funkcji znajdziesz poniżej.
# from typing import List
# def f(val: int, digits: List[int]) -> bool
# # write code here
# pass
# W celu ułatwienia Ci zadania, poniżej masz kawałek kodu, który przygotuje Ci losowe liczby do testowania Twojej metody.
# from random import randint
#  # Liczba elementów do wylosowania
# digits_example = [randint(-1000, 1000) for _ in range(n)]
# * Możesz zaszaleć i zobaczyć jak długo Twój kod wykonuje się przy np. milionie elementów w liście. - Czy Twoje podejście jakkolwiek się zmieni, jeżeli wiesz, że liczba elementów będzie duża?

                                                        # ZADANIE 1
print("\t\t\t\t\t\t\t\tZADANIE 1")
from random import randint
from typing import List

def f(value: int, digits: List[int]) -> bool:
    for numb in digits:
        if value == numb:
            return True
    return False

n = 100000
numbers: list = [randint(-10000, 10000) for _ in range(n)]
value: int = -2

result = f(value, numbers)

print(result)




# Zadanie 2
# Użytkownik podaje liczbę w zakresie od 101 - 99999.
# Napisz program, który zamieni kolejnością cyfry w podanej liczbie.
# Przykład
# 365 -> 563
# 90238 -> 83209
                                                        # ZADANIE 2
print("\t\t\t\t\t\t\t\tZADANIE 2")
while True:
    try:
        numb: int = int(input("Give me number in range 101-99999: "))
        if numb >= 101 and numb <= 99999:
            break
        else:
            print("that not what i was expecting (-_-)")
    except:
        print("that not what i was expecting (-_-)")

string: str = str(numb)
my_list: list = list(string)
my_sequance: List[list] = my_list
my_list.reverse()
str_again:str = (''.join(my_list))
int_again:int = int(str_again)

print(int_again)

