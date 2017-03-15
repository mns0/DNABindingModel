#main file with io handeling
import helper as hp
import geometry as geo
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as mpatches


#model of nucleotde translocation into a graphene nanopore with various geometry pores
def main():
    runSim = False
    geo.drawSpiral(hp.getXY())
    skipProb = 22
    trials = 100
    vel = 1 #  nm/ns
    geom='spiral'
    windowTime = 500 #50 ps
    if runSim:
        hp.initSim(trials,geom,windowTime,vel)
        data = hp.runSimulations(trials,geom,windowTime,skipProb,vel)
        plt.hist(data,250)
        plt.show()
        #hp.analyzeData(data)

main()
