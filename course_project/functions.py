from exceptions import *

def checkInt(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

def toFloat(x,message,ex):
    try:
        a = float(x)
        return(a)
    except ValueError:
        raise ex(message)

def toInt(x,message):
    try:
        a = int(x)
        return(a)
    except ValueError:
        raise WrongValueException(message)
    
def toFloatList(lst,n,message):
    temp = []
    try:
        for i in range(0,n):
            a = float(lst[i])
            temp.append(a)
        return temp
    except ValueError:
        message = message + "значение " + str(i)
        raise WrongValueException(message)
    except IndexError:
        raise WrongValueException("неверный размер списка")


'''def isUniq(lst,listName):
    uniqList = list(set(lst))
    if not len(lst) == len(uniqList):
        raise AllValuesNotUniq("Присутствуют неуникальные значения в списке " + listName)



def isAsc(lst,listName):
        tempValue = lst[0]
        
        for i in range(1,len(lst)):
            if tempValue <= lst[i]:
                tempValue = lst[i]
            else:
                raise IsNotSortedInAsc("Список " + listName + " не отсортирован по возрастанию")

def isHaveNegative(lst,listName):
    for i in lst:
        if i < 0:
           raise NegativeValue("Список " + listName + " имеет отрицательные значения")

def test():
    testList = [1,2,5,5]
    isHaveNegative(testList,"тестовый")

test()'''

def checkTimeList(lst): 
    tempValue = lst[0]
    if tempValue < 0:
        raise TimeNegativeValue("Список временных точек содержит отрицательное значение. Позиция 1", 0)
    for i in range(1,len(lst)):
            if tempValue < lst[i]:
                tempValue = lst[i]
            else:
                raise IsNotSortedInAsc("Список временных точек не отсортирован по возрастанию. Позиция " + str(i+1), i)
            if lst[i] < 0:
                raise TimeNegativeValue("Список временных точек содержит отрицательное значение. Позиция " + str(i+1), i)

def checkConcList(lst):
    tempValue = lst[0]
    if tempValue < 0:
        raise ConcNegativeValue("В списке концентраций содержится отрицательное значение. Позиция 1", 0)
    for i in range(1,len(lst)):
        if tempValue != lst[i]:
            tempValue = lst[i]
        else:
            raise WrongNeighboringValues("В списке концентраций имеются одинаковые рядом стоящие значения. Позиция " + str(i+1), i)
        if lst[i] < 0:
            raise ConcNegativeValue("В списке концентраций содержится отрицательное значение. Позиция " + str(i+1), i)
            

def toFloatTableValue(v,message,row,col):
    try:
        return float(v)
    except ValueError:
        raise WrongTableValue(message,row,col)
