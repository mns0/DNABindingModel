import numpy as np
from multiprocessing import pool

#initialization statement
def initStatement(trials,geo,windowTime):
    print('#####################')
    print('# Running simulation#')
    print('# trials: ' + str() +'      #')
    print('# geometry: ' + str() + '    #')
    print('# Window Time: ' + str() + '    #')
    print('#####################')

#run the simulations
def runSimulations(trials,geo,windowTime):
    stats = []
    for trial in np.arange(trials):
        runSim(geo,windowTime)
    return stats

#run single simulation
def runSim(geo,windowTime):
    coor = getXY()
    calcExpectationTime(coor,geo,windowTime);
    return

#get initial location of nucleotide
def getXY():
     return [np.random.uniform(low=-150,high=150),
             np.random.uniform(low=-150,high=150)]


def inGeo(coor,geo):
    return


#calculate exectation time for trial
def calcExpectationTime(coor,geo,windowTime):
    if inGeo(coor,geo):
        dist = 0
    else:
        dist = distanceFromEnt(coor,geo)
    geoFac = getGeometricFactor(coor,geo)
    expTime = geoFac*windowTime
    return

#distance from channel enterance
#assume pushed -y
def distanceFromEnt(coor,geo):
    x, y = coor
    return

def getGeometricFactor(coor,geo):
    return

#analyze the data
def analyzeData(data):
    return


def initSim(trials,geo,windowTime):
    initStatement(trials,geo,windowTime)
