def sort_list(numbers):  # функция сортировки списка вставками
    for i in range(1, len(numbers)):
        x = numbers[i]
        idx = i
        while idx > 0 and numbers[idx - 1] > x:
            numbers[idx] = numbers[idx - 1]
            idx -= 1
        numbers[idx] = x
    return numbers


def number_index(numbers, num):  # Функция поиска индекса числа после которого будет подставляемое число
    n_idx = 0
    if num < numbers[-1]:  # Проверяем меньше ли подставляемое максимального в списке
        for i in range(len(numbers)):
            if numbers[i] < num <= numbers[i+1]:
                n_idx = i
                break
            else:
                n_idx = 0
    else:
        n_idx = 'len(list) - 1'
    return n_idx


try:
    string = input('Введите целые числа через пробел, которые хотите отсортировать:')
    n = int(input('Введите подставляемое целое число:'))
    list_of_strings = string.split()
    list_of_numbers = list(map(int, list_of_strings))  # список чисел
except ValueError as e:
    print(f'Текст ошибки: {e}\nВведенные числа не удовлетворяют условиям')
else:
    if len(list_of_numbers) <= 1:
        print(f'Вы ввели только одно число {list_of_numbers}, сортировать нечего')
    else:
        sortlist = sort_list(list_of_numbers)
        if n <= sortlist[0]:  # Если подставляемое число меньше минимального в списке
            print(f'Отсортированый список введеных чисел: {sortlist}\nПодставляемое число "{n}" будет в начале списка')
        if n > sortlist[-1]:  # Если подставляемое число больше максимального в списке
            print(f'Отсортированый список введеных чисел: {sortlist}\nПодставляемое число "{n}" будет в конце списка')
        if sortlist[0] < n < sortlist[-1]:
            index = number_index(sortlist, n)
            print(f'Отсортированый список введеных чисел: {sortlist}\nИндекс числа предыдущего подстовляемому: {index}')
finally:
    print("Выход из программы")
