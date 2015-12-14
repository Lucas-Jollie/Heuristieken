def seriesScore(genome):
    """
    returns the number of genes that are in a series
    divided by the number of series
    e.g. [1,2,3,5,4] returns 5 divided by 2
    """
    
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
    

    for i in range(lengthN - 1):

        # there is no current series
        if (newseriesup == False and newseriesdown == False):
            if (genome[i + 1] == genome[i] + 1):
                series += 1
                newseriesup = True
                serieLen = 2
            elif (genome[i + 1] == genome[i] - 1):
                series += 1
                newseriesdown = True
                serieLen = 2

        # the current series is going up
        elif (newseriesup == True):
            if (genome[i + 1] == genome[i] + 1):
                serieLen += 1
            else:
                totalLen += serieLen
                serieLen = 0
                newseriesup = False

        # the current serie is going down
        elif (newseriesdown == True):
            if (genome[i + 1] == genome[i] - 1):
                serieLen += 1
            else:
                totalLen += serieLen
                serieLen = 0
                newseriesdown = False

        
    totalLen += series # each serie is at least 2 big so need to add 1 for each series
    

    unsorted = lengthN - serieLen
    print serieLen
    print series
    print totalLen
    
#    D = 1 + ((series + unsorted) / serieLen) * lengthN
#    return D
    
melan = [1, 2, 3, 4, 5]
#melan = [2, 1, 3, 4, 5]
#melan = [5, 4,3,2,1]
#melan = [3,2,1,4,5]
melan = [5,4,1,3,2]
#melan = [4, 2, 5, 1, 3]
#print seriesScore(melan)


def bart(genome):
    added = False
    serieLen = 0.0
    lengthN = len(genome)
    archive = []
    for i in range(lengthN - 1):
        if ((genome[i] + 1 == genome[i+1]) & (genome[i] not in archive)):
            archive.append(genome[i])
            added = True
        elif ((genome[i] - 1 == genome[i+1]) & (genome[i] not in archive)):
            archive.append(genome[i])
            added = True
        if (((genome[i] + 1 != genome[i+1]) & (genome[i] - 1 != genome[i+1])) & added == True):
            added = False
            archive.append(genome[i])
            
    serieLen = len(archive)
    if added == True:
        serieLen += 1
    print len(archive)
    print archive
    print "serie length", serieLen

############    for i in range(lengthN - 1):
############        if (genome[i] - 1 == genome[i+1]):
#############            if added == False:
#############                serieLen += 1
############            serieLen += 1
############            i += 1
############            added = True
############        elif (genome[i] - 1 != genome[i+1]) & (added == True):
############            serieLen += 1
############            
#############    if added == True:
#############        serieLen += 1

print bart(melan)

