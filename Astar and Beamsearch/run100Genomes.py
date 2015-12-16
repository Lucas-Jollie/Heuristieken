from writeLines import *
from readLines import readGenomes
from generationAMix100 import *

start = []
solution = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
totalSolutions = []
average = 0

results = open("100sorted.txt", 'w')

genes = readGenomes()

for i in range(len(genes)):
    for j in range(len(genes[i])):
        start.append(genes[i][j])

    writeStart(results, i, start)
    inversions = runSimulation(start, solution)
    totalSolutions.append(inversions)
    writeSolution(results, inversions)

    # clear start at end run
    start[:] = []
for i in range(len(totalSolutions)):
    average += totalSolutions[i]
average = average / len(totalSolutions)
results.write("\n")
results.write("Average inversions: ")
results.write(str(average))
results.write("\n")
#runSimulation(start, solution)
