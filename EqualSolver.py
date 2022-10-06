import math
def GetDis(a, b ,c):
	D = (b * b) - (4 * a * c)
	if D < 0:
		return "Нет корней"
	if D == 0:
		result1 = (-b) / (2*a)
		return "Дискриминант равен: " + str(D) + "\nЕдинственный корень равен" + str(result1) 
	first_x = (-b - math.sqrt(D)) / (2*a)
	second_x = (-b + math.sqrt(D)) / (2*a)
	result = "Первый корень равен: " + str(first_x) + "\nВторой корень равен: " + str(second_x)
	#result2 = str((-b)) + " +- " + "√" + str(D) + " \n-------------\n " + str(2 * a)
	fin_res = "Дискриминант равен: " + str(D) + "\n" +result
	return fin_res