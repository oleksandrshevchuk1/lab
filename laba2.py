my_list = [42, 7, 108, 15, 256, 99, 3, 84, 61, 12, "яблуко", "киця", "сонце", "будинок", "школа", "друг", "ніч", "місто", "музика", "книга"]

int_list = []
str_list = []
for x in my_list:
    if type(x) == int:
        int_list.append(x)
    else:
        str_list.append(x)
int_list.sort()
str_list.sort()
sort_list = int_list.copy()
sort_list.extend(str_list)
number_list = [x for x in int_list if x % 2 == 0]
upper_list = [x.upper() for x in str_list]
print("Початковий список:", my_list)
print("Посортований:", sort_list)
print("Числа без остачі:", number_list)
print("Слова Капсом:", upper_list)