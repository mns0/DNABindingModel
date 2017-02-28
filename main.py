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
    trials = 5000
    geom='spiral'
    windowTime = 50 #50 ps
    if runSim:
        hp.initSim(trials,geom,windowTime)
        data = hp.runSimulations(trials,geom,windowTime)
        #plt.hist(data)
        #plt.show()
        #hp.analyzeData(data)

main()
