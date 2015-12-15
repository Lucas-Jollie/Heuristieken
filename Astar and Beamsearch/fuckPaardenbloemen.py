def seriesScore(genome):
    """
    Lucas self notes:
    D = 1 + (T + U) / St
    met D is priority
    T = totaal aantal elementen (series)
    U = # unsorted numbers
    St = totale lengte sequenties serieLen
    """
    lengthN = len(genome)
    totalLen = 0.0
    newseriesup = False
    newseriesdown = False
    series = 0.0
    serieLen = 0.0




#    unsorted = lengthN - serieLen
#    print serieLen
#    print series
#    print "totalLen", totalLen

    return series

#    D = 1 + ((series + unsorted) / serieLen) * lengthN
#    return D

melan = [1, 2, 3, 4, 5]
#melan = [2, 1, 3, 4, 5]
#melan = [5, 4,3,2,1]
#melan = [3,2,1,4,5]
#melan = [5,4,1,3,2]
#melan = [4, 2, 5, 1, 3]
#print seriesScore(melan)
#solution = [1,2,3,4,5]

def bart(genome):

    if len(genome) == 25:
        solution = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
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
        serieLen = 0.001
    unsorted = lengthN - serieLen
#    print "counter", counter
    series = counter
#    print "serie length", serieLen

    if (genome == solution):
        D = 0.1
    else:
        D = 1 + ((series + unsorted) / serieLen) * lengthN
    
    return D


ans = bart(melan)
#print "bart", ans
