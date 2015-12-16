# Groupname: Aardbeizonder
# Names: Lucas Jollie, Bart Quaink, Anneke ter Schure
#
# A mix of beam and astar; uses a priority queue! and doesn't stop when solution found!
# only prints best solution!
# loops through the generations instead of just the priority queue
# -------------------------------------------------------------------------------

# imports
import time
import copy
import heapq
from pythontrie import Trie
from scoreDefs import generationScore
from heapq import *

# initialise
queue = []
archive = Trie()

#TODO adjust: ########################
beam = 100
maxQueue = 50
maxGenerations = 15
######################################

start_time = time.time()

class Node:
    """
    creates nodes for the graph needed for this type of search
    """
    def __init__(self, cargo=None, parent=None, score=None):
        self.cargo = cargo
        self.prev = parent
        # self.score = score

    def __str__(self):
        return str(self.cargo)

def generateAllChildren(parent):
    """
    Generates all children of parent
    Based on inversions of size 3
    """
    children = []
    length = len(parent)

    for i in range(length):
        for j in range(length):
            temp_parent = copy.copy(parent)
            if i != j:
                begin = copy.copy(i)
                end = copy.copy(j)
                while begin < end:
                    temp = temp_parent[end]
                    temp_parent[end] = temp_parent[begin]
                    temp_parent[begin] = temp
                    begin += 1
                    end -= 1
                string_parent = copy.copy(temp_parent)
                children.append(temp_parent)

    return children

def selectChildren(childrennodes, g):
    # temporary lists needed for sorting the nodes according to their score
    scores = []
    children = []
    genomes = []

    # calculate "fitness" scores and filter out double genomes
    for i in range(len(childrennodes)):
        if (childrennodes[i].cargo not in genomes):
            s = generationScore(childrennodes[i].cargo, g)
            scores.append(s)
            children.append(childrennodes[i])
            genomes.append(childrennodes[i].cargo)

    # check which (beamwidth number of) genomes have the best scores
    dictionary = heapq.nsmallest(beam, zip(scores, children))

    # put the best genome nodes in a list before returning
    best_children = []
    for j in range(len(dictionary)):
        best_children.append(dictionary[j][1])

    childrennodes = []
    scores = []
    return best_children

# algorithm
def runSimulation(start, solution, beam):
    """
    Returns minumum number of time steps needed to get to solution
    """
    solutionNodes = []
    queue = []
    g = 0
    solution_found = False

    pare_node = Node(start)
    m = (0, pare_node)
    heappush(queue, m)

    while ((queue != []) and (g <= maxGenerations) and (solution_found == False)):
        print "--- Computing generation", g, "---"
        nextGeneration = []
        g += 1

        # make a bunch of children from the selected parents and add them to the graph
        for b in range(beam):
            if (queue != []):
                pare_node = heappop(queue)
                children = generateAllChildren(pare_node[1].cargo)
                for i in range(len(children)):
                    # create nodes
                    node = Node(children[i], pare_node[1])
                    nextGeneration.append(node)

        # make a selection of this generation and reset queue for next generation
        c = selectChildren(nextGeneration, g)
        queue = []

        # check selection for the solution or else use them as parents
        # to make the next generation
        for i in range(len(c)):
            if (c[i].cargo == solution):
                solution_found = True
                solutionNodes.append(c[i])
                print "Solutions found:", len(solutionNodes)
                break
            else:
                score = generationScore(c[i].cargo, g)
                l = (score, c[i])
                if (len(queue) <= maxQueue):
                    heappush(queue, l)
                else:
                    heappushpop(queue, l)

    # only print shortest solutions
    lowest = 50
    inversions = 0
    for j in range(len(solutionNodes)):
        node = solutionNodes[j]
        while((node.prev != None) and (inversions < lowest)):
            print "Step", node
            node = node.prev
            inversions += 1
        if (inversions < lowest):
            lowest = inversions
            print "Inversions: ", inversions
            print "Start:", start
        j += 1

# starting points ##############################################################
start = [23,1,2,11,24,22,19,6,10,7,25,20,5,8,18,12,13,14,15,16,17,21,3,4,9]
solution = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

## size: 4 ## ideal beam = at least 4 to 50
# start = [2,1,4,3]
# solution = [1,2,3,4]

## size: 6 ## ideal beam = 50
# start = [1,2,3,5,6,4]
# solution = [1,2,3,4,5,6]

## size: 7 ## ideal beam = 25
# start = [1,2,7,3,5,6,4]
# solution = [1,2,3,4,5,6,7]

## size: 8 ## ideal beam = 120
# start = [4,2,3,1,6,8,7,5]
# solution = [1,2,3,4,5,6,7,8]

## size: 9 ## ideal beam = 120
# start = [1,2,3,4,6,8,9,7,5]
# solution = [1,2,3,4,5,6,7,8,9]

## size: 10 ## ideal beam = 90 or 95
# start = [4,2,3,1,10,6,8,9,7,5]
# solution = [1,2,3,4,5,6,7,8,9,10]

## size: 11 ##
# start = [4,2,3,1,6,11,10,9,8,7,5]
# solution = [1,2,3,4,5,6,7,8,9,10,11]

# start = [4,2,3,1,6,11,10,9,8,7,5]
# solution = [1,2,3,4,5,6,7,8,9,10,11]

stringsol = copy.copy(solution)

counter = 0
while (beam < 10000):
    print "run:", counter
    print "beam:", beam
    runSimulation(start, solution, beam)
    print "---", (time.time() - start_time), "seconds ---"
    counter += 1
    beam += 20
