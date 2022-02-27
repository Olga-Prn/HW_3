# В проекте создать новый модуль 3seq.py. Задание:
#
# Пользователь вводит элементы 1-го списка (по очереди как в МОДУЛЬ 1 или вместе как в МОДУЛЬ 2)
# Затем он вводит элементы 2-го списка
# Удалить из первого списка элементы присутствующие во 2-ом и вывести результат на экран
# Пример работы: Введите элементы 1-го списка: 1,2,3,4,5
# Введите элементы 2-го списка: 2,5
# Результат: 1,3,4
def list_number(num_user):
    split = [',',';','/']
    j = 0
    while j != 1:
        number_str  = input('Введите элементы списка № {}, используя разделитель '.format(num_user))
        for user_split in split:
            if number_str.find(user_split) != -1:
                j += 1
                split_enter = user_split
        if j > 1:
            print('используйте один из следующих разделителей: запятую(,), точку с запятой(;), слэш(/)')
            j = 0
    list_n = list(set(number_str))
    list_n.remove(str(split_enter))
    list_n = [int(x) for x in list_n]
    return list_n

list_1 = list_number(1)
list_2 = list_number(2)

list_3=list(set(list_1)-set(list_2))
print('результат:', end = ' ')
for x in list_3:
    print(x, end=', ')
