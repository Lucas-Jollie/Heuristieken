# import random module
import ast

def readGenomes():

    genomes = []
    # open output and input files
    f = open("100randomgenomes.txt", "r")
    counter = 0

    for row in f.readlines():
        totalInversions = 0.0

        # assigne values of genomes
        preprow = row[:-2]
        preprow = preprow[1:]
        melan = preprow.split(', ')
        melan = map(int, melan)
#        print melan
        genomes.append(melan)
    
    return genomes
    
#readGenomes()
