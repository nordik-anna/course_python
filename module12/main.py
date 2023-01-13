per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input())
tkb = per_cent['ТКБ']
ckb = per_cent['СКБ']
vtb = per_cent['ВТБ']
sber = per_cent['СБЕР']
sumvkl = []
sumvkl.append(money / 100 * tkb)
sumvkl.append(money / 100 * ckb)
sumvkl.append(money / 100 * vtb)
sumvkl.append(money / 100 * sber)
m=max(sumvkl)
print('Максимальная сумма, которую вы можете заработать' , m) 