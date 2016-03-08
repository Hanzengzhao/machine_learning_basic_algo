import math
import random
import scipy as sp
import matplotlib.pyplot as plt
W=[]
X=[]
Y=[]

step=0.0001
trainnum=500
testnum=100
polynum=10
X1=[]
Y1=[]
select={}
for i in range(polynum):
	W.append(1);
for i in range(trainnum):
	X.append(random.uniform(-1,1))
	Y.append(math.sin(X[i]))
for i in range(testnum):
	X1.append(random.uniform(-1,1))
	Y1.append(math.sin(X[i]))
	

def qiupiandao(i,W,lamata,X,Y):
	suml=0
	for q in range(polynum):
		suml=suml+W[q]**2
	suml=math.sqrt(suml)
	sumh=lamata*W[i]/suml
	for j in range(trainnum):
		sum0=0
		for q in range(polynum):
			sum0=sum0+W[q]*(X[j]**q)
			if q==0:
				sum0=sum0-Y[j]
		sumh=sumh+sum0*i*W[i]*X[j]**(i-1)/trainnum		 
	return sumh

def lostfuction(lamata,W,X,Y):
	suml=0
	for i in range(polynum):
		suml=suml+W[i]**2
	
	suml=lamata*math.sqrt(suml)
	for j in range(trainnum):
		sum0=0
		for q in range(polynum):
			sum0=sum0+W[q]*(X[j]**q)
			if q==0:
				sum0=sum0-Y[j]
		suml=suml+sum0**2/(2*trainnum)
	return suml

def error(f, x, y):  
	return sp.sum((f(x)-y)**2)

for lamata in range(5): 
	while True:
		prelost=lostfuction(lamata,W,X,Y)
		for i in range(polynum):
			W[i]=W[i]-step*qiupiandao(i,W,lamata,X,Y)
		postlost=lostfuction(lamata,W,X,Y)
		print prelost-postlost
		if prelost-postlost<0.001:
			break
	f1 = sp.poly1d(W)
	fx=sp.linspace(-1,1,100)
	er=error(f1, X1, Y1)
	plt.plot(fx, f1(fx))
	#plt.legend(["lamata=%i" % lamata], loc="upper left")
	select[lamata]=[]
	select[lamata].append(er)
	select[lamata].append(list(W))
	for i in range(polynum):
		W[i]=1
	

for lamata in range(5):
	miner=0
	print lamata,select[lamata][0],select[lamata][1]
	if select[lamata][0] < select[miner][0]:
		miner=lamata



print "lamata,lost,W"
print miner,select[miner][0],select[miner][1]
plt.plot(X,Y,'.')    
plt.show()









