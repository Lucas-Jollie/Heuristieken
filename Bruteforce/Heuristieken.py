# Groupname: Aardbeizonder
# Names: Lucas Jollie, Bart Quaink, Anneke ter Schure
#
# File: Heuristieken.py
#
# provides helperfunctions to calculate "fitness" scores for genomes
# bigger scores are better in these cases
# ------------------------------------------------------------------------------


def seriesScore(genome):
    """
    returns the number of genes that are in a series
    divided by the number of series
    e.g. [1,2,3,5,4] returns 5 divided by 2
    """
    totalLen = 0
    newseriesup = False
    newseriesdown = False
    series = 0
    serieLen = 0

    for i in range(len(genome) - 1):
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
            else:
                series += 1

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

    if (series == 0 or totalLen == 0):
        return 0
    elif (serieLen == len(genome)):
        return serieLen, series

    totalLen += series # each serie is at least 2 big so need to add 1 for each series
    return totalLen, series

def geneDistance(genome):
    """
    returns the negative sum of the distance between the current place of a gene
    and it's target location
    """
    distanceSum = 0
    for i in range(len(genome)):
        # if (genome[i] < i + 1):
        distance = abs(genome[i] - (i + 1))
        distanceSum += distance
    return -distanceSum

def geneTargets(genome):
    """
    returns the number of genes that are already at their target location
    maybe make this relative instead of absolute so an inverted genome gets a
    low score
    """
    numberCorrect = 0
    for i in range(len(genome)):
        if (genome[i] == i + 1):
            numberCorrect += 1
    return numberCorrect


test1 = [1,2,3,5,4]
test2 = [1,3,5,2,4]
test3 = [5,4,3,2,1]

print "seriesScore 1: ", seriesScore(test1) # should return 5 / 2
print "seriesScore 2: ", seriesScore(test2) # should give no series and no length
print "seriesScore 3: ", seriesScore(test3) # should give 5 / 1

print "getTargets 1: ", geneTargets(test1) # should return 3
print "getTargets 2: ", geneTargets(test2) # should return 1
print "getTargets 3: ", geneTargets(test3) # should return 1

print "geneDistance 1: ", geneDistance(test1) # should return -2
print "geneDistance 2: ", geneDistance(test2) # should return -6
print "geneDistance 3: ", geneDistance(test3) # should return -12
