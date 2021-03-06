lamata=0.5
trainnum=100
X=rand(1,trainnum);
Y=sin(X);
G=zeros(10,10);
b=zeros(10,1)
Gtemp=zeros(10,10);

for i=1:10
	for j=1:10
		for l=1:100
		Gtemp(i,j)=Gtemp(i,j)+X(1,l)^(i+j-2);
		end
	end
end 

for i=1:10
	for j=1:10
		G(i,j)=Gtemp(i,j)/2*trainnum
		if i==j
		G(i,j)=G(i,j)+lamata;
		end
	end
end

for i=1:10  %一次项系数
	for l in 1:100
		b(i,1)=b(i,1)-2*Y(1,l)*X(1,l)^(i-1)
	end
end
	
		
function  [x,n]=conjgrad(A,b,x0)     
	r1=b-A*x0;     
	p=r1;     
	n=0; 
    	for i=1:rank(A)         
		if(dot(p,A*p)<1.0e-10) 
            		break;         
		end 
        	alpha=dot(r1,r1)*(dot(p,A*p))^-1;
        	x=x0+alpha*p;           
		r2=r1-alpha*A*p; 
        	if(r2<1.0e-10)                
			break;            
		end 
           	belta=dot(r2,r2)*(dot(r1,r1))^-1;
	        p=r2+belta*p;           
		n=n+1;     
	end 





