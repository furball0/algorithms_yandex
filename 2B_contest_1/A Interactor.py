# Лена руководит разработкой тестирующей системы, в которой реализованы интерактивные задачи.
# До заверщения очередной стадии проекта осталось написать модуль, определяющий итоговый вердикт системы
# для интерактивной задачи. Итоговый вердикт определяется из кода завершения задачи, вердикта интерактора и
# вердикта чекера по следующим правилам:
#
# Вердикт чекера и вердикт интерактора — это целые числа от 0 до 7 включительно.
# Код завершения задачи — это целое число от -128 до 127 включительно.
# Если интерактор выдал вердикт 0, итоговый вердикт равен 3 в случае, если программа завершилась с ненулевым кодом, и
# 	вердикту чекера в противном случае.
# Если интерактор выдал вердикт 1, итоговый вердикт равен вердикту чекера.
# Если интерактор выдал вердикт 4, итоговый вердикт равен 3 в случае, если программа завершилась с ненулевым кодом, и
# 	4 в противном случае.
# Если интерактор выдал вердикт 6, итоговый вердикт равен 0.
# Если интерактор выдал вердикт 7, итоговый вердикт равен 1.
# В остальных случаях итоговый вердикт равен вердикту интерактора.
# Ваша задача — реализовать этот модуль.

# Входной файл состоит из трёх строк. В первой задано целое число r (-128 <= r <= 127) — код завершения задачи,
# во второй — целое число i (0 <= i <= 7) - вердикт интерактора,
# в третьей — целое число c (0 <= c <= 7) - вердикт чекера.

# ans - итоговый вердикт

nums = [int(input()) for _ in range(3)]
r, i, c = nums[0], nums[1], nums[2]
# i = 1, 0 , 4, 6, 7 то if
# i = 2,3,5 -> ans = i
if i in (0, 1, 4, 6, 7):
	if i == 0:
		if r != 0:
			ans = 3
		else:
			ans = c

	if i == 1:
		ans = c

	if i == 4:
		if r != 0:
			ans = 3
		else:
			ans = 4

	if i == 6:
		ans = 0

	if i == 7:
		ans = 1
else:
	ans = i

print(ans)