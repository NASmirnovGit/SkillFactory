def sort_list(list): # функция сортировки списка вставками
    for i in range(1, len(list)):
        x = list[i]
        idx = i
        while idx > 0 and list[idx - 1] > x:
            list[idx] = list[idx - 1]
            idx -= 1
        list[idx] = x
    return list


def number_index(list, n): # Функция поиска индекса числа после которого будет подставляемое число
    n_idx = 0
    if n < list[-1]: # Проверяем меньше ли подставляемое максимального в списке
        for i in range(len(list)):
            if list[i] < n and list[i+1] >= n:
                n_idx = i
                break
            else:
                n_idx = 0
    else:
        n_idx = len(list) - 1
    return n_idx


try:
    string = input('Введите числа через пробел:')
    n = int(input('Введите подставляемое число:'))
except ValueError as e:
    print(f'Текст ошибки: {e}\nВы ввели не число')
else:
    list_of_strings = string.split()
    list_of_numbers = list(map(int, list_of_strings))  # список чисел
    list = sort_list(list_of_numbers)
    if n < list[0]: # Если подставляемое число меньше минимального в списке
        print(f'Отсортированый список введеных чисел: {list} \nПодставляемое число "{n}" будет в начале')
    else:
        index = number_index(list, n)
        print(f'Отсортированый список введеных чисел: {list} \nИндекс числа предыдущего подстовляемому: {index}')
finally:
    print("Выход из программы")


