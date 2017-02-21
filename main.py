#main file with io handeling
import helper as hp
import numpy as np
import matplotlib.pyplot as plt

def inSpiral(coor):
    xp,yp = coor
    t = np.arange(-0.3*np.pi,3.9*np.pi,np.pi/20)
    x1 = 30*np.exp(0.14*t)*np.cos(t) - 9
    y1 = 30*np.exp(0.14*t)*np.sin(t) + 15
    x2 = 18*np.exp(0.15*t)*np.cos(t) - 7
    y2 = 18*np.exp(0.15*t)*np.sin(t) + 12
    return False

#define geometry
def drawSpiral(coor):
    x,y = coor
    t = np.arange(-0.3*np.pi,3.9*np.pi,np.pi/20)
    x1 = 30*np.exp(0.14*t)*np.cos(t) - 9
    y1 = 30*np.exp(0.14*t)*np.sin(t) + 15
    x2 = 18*np.exp(0.15*t)*np.cos(t) - 7
    y2 = 18*np.exp(0.15*t)*np.sin(t) + 12
    if inSpiral(coor):
        txt = "in geo"
    else:
        txt = "not in geo"
    plt.plot(x1,y1,x2,y2)
    plt.scatter(x,y,s=100)
    plt.text(100, 100,txt, color='green', fontsize=15)
    plt.show()


#model of nucleotde translocation into a graphene nanopore with various geometry pores
def main():
    runSim = False
    drawSpiral(hp.getXY())
    trials = 100
    geo='spiral'
    windowTime = 50 #50 ps
    if runSim:
        hp.initSim(trials,geo,windowTime)
        data = hp.runSimulations(trials,geo,windowTime)
        hp.analyzeData(data)

main()
