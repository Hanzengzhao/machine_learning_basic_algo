from numpy import *  
#coding: utf-8      
def pca(dataMat, K=5):  
        meanVals = mean_value(dataMat) 
  
        meanRemoved = dataMat - meanVals 
        stded = meanRemoved / std(dataMat,axis=0)  
        covMat = cov(stded, axis=0) 
        eigVals, eigVects = linalg.eig(mat(covMat)) 
        eigValInd = argsort(eigVals)   
        eigValInd = eigValInd[-K:]    
        seleEigVects = eigVects[:, eigValInd]       
        lowDDataMat = stded * seleEigVects    
        return lowDDataMat
def mean_value(MAT):
        mean_va=random.random(size=(1,8))
	for j in range(MAT.shape[1]):
		sum0=0
		for i in range(MAT.shape[0]):
			sum0=sum0+MAT[i][j]
		mean_va[0,j]=sum0
	return mean_va
	
randArray = random.random(size=(10,8))
a=pca(randArray)
print a


