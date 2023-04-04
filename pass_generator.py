# #napisz generator haseł z zawarciem poniższych warunków:
# # zapytaj jak długie będzie hasło
# # zapytaj czy zawrzeć znaki (!@#$%)
# # zapytaj czy dodać małe litery
# # zapytaj czy dodać duże litery
# # zapytaj czy dodać <>?{}[];:'",.()|/
#
#
import random

def option():
    option = []
    run = True
    while True:
        lowercase = input('use LOWER case characters (a,b,c...) in password? ([y]/n)')
        if lowercase.lower() == 'y':
            option.append('lower')
        uppercase = input('use UPEER case characters (A,B,C...) in password? ([y]/n)')
        if uppercase.lower() == 'y':
            option.append('upper')
        numberchar = input('use numbers (1,2,3...) in password? ([y]/n)')
        if numberchar.lower() == 'y':
            option.append('number')
        numericchar = input('use special characters (!,@,#...) in password? ([y]/n)')
        if numericchar.lower() == 'y':
            option.append('special')
        enterchar = input('use special characters (,{,},[,],;...) in password? ([y]/n)')
        if enterchar.lower() == 'y':
            option.append('enter_special')
        if option != []:
            return option


def option_implementation(options):
    NUMERIC_SPECIAL_CHAR = ["!", "@", "#", "$", "%", '&', '*', '_', '-', '=', '+']
    LOWER_CASE_CHAR = ["q", 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
                       'z', 'x', 'c', 'v', 'b', 'n', 'm']
    UPPER_CASE_CHAR = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L',
                       'Z', 'X', 'C', 'V', 'B', 'N', 'M']
    ENTER_SPECIAL_CHAR = ['[', ']', '{', '}', ';', ':', '"', "'", '<', '>', '/', '|', ',', '.', '?']
    NUMBER_CHAR = ['1', '2', '3', '4', '5', '6', '7', '8', '8', '9', '0']

    ALL_USED_CHAR = []
    for i in options:
        if i == 'lower':
            ALL_USED_CHAR.append(LOWER_CASE_CHAR)
        elif i == 'upper':
            ALL_USED_CHAR.append(UPPER_CASE_CHAR)
        elif i == 'number':
            ALL_USED_CHAR.append(NUMBER_CHAR)
        elif i == 'special':
            ALL_USED_CHAR.append(NUMERIC_SPECIAL_CHAR)
        elif i == 'enter_special':
            ALL_USED_CHAR.append(ENTER_SPECIAL_CHAR)

    return ALL_USED_CHAR


def generate_password(numbers_of_char, all_used_char):
    password_list = []
    for i in range(numbers_of_char):
        rand_list_char = random.choice(all_used_char)
        password_list.append(random.choice(rand_list_char))
    passowrd = ''.join(password_list)
    return passowrd



options = option()
all_char = option_implementation(options)
print('Your generated password:', generate_password(8, all_char))

