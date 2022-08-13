import numpy as np
import math
import random 
from random import randint
from matplotlib import pyplot as plt
import pylab as plb
import matplotlib.cm as cm
#array REP (x,y,r, num, newnum), here x,y - position 10-90, r-radius 20, num - fuzzy number, newnum - exact number

#message
box_1 = {'facecolor':'black',    #  цвет области
       'edgecolor': 'black',     #  цвет крайней линии
       'boxstyle': 'round'}    #  стиль области
       
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
n =30
#m = 101
Radiusmin=20
Radiusmax=20
MaxNum= int( math.pi * Radiusmax * Radiusmax / 4 ) # number persons in square 

items = [ [0]*5 for i in range(n)]
s_x = [ [0] for i in range(n)]
s_y = [ [0] for i in range(n)]
for i in range(n):
			items[i][0] = random.randint(10, 90)
			s_x[i]= items[i][0]
			items[i][1] = random.randint(10, 90)
			s_y[i]= items[i][1]
			items[i][2] = random.randint(Radiusmin, Radiusmax)
			items[i][3] = random.randint(1, MaxNum)
			items[i][4] = items[i][3] # newnum=num initial
			
#print(items)  
print("Initial Items")
print("i [x,y, r, num. newnum]")
for i in range(n):
    print(i,items[i])

#intersection matrix

intersect = [ [0]*n for i in range(n)]
for i in range(n):
	for j in range(i+1,n):
		dist=getLen(items[i][0],items[i][1],items[j][0],items[j][1])
		intersect[i][j] = s(items[i][2],items[j][2],dist)
		intersect[j][i]=intersect[i][j]
print("Intersection Matrix")		
for i in range(n):
    print(i,intersect[i])
print(i,'--------------------')    
#reducing fuzzy
for i in range(n):
	for j in range(i+1,n):
		InArea=intersect[i][j] * min(items[i][4],items[j][3]) / 100 
		items[i][4] =  items[i][4] - InArea / 2
	items[i][4] = int( items[i][4]) 
#		
print("Final Items")
print("i [x,y, r, num. newnum]")
for i in range(n):
    print(i,items[i])		
#
FuzzyTotal=0 
ClearTotal=0
for i in range(n):
	FuzzyTotal=FuzzyTotal+items[i][3] 
	ClearTotal=ClearTotal+items[i][4] 
#drawcircle(x,y.r.n, newnum)

plt.figure()
ax = plt.gca()
#for a, b, color, size in zip(x, y, colors, s):
    # plot circles using the RGBA colors
cmap=plb.get_cmap("jet")
for i in range(n):
	#fillcolor='green'
	#fillcolor= (items[i][3]/MaxNum, items[i][3]/MaxNum, items[i][3]/MaxNum) #colored
	fillcolor= cmap(items[i][3]/MaxNum) #grey
	circle = plt.Circle((items[i][0], items[i][1]), items[i][2], color=fillcolor,fill=True, alpha = 0.4)
	ax.add_artist(circle)
	plt.text(items[i][0], items[i][1],'#'+str(i)+': ['+str(items[i][3])+'>'+str(items[i][4])+']',bbox = box_1,color = 'white',
        fontsize = 10)
plt.text( -10,-20,'Итого(нечеткое):'+str(int(FuzzyTotal))+'> Итого(четкое):'+str(int(ClearTotal))+' ('+str( int((ClearTotal-FuzzyTotal)/FuzzyTotal * 100) )+'%)',bbox = box_1,color = 'white',  fontsize = 12)       
plt.xlim([-10, 110])
plt.ylim([-10, 110])
ax.set_aspect(1.0)  # make aspect ratio square
plt.grid()
#
 
s = plt.scatter(s_x,s_y,c = s_x, cmap='viridis')
c = plt.colorbar()
plt.show()

'''
# generate some random data
npoints = 5
x = np.random.randn(npoints)
y = np.random.randn(npoints)
print(x)
print(y)


# make the size proportional to the distance from the origin
s = [0.1*np.linalg.norm([a, b]) for a, b in zip(x, y)]
s = [a / max(s) for a in s]  # scale
print(s)
# set color based on size
c = s
colors = [cm.jet(color) for color in c]  # gets the RGBA values from a float

# create a new figure
plt.figure()
ax = plt.gca()
for a, b, color, size in zip(x, y, colors, s):
    # plot circles using the RGBA colors
    circle = plt.Circle((a, b), size, color=color, fill=False)
    ax.add_artist(circle)

# you may need to adjust the lims based on your data
minxy = 1.5*min(min(x), min(y))
maxxy = 1.5*max(max(x), max(y))
plt.xlim([minxy, maxxy])
plt.ylim([minxy, maxxy])
ax.set_aspect(1.0)  # make aspect ratio square

# plot the scatter plot
plt.scatter(x,y,s=0, c=c, cmap='jet', facecolors='none')
plt.grid()
plt.colorbar()  # this works because of the scatter
plt.show()
'''


