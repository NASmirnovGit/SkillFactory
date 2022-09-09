a = list(input("Введите первую строку: "))
b = input("Введите вторую строку: ")
print(a,b)
a_set, b_set = set(a), set(b.split()) # используем множественное присваивание
print(a_set, b_set)
a_and_b = a_set.symmetric_difference(b_set)

print(a_and_b)