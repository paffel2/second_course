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
        s1 = self.numOfValues
        s2, s3, s4, s5, s6 = 0, 0, 0, 0, 0
        for i in range(1,self.numOfValues):
            y = (log(fabs(self.ca[i-1] - self.ca[i]))) / (log(self.t[i]-self.t[i-1]))
            x = log(self.t[i])
            s2 += x
            s3 += y
            s4 += x*x
            s5 += x*y
            s6 += y*y
        print(s1,s2, s3, s4, s5, s6)
        self._k = exp((s3*s4 - s2*s5)/(s1*s4 - s2*s2))
        self._n = (s1*s5 - s2*s3)/(s1*s4 - s2*s2)
        self._r = (s1*s5 - s2*s3)/sqrt((s1*s4 - s2*s2)*(s1*s6 - s3*s3))


class Dispertion(object):
    def __init__(self,ca, listOfT,n,k, caValues, numOfValues):
        self.ca = ca
        self.t = listOfT
        self.n = n
        self.k = k
        self.caValues = caValues
        self.numOfValues = numOfValues

    def countCbValues(self):
        ca = self.ca
        cbValues = []
        cb = 0
        for i in range(1, self.numOfValues):
            t = self.t[i] - self.t[i-1] 
            cb = cb + self.k*pow(ca,self.n)*t
            cbValues.append(cb)
            ca = ca - self.k*pow(ca,self.n)*t
            print("Значениея cb ", cb, "ca ", ca)
        return cbValues

# TO DO
    def countCcValues(self):
        ca = self.ca
        ccValues = []
        cc = 0
        for i in self.t:
            cc = cc + self.k*pow(ca,self.n)
            ccValues.append(cc)
            ca = ca - self.k*2*pow(ca,self.n)
        return ccValues
    
    def countDispertion(self):
        ca = self.ca
        d = 0
        d += pow(ca - self.ca,2)
        for i in range(0, self.numOfValues):
            ca = ca - self.k*2*pow(ca,self.n)
            d += pow(ca - self.ca,2)
        return d

    