import math as m
import numpy as np

# вычисление значения функции
def calculateFunction(x):
    if 2 <= x <= 3:
        return((np.NaN, np.NaN))
    else:
        upper = m.sqrt(x*x-5*x+6)
        lower = x - 3
        result = upper*upper / lower
    return((x,result))

# вычисление всех значений функции на заданном интервале
def countPoints(start,end):
    listOfX = []
    listOfY = []
    while start <= end:
        tmp = calculateFunction(start)
        listOfX.append(tmp[0])
        listOfY.append(tmp[1])
        start += 0.1
    return((listOfX,listOfY))

# функция для проверки, что строка преобразуется в число
def checkFloat(x):
    try:
        float(x)
        return True
    except ValueError:
        return False
