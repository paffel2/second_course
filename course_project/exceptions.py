class TableValueException(Exception):
    def __init__(self, row, col):
        self.row = row
        self.col = col

class AllValuesNotUniq(Exception):
    def __init__(self, message):
        self.message = message

class IsNotSortedInAsc(Exception):
    def __init__(self, message,position):
        self.message = message
        self.position = position

class WrongNeighboringValues(Exception):
    def __init__(self, message, position):
        self.message = message
        self.position = position

# проверка значений таблицы
class NegativeValue(Exception):
    def __init__(self, message,position):
        self.message = message
        self.position = position

class TimeNegativeValue(NegativeValue):
    pass

class ConcNegativeValue(NegativeValue):
    pass

# проверка обычных значений
class WrongValueException(Exception):
    def __init__(self, message):
        self.message = message

class WrongCbValue(WrongValueException):
    pass

class WrongCaValue(WrongValueException):
    pass

class WrongCcValue(WrongValueException):
    pass

class WrongNumOfRows(WrongValueException):
    pass

class WrongTableValue(WrongValueException):
    def __init__(self, message,row,col):
        super().__init__(message)
        self.row = row
        self.col = col