from Heuristieken import *

def totalScore(genome, gen):
    a = generationScore(genome, gen)
#    print "a", a
    b = geneTargets(genome)
    b = float(b)
    if b == 0:
        b += 0.01
#    print "b", b
    c = abs(geneDistance(genome))
#    print "c", c
    if c == 0:
        return a

    return float(a * (b / c))

melan = [1, 2, 3, 4, 5]
melan = [2, 1, 3, 4, 5]
melan = [5, 4,3,2,1]
melan = [3,2,1,4,5]
melan = [5,4,1,3,2]
melan = [4, 2, 5, 1, 3]
#print seriesScore(melan)
#solution = [1,2,3,4,5]

def generationScore(genome, generation):

    if len(genome) == 25:
        solution = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    elif(len(genome)) == 5:
        solution = [1,2,3,4,5]
    else:
        solution = []

    series = 0
#    print "series", series
    added = False
    serieLen = 0.0
    lengthN = len(genome)
    up = False
    down = False
    counter  = 1
    archive = []
    for i in range(lengthN - 1):
        if ((genome[i] + 1 == genome[i+1]) & (genome[i] not in archive)):
            archive.append(genome[i])
            added = True
            down = False
            up = True
        elif ((genome[i] - 1 == genome[i+1]) & (genome[i] not in archive)):
            archive.append(genome[i])
            added = True
            down = True
            up = False
        if (((genome[i] + 1 != genome[i+1]) & (genome[i] - 1 != genome[i+1])) & added == True):
            added = False
            archive.append(genome[i])
        if ((genome[i] + 1 != genome[i+1]) & (genome[i] - 1 != genome[i+1])):
            counter += 1

    serieLen = len(archive)
    if added == True:
        serieLen += 1

    if serieLen == 0:
        serieLen = 0.01
    unsorted = lengthN - serieLen
#    print "counter", counter
    series = counter
#    print "serie length", serieLen

    if (genome == solution):
        D = 0.01 * generation
    else:
        D = (1 + ((series + unsorted) / serieLen) * lengthN) * generation

    return D


ans = totalScore(melan, 1)
# print "bart", ans
