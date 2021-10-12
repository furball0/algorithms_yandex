# Август и Беатриса играют в игру.
# Август загадал натуральное число от 1 до n.
# Беатриса пытается угадать это число, для этого она называет некоторые множества натуральных чисел.
# Август отвечает Беатрисе YES, если среди названных ей чисел есть задуманное или NO в противном случае.
# После нескольких заданных вопросов Беатриса запуталась в том,
# какие вопросы она задавала и какие ответы получила и просит вас помочь ей определить, какие числа мог задумать Август.
#
# Формат ввода
# Первая строка входных данных содержит число n — наибольшее число, которое мог загадать Август.
# Далее идут строки, содержащие вопросы Беатрисы. Каждая строка представляет собой набор чисел, разделенных пробелами.
# После каждой строки с вопросом идет ответ Августа: YES или NO.
# Наконец, последняя строка входных данных содержит одно слово HELP.
#
# Формат вывода
# Вы должны вывести (через пробел, в порядке возрастания) все числа, которые мог задумать Август.

dct = {}
n = int(input())
all_nums = {i for i in range(1, n)}
answer = all_nums
while True:
	nums = input()
	if nums == 'HELP':
		break
	nums = set(map(int, nums.split()))
	status = input()
	if status == 'YES':
		answer &= nums
	else:
		answer -= nums
for el in sorted(list(answer)):
	print(el, end=' ')


