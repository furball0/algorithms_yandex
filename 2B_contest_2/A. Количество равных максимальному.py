# Последовательность состоит из натуральных чисел и завершается числом 0.
# Всего вводится не более 10000 чисел (не считая завершающего числа 0).
# Определите, сколько элементов этой последовательности равны ее наибольшему элементу.
#
# Числа, следующие за числом 0, считывать не нужно.
#
# Формат ввода:
# Вводится последовательность целых чисел, оканчивающаяся числом 0 (само число 0 в последовательность не входит).
#
# Вывести ответ

def max_element_count(seq):
	max_el = seq[0]
	for i in seq:
		if i > max_el:
			max_el = i
	counter = 0
	for i in range(len(seq)):
		if seq[i] == max_el:
			counter += 1
	return counter

def input_function():
	first = int(input())
	sequence = []
	while first != 0:
		sequence.append(first)
		first = int(input())
	return sequence

print(max_element_count(input_function()))



