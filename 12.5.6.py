string = input("Введите числа через пробел:")

list_of_strings = string.split() # список строковых представлений чисел
list_of_numbers = list(map(int, list_of_strings)) # список чисел
print(list_of_numbers)
list_of_numbers[0], list_of_numbers[-1] = list_of_numbers [-1], list_of_numbers[0]
print(list_of_numbers)

print(sum(list_of_numbers[:])) # sum() вычисляет сумму элементов списка