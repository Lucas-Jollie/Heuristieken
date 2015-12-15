from writeLines import *
from readLines import readGenomes
from generationAMix100 import *

start = []
solution = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

results = open("100sorted.txt", 'w')

genes = readGenomes()

for i in range(2):
#for i in range(len(genes)):
    for j in range(len(genes[i])): 
        start.append(genes[i][j])
    
    writeStart(results, i, start)
    inversions = runSimulation(start, solution)
    writeSolution(results, inversions)
    
    # clear start at end run
    start[:] = []
#runSimulation(start, solution)
