money = int(input('Введите величину депозита:'))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
#Создаем список значений процентной ставки в разных банках
stavka = list(per_cent.values())
#Создаем пустой список для внесения в него значений заработка
deposit = []
deposit.append(int(stavka[0]*money/100))
deposit.append(int(stavka[1]*money/100))
deposit.append(int(stavka[2]*money/100))
deposit.append(int(stavka[3]*money/100))
print(deposit, '\nМаксимальная сумма, которую вы можете заработать — ', max(deposit))
