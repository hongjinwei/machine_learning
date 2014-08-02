from numpy import *
import operator

def create_dataset():
    group = array([[1.0,1.1],[1.0,1.0],[0, 0],[0,0.1]])
    labels = ['A','A','B','B']
    return group,labels

#example
#inX = [2.3,34,23]
#dataset = array([[1,2,3],[2,3,4],[4,5,6]])
#lables = ["atype","btype","atype"]
def classify(inX,dataSet,labels,k):
    dataSetSize = dataSet.shape[0]
    
    #calculate the distance
    diffMat = tile(inX,(dataSetSize,1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistance = sqDiffMat.sum(axis=1)
    distances = sqDistance ** 0.5
    #print distances
    sortedDistIndicies = distances.argsort() #return an array of indexing value ascendingly
    #print sortedDistIndicies
    classCount = {}
    
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1 #get value ,first arg is the key and the second is default
    #print classCount 
    sortedClassCount = sorted(classCount.iteritems(),
                              key = operator.itemgetter(1), #sorted with key,this is a  function
                              reverse = True) #now the first one is the max number
    
    #print sortedClassCount
    return sortedClassCount[0][0]

def file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)
    returnMat = zeros((numberOfLines, 3)) #return a new m*n zero matrix
    classLabelVector = []
    index = 0
    for line in arrayOLines:
        line = line.strip() #strip enter character
        listFormLine = line.split('\t')
        returnMat[index,:] = listFormLine[0:3] #give the value of 0-2 to the index line
        classLabelVector.append(int(listFormLine[-1])) #get the last element
        index += 1

    return returnMat,classLabelVector
    
