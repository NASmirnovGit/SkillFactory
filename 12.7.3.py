money = int(input('Введите величину депозита:'))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
# Создаем копию словаря
deposit_dict = per_cent.copy()
# Заменяем значения в словаре
deposit_dict.update([('ТКБ', int(per_cent['ТКБ'] * money / 100)), ('СКБ', int(per_cent['СКБ'] * money / 100)),
                     ('ВТБ', int(per_cent['ВТБ'] * money / 100)), ('СБЕР', int(per_cent['СБЕР'] * money / 100))])
deposit_list = [int(per_cent['ТКБ'] * money / 100), int(per_cent['СКБ'] * money / 100),
                int(per_cent['ВТБ'] * money / 100), int(per_cent['СБЕР'] * money / 100)]
print('Вывод заработка в виде словаря:\n', deposit_dict,'\nВывод заработка в виде списка:\n',
      deposit_list, '\nМаксимальная сумма, которую вы можете заработать — ', max(deposit_list))
