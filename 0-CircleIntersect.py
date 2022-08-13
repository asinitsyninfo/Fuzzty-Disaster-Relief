import matplotlib.pyplot as plt
import numpy as np
import math
import random
def s(r1,r2,x):
	f1 = (r1*r1 - r2*r2 + x*x) / (2 * r1 * x)  
	f1 =  2 *  math.acos(f1) 
	f2 = (r2*r2 - r1*r1 + x*x) / (2 * r2 * x)
	f2 =  2 * math.acos( f2 ) 
	s1 = ( r1*r1 * (f1 - math.sin(f1)) ) / 2
	s2 = ( r2*r2 * (f2 - math.sin(f2)) ) / 2
	s = s1+s2
	s = s / (math.pi * r1* r1) * 100
	return s
#print (s(20,20,10) )	
ss = np.vectorize(s)
R1=20
R2=20
x = np.arange(0.001,100,1)
xx=x*(R1+R2)/100
plt.title("Область пересечения окружностей C_j1 & C_j2") 
plt.xlabel("Дистанция (%) [0, R_j1+R_J2]")   
plt.ylabel("Пересечение(%)")   
plt.grid()       
plt.plot(x,ss(R1,R2,xx))
plt.plot(x,100-100/(R1+R2)*xx)
plt.show()
