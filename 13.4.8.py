try:
    n = input('Введите число:')
    n = int(n)
except ValueError as e:
    print(e)
    print("Вы ввели не число")
else:  # код в блоке else выполняется только в том случае, если код в блоке try выполнился успешно (т.е. не вылетело никакого исключения).
    print(f'Вы ввели {n}')
finally:  # код в блоке finally выполнится в любом случае при выходе из try-except
    print("Выход из программы")

