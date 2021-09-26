# На Новом проспекте построили подряд 10 зданий.
# Каждое здание может быть либо жилым домом, либо магазином, либо офисным зданием.
# Но оказалось, что жителям некоторых домов на Новом проспекте слишком далеко приходится идти до ближайшего магазина.
# Для разработки плана развития общественного транспорта на Новом проспекте мэр города попросил вас выяснить,
# какое же наибольшее расстояние приходится преодолевать жителям Нового проспекта, чтобы дойти от своего дома до
# ближайшего магазина.
#
# Формат ввода
# Программа получает на вход десять чисел, разделенных пробелами.
# Каждое число задает тип здания на Новом проспекте: число 1 обозначает жилой дом, число 2 обозначает магазин, число 0
# обозначает офисное здание. Гарантируется, что на Новом проспекте есть хотя бы один жилой дом и хотя бы один магазин.
# Формат вывода
# Выведите одно целое число: наибольшее расстояние от дома до ближайшего к нему магазина.
# Расстояние между двумя соседними домами считается равным 1
# (то есть если два дома стоят рядом, то между ними расстояние 1,
# если между двумя домами есть еще один дом, то расстояние между ними равно 2 и т.д.)

def dist_to_shop(seq, i):
	dist = 9
	for k in range(1,9):
		if k < dist and ((i+k <= 9 and seq[i+k] == 2) or (i-k >= 0 and seq[i-k] == 2)):
			dist = k
	return dist

seq = list(map(int, input().split()))
distances = []
for i in range(len(seq)):
	if seq[i] == 1:
		distances.append(dist_to_shop(seq, i))
print(max(distances))