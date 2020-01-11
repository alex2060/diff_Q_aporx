
#https://www.youtube.com/watch?v=cXHvC_FGx24
import math
import random
from scipy.optimize import minimize
import time
import matplotlib.pyplot as plt
def F_input(array,driv,value):
	amout=0
	if driv==0:
		amout+=array[0]
	counter=1

	for x in range(len(array)//2):

		amout+= ( array[2*x+1]*math.sin( value/counter   +  math.pi*driv/2 )  +   array[2*x+2]*math.cos( (value)/counter + math.pi*driv/2 ) )/( counter**driv )
		counter=counter+1

	return amout


def gama_differnace(value,function):
	return F_input(function,0,value)-F_input(function,2,value)**2+value



def points(number,end):
	out=[0]*number
	for x in range(number):
		out[x]=x*end/number
	return out


def make_randome_imputs(number):
	out=[0]*number
	for x in range(number):
		out[x]=3*(random.random()-0.5)
	return out


def solve(iterations,inital_conditions,order_funciton,multiplyer,number_of_aproxmations_,number_of_points,end):
	def test_function(x0):
		sums=0
		mypoints=points(number_of_points,end)
		for x in range( len(mypoints) ):
			sums+=( gama_differnace(mypoints[x],x0)**2 )**1/2
		sums/number_of_points
		add=0
		for x in range(len(inital_conditions)):
			add+=( order_funciton(x0,x,0)-inital_conditions[x] )**2
		return (sums+add*multiplyer)

	b=(-10000,10000)
	bnd=[0]*(2*number_of_aproxmations_+1)
	for come_on in range(2*number_of_aproxmations_+1):
		bnd[come_on]=b


	minsol=100000

	x0=make_randome_imputs(2*number_of_aproxmations_+1)
	minsol=test_function(x0)
	outsol=minimize(test_function,x0,method='SLSQP',bounds=bnd)
	for x in range(iterations):
		x0=make_randome_imputs(2*number_of_aproxmations_+1)
		sol=minimize(test_function,x0,method='SLSQP',bounds=bnd)
		print(sol.fun,minsol)
		if sol.fun<=minsol:
			minsol=sol.fun
			outsol=sol
	return outsol


array=[1,1,2,-1,3]



print(F_input(array,0,2))
print(F_input(array,1,2))
print(F_input(array,2,2))
print(points(10,20))

ret=solve(10,[1,2],order_funciton=F_input,multiplyer=3,number_of_aproxmations_=5,number_of_points=100,end=1)
print(ret)
test=ret.x


print(F_input(test,1,0))
xplot=[0]*100
yplot=[0]*100
my_points=points(100,1)
for x in range(100):
	xplot[x]=gama_differnace(my_points[x],test)
	yplot[x]=my_points[x]
print(xplot)
plt.plot(yplot,xplot)
plt.show()




x_val=1
x_prime=2
time=0

xplot_1=[0]*2000
yplot_1=[0]*2000
xplot_2=[0]*2000
yplot_2=[0]*2000
for x in range(2000):
	x_val=x_val+x_prime*0.001
	x_prime=x_prime+(x_val+time)**1/2*0.001
	xplot_1[x]=F_input(test,0,time)
	yplot_1[x]=time
	xplot_2[x]=x_val
	yplot_2[x]=time
	time=time+0.001

#print(yplot_1)
plt.plot(yplot_1,xplot_1)
plt.plot(yplot_2,xplot_2)


plt.show()



# ganesh 
