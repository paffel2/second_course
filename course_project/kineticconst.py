from math import *
from numpy import *

class KineticConst(object):
    def __init__(self,cb,cc,listOfC, listOfT, numOfValues):
        self.ca = listOfC
        self.t = listOfT
        self.cb = cb
        self.cc = cc
        self._n = 0
        self._r = 0
        self._k = 0
        self.numOfValues = numOfValues

    def getK(self):
        return self._k
    
    def getN(self):
        return self._n
    
    def getR(self):
        return self._r
    
    def countKineticParameters(self):
        s1 = self.numOfValues - 1
        s2, s3, s4, s5, s6 = 0, 0, 0, 0, 0
        for i in range(s1):
            y = log(fabs(self.ca[i+1] - self.ca[i]) / (self.t[i+1]-self.t[i]))
            x = log(self.ca[i])
            s2 += x
            s3 += y
            s4 += x*x
            s5 += x*y
            s6 += y*y
        print(s1,s2,s3,s4,s5,s6)
        self._k = exp((s3*s4 - s2*s5)/(s1*s4 - s2*s2))
        self._n = (s1*s5 - s2*s3)/(s1*s4 - s2*s2)
        self._r = (s1*s5 - s2*s3)/sqrt((s1*s4 - s2*s2)*(s1*s6 - s3*s3))


class Dispertion(object):
    def __init__(self,ca, listOfT,n,k,caValuesExp, numOfValues,cb,cc):
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
        for i in range(self.numOfValues-1):
            t = self.t[i+1] - self.t[i] 
            cb = cb + self.k * (pow(ca,self.n)) * t
            cc = cc + self.k * (pow(ca,self.n)) * t * 2
            self.cbValues.append(cb)
            self.ccValues.append(cc)
            ca = ca - self.k *  (pow(ca,self.n)) * t
            self.caValuesCounted.append(ca)
            #print(f'Значениея cb = {cb}, ca = {ca}, cc = {cc}')
    
    def countDispertion(self):
        d = 0
        for i in range(0, self.numOfValues):
            d += pow(self.caValuesExp[i] - self.caValuesCounted[i],2)
        return d

    