# Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
# Элементы нужно выводить в том порядке, в котором они встречаются в списке.
#
# Формат ввода
# Вводится список чисел. Все числа списка находятся на одной строке.
#
# Формат вывода
# Выведите ответ на задачу.
#

lst = list(map(int, input().split()))

min_value = min(lst)
max_value = max(lst)

dct = {i:0 for i in range(min_value, max_value+1)}
for i in range(len(lst)):
	dct[lst[i]] += 1
for i in range(len(lst)):
	if dct[lst[i]] == 1:
		print(lst[i], end=' ')