import numpy as np
import math
import random 
from random import randint
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import pylab as plb
#array REP (x,y,r, num, newnum), here x,y - position 10-90, r-radius 20, num - fuzzy number, newnum - exact number
# intersection square of 2 circles r1 and r2 on distanse x
def s(r1,r2,x):
	if (r1+r2<x):
		return 0
	f1 = (r1*r1 - r2*r2 + x*x) / (2 * r1 * x)  
	f1 =  2 *  math.acos(f1) 
	f2 = (r2*r2 - r1*r1 + x*x) / (2 * r2 * x)
	f2 =  2 * math.acos( f2 ) 
	s1 = ( r1*r1 * (f1 - math.sin(f1)) ) / 2
	s2 = ( r2*r2 * (f2 - math.sin(f2)) ) / 2
	s = s1+s2
	s = int ( s / (math.pi * r1* r1) * 100 )
	return s
#
#ss = np.vectorize(s)
#
def getLen(x1,y1,x2,y2):
    diff_x = (x1-x2)**2
    diff_y = (y1-y2)**2
    length = math.sqrt(diff_x+diff_y)
    return length
#
plt.title("Зависимость ") 
plt.xlabel("R - радиус")   
plt.ylabel("Отношение четкого к нечеткому итогу (%)")   
plt.grid()       
#
n =15
m = 5
I = [0] * 120 
CT = [0] * 120
for iii in range(0,120):
	items = [[85, 48, iii, 9, 9],
	[40, 51, iii, 7, 7],
	[80, 30, iii, 5, 5],
	[87, 75, iii, 19, 19],
	[73, 82, iii, 3, 3],
	[24, 89, iii, 5, 5],
	[45, 61, iii, 8, 8],
	[40, 70, iii, 14, 14],
	[77, 19, iii, 29, 29],
	[70, 46, iii, 24, 24],
	[19, 24, iii, 21, 21],
	[27, 21, iii, 4, 4],
	[19, 48, iii, 24, 24],
	[39, 84, iii, 28, 28],
	[74, 89, iii, 22, 22],
	]
#intersection matrix
	intersect = [ [0]*n for i in range(n)]
	for i in range(n):
		for j in range(i+1,n):
			dist=getLen(items[i][0],items[i][1],items[j][0],items[j][1])
			intersect[i][j] = s(items[i][2],items[j][2],dist)
			intersect[j][i]=intersect[i][j]
#reducing fuzzy
	for i in range(n):
		for j in range(i+1,n):
			InArea=intersect[i][j] * min(items[i][4],items[j][3]) / 100 
			items[i][4] =  items[i][4] - InArea / 2
		items[i][4] = int( items[i][4]) 
#Difference Total		
	FuzzyTotal=0 
	ClearTotal=0
	for i in range(n):
		FuzzyTotal=FuzzyTotal+items[i][3] 
		ClearTotal=ClearTotal+items[i][4]
		I[iii]=iii
		CT[iii]=ClearTotal*100/FuzzyTotal
	#print(i, FuzzyTotal,ClearTotal)   	
cmap=plb.get_cmap("jet")
ax = plt.gca()
for i in range(n):
	fillcolor= cmap(items[i][3]/30) #grey
	circle = plt.Circle((items[i][0], items[i][1]), 2, color=fillcolor,fill=True, alpha = 0.4)	
	circle1 = plt.Circle((items[i][0], items[i][1]), 10, color=fillcolor,fill=True, alpha = 0.4)	
	ax.add_artist(circle)	 
	ax.add_artist(circle1)
#print(I,CT)   	 
plt.xlim([-20, 120])
plt.ylim([-20, 120])
ax.set_aspect(1.0)  # make aspect ratio square
plt.plot(I,CT)
plt.show()

