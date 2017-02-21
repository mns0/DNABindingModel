#main file with io handeling
import helper as hp
import numpy as np
import matplotlib.pyplot as plt





class geometry:
	"""  geometry type

	"""
	def __init__(self, geo ):
		geo = geometry.geo




#define geometry
def drawSpiral():
	t = np.arange(-0.3*np.pi,3.9*np.pi,np.pi/20)
	x1 = 30*np.exp(0.14*t)*np.cos(t) - 9
	y1 = 30*np.exp(0.14*t)*np.sin(t) + 15
	x2 = 18*np.exp(0.15*t)*np.cos(t) - 7
	y2 = 18*np.exp(0.15*t)*np.sin(t) + 12
	#plt.plot(x1,y1,x2,y2)
	#plt.show()





#model of nucleotde translocation into a graphene nanopore with various geometry pores
def main():
	drawSpiral()
	exit()
	trials = 100
	geo='spiral'
	windowTime = 50 #50 ps
	hp.initSim(trials,geo,windowTime)
	data = hp.runSimulations(trials,geo,windowTime)
	hp.analyzeData(data)

main()
