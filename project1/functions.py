import math as m
import numpy as np

# вычисление значения функции
def calculateFunction(x):
    if 2 < x <= 3:
        return((np.NaN, np.NaN))
    else:
        y = x - 2
    return((x,y))

# вычисление всех значений функции на заданном интервале
def countPoints(start,end,step=0.1):
    listOfX = []
    listOfY = []
    while start <= end:
        tmp = calculateFunction(start)
        listOfX.append(tmp[0])
        listOfY.append(tmp[1])
        start += step
    return((listOfX,listOfY))

# функция для проверки, что строка преобразуется в число
def checkFloat(x):
    try:
        float(x)
        return True
    except ValueError:
        return False
