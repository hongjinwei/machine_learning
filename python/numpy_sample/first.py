from numpy import *

#build 4x4 rand matrix
print random.rand(4,4)
print '============'
randMat = mat(random.rand(4,4))

#randMat.I randMat
print 'randMat:'
print randMat
print 'randMat.I:'
print randMat.I
#randMat.I solve the inverse of a matrix 
myEye = randMat*randMat.I
print myEye
#eye function create an identity matrix of n
print eye(4,4)
