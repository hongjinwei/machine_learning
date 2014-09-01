from numpy import *

def standRegres(xArr, yArr):
    xMat = mat(xArr)
    yMat = mat(yArr).T
    xTx = xMat.T * xMat
    if linalg.det(xTx) == 0.0:
        print "Non-singular Matrix , can not inverse!"
        return 

    theta = xTx.I * (xMat.T * yMat) 
    return theta
