from exceptions import *


def checkInt(x):
    try:
        int(x)
        return True
    except ValueError:
        return False


def toFloat(x, message, ex):
    try:
        a = float(x)
        return a
    except ValueError:
        raise ex(message)


def toInt(x, message):
    try:
        a = int(x)
        return a
    except ValueError:
        raise WrongValueException(message)


def toFloatList(lst, n, message):
    temp = []
    try:
        for i in range(0, n):
            a = float(lst[i])
            temp.append(a)
        return temp
    except ValueError:
        message = message + "значение " + str(i)
        raise WrongValueException(message)
    except IndexError:
        raise WrongValueException("неверный размер списка")


def checkTimeList(lst):
    if lst[0] < 0:
        raise TimeNegativeValue(
            "Список временных точек содержит отрицательное значение. Позиция 1", 0
        )
    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            raise IsNotSortedInAsc(
                f"Список временных точек не отсортирован по возрастанию. Позиция {i + 1}",
                i,
            )
        if lst[i] < 0:
            raise TimeNegativeValue(
                f"Список временных точек содержит отрицательное значение. Позиция {i+1}",
                i,
            )


def checkConcList(lst):
    if lst[0] < 0:
        raise ConcNegativeValue(
            "В списке концентраций содержится отрицательное значение. Позиция 1", 0
        )
    for i in range(1, len(lst)):
        if lst[i - 1] == lst[i]:
            raise WrongNeighboringValues(
                f"В списке концентраций имеются одинаковые рядом стоящие значения. Позиция {i+1}",
                i,
            )
        if lst[i] < 0:
            raise ConcNegativeValue(
                f"В списке концентраций содержится отрицательное значение. Позиция {i+1}",
                i,
            )


def toFloatTableValue(v, message, row, col):
    try:
        return float(v)
    except ValueError:
        raise WrongTableValue(message, row, col)
