from math import *
from numpy import *
from exceptions import WrongCaValue


class KineticConst(object):
    def __init__(self, cb, cc, listOfC, listOfT, numOfValues):
        self.ca = listOfC
        self.t = listOfT
        self.cb = cb
        self.cc = cc
        self.n = 0
        self.r = 0
        self.k = 0
        self.numOfValues = numOfValues

    def countKineticParameters(self):
        s1 = self.numOfValues - 1
        s2, s3, s4, s5, s6 = 0, 0, 0, 0, 0
        for i in range(s1):
            y = log(fabs(self.ca[i + 1] - self.ca[i]) / (self.t[i + 1] - self.t[i]))
            x = log(self.ca[i])
            s2 += x
            s3 += y
            s4 += x * x
            s5 += x * y
            s6 += y * y
        self.k = exp((s3 * s4 - s2 * s5) / (s1 * s4 - s2 * s2))
        self.n = (s1 * s5 - s2 * s3) / (s1 * s4 - s2 * s2)
        self.r = (s1 * s5 - s2 * s3) / sqrt((s1 * s4 - s2 * s2) * (s1 * s6 - s3 * s3))


class Dispertion(object):
    def __init__(self, ca, listOfT, n, k, caValuesExp, numOfValues, cb, cc):
        self.ca = ca
        self.cb = cb
        self.cc = cc
        self.t = listOfT
        self.n = n
        self.k = k
        self.caValuesExp = caValuesExp
        self.caValuesCounted = [ca]
        self.ccValues = [cc]
        self.cbValues = [cb]
        self.numOfValues = numOfValues

    def countCValues(self):
        ca = self.ca
        cb = self.cb
        cc = self.cc
        for i in range(self.numOfValues - 1):
            if ca < 0:
                raise WrongCaValue("Модель невозможно описать линейной регрессией")
            else:
                t = self.t[i + 1] - self.t[i]
                cb = cb + self.k * (pow(ca, self.n)) * t
                cc = cc + self.k * (pow(ca, self.n)) * t * 2
                self.cbValues.append(cb)
                self.ccValues.append(cc)
                ca = ca - self.k * (pow(ca, self.n)) * t
                self.caValuesCounted.append(ca)

    def countDispertion(self):
        d = 0
        for i in range(0, self.numOfValues):
            d += pow(self.caValuesExp[i] - self.caValuesCounted[i], 2)
        return d
