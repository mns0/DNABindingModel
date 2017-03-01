import numpy as np
from multiprocessing import pool
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as mpatches
import math
import operator
import random

##globaly define path ##
t = np.arange(-0.3*np.pi,3.9*np.pi,np.pi/30)
x1 = 30*np.exp(0.14*t)*np.cos(t) - 9
y1 = 30*np.exp(0.14*t)*np.sin(t) + 15
x2 = 18*np.exp(0.15*t)*np.cos(t) - 7
y2 = 18*np.exp(0.15*t)*np.sin(t) + 12
xx = np.hstack((x2,x1[::-1]))
yy = np.hstack((y2,y1[::-1]))
z1 = zip(xx,yy)
codes = np.ones(len(xx))*Path.LINETO
codes[0] = Path.MOVETO
codes[-1] = Path.STOP
structPath = Path(z1,codes)
##########################


#initialization statement
def initStatement(trials,geo,windowTime):
    print('#####################')
    print('# Running simulation#')
    print('# trials: ' + str() +'      #')
    print('# geometry: ' + str() + '    #')
    print('# Window Time: ' + str() + '    #')
    print('#####################')

#run the simulations
def runSimulations(trials,geo,windowTime,prob):
    stats = []
    for trial in np.arange(trials):
        stats.append(runSim(geo,windowTime,prob))
    return stats

#run single simulation
def runSim(geo,windowTime,prob):
    coor = getXY()
    return calcExpectationTimeM1(coor,geo,windowTime,prob);


#get initial location of nucleotide
def getXY():
     return [np.random.uniform(low=-150,high=150),
             np.random.uniform(low=-150,high=150)]


def inGeo(coor,geo):
    global structPath
    return structPath.contains_points([coor])


#calculate exectation time for trial
def calcExpectationTimeM1(coor,geo,windowTime,prob):
    pen = 0
    entDist = distanceFromEnt(coor,geo)
    geoFac = getGeometricFactor(coor,geo,entDist)
    if inGeo(coor,geo):
        dist = 0
    else:
        #idx, dist = distanceFromEnt2(coor,geo)
        pen = windowTime
        #print(idx,dist)
    skipP = skipCalculation(geoFac,coor,entDist,windowTime,prob)
    expTime =  geoFac*windowTime+pen+skipP
    return expTime

#random guessing of time
def calcExpectationTimeM2(windowTime):
    #probability of landing in spiral
    extArea = 1.0 - 20470.0/33676
    AddTime = 0
    skipTime = 0
    if (random.random() < extArea):
        AddTime = 500
    if (random.randint(1,10) == 1 ):
        skipTime = 500
    geoFactor = random.randint(1,10)
    #print( geoFactor*windowTime + AddTime, math.exp(-16)  )
    return geoFactor*windowTime + AddTime

#distance from channel
#assume pushed -x
def distanceFromEnt(coor,geo):
    global x1, y1
    points = zip(x1,y1)
    distArr = []
    for x,y in points:
        distArr.append(math.sqrt((x-coor[0])**2 + (y-coor[1])**2))
    min_index, min_value = min(enumerate(distArr), key=operator.itemgetter(1))
    #print(min_index,min_value)
    return ( min_index,min_value)

def distanceFromEnt2(coor,geo):
    global x1, y1
    minDist = 0
    vals =   (y1 <= coor[1]+5) & (y1 >= coor[1]-5)
    idx = np.ravel(np.where(vals))
    print(len(idx),idx)
    if len(idx) > 1:
        idx, minDist = getSmallestIndex(coor,idx)
    return (idx, minDist)

#calculate minimum distance such that
def getSmallestIndex(coor,idx):
    global x1, y1
    minArray = 0
    minDist = 9999
    for i in idx:
        if coor[0] > x1[i]:
            dist = coor[0] - x1[i]
        else:
            dist = coor[0] + 150 + (150 - x1[i])
        if dist < minDist:
            minDist = dist
            minArray = i
    return (minArray, minDist)


def getGeometricFactor(coor,geo,entDist):
    global x1, y1, t
    x = t[entDist[0]]/(np.pi/2)  + 1
    return x

#analyze the data
def analyzeData(data):
    return

def initSim(trials,geo,windowTime):
    initStatement(trials,geo,windowTime)

#determines the penelty of skipping for the trial
def skipCalculation(geoFac,coor,entDist,windowTime,prob):
    skipTime =0
    for i in range(int(geoFac)):
        m = 95.0/100.0
        r = random.random()
        if  m < random.random():
            skipTime = 3*windowTime*random.randint(1,10)
    return skipTime
