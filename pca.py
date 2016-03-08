from numpy import *  
#coding: utf-8      
def pca(dataMat, topNfeat=5):  
        meanVals = mean(dataMat, axis=0)  
        meanRemoved = dataMat - meanVals #减去均值  
        stded = meanRemoved / std(dataMat) #用标准差归一化  
        covMat = cov(stded, rowvar=0) #求协方差方阵  
        eigVals, eigVects = linalg.eig(mat(covMat)) #求特征值和特征向量
	#print eigVals
	#print eigVects  
        eigValInd = argsort(eigVals)  #对特征值进行排序
	#print eigValInd  
        eigValIndre = eigValInd[-(topNfeat ):]
	#eigValInd=eigValIndre.reverse()
	#print  eigValInd    
        redEigVects = eigVects[:, eigValIndre]       # 除去不需要的特征向量
	#print  redEigVects 
        lowDDataMat = stded * redEigVects    #求新的数据矩阵  
        reconMat = (lowDDataMat * redEigVects.T) * std(dataMat) + meanVals  
        return lowDDataMat, reconMat  

randArray = random.random(size=(10,8))
print randArray
a,b=pca(randArray)
print a,b


