# Groupname: Aardbeizonder
# Names: Lucas Jollie, Bart Quaink, Anneke ter Schure
#
# File: depthFirst.py
# Goal: find the best solution with the least amount of steps
#
# -------------------------------------------------------------------------------

# inititalise genome class
class Fruitfly(object):
    """ Represents the genome of a fruitfly """
    def __init__(self, genome):
        """ Initializes genome as a list with particular size """
        self.genome = []
        
    def GetSequence(self):
        """ Returns the current genome sequence """
        return self.genome

# initialise archive maybe using pygtrie?
class Archive(object):
    """ Represents a trie datastructure containing all past genomes """
    def __init__(self, rootnode):
        self.rootnode


# algorithm
def runSimulation():
    """ Returns minumum number of time steps needed to get to solution"""

    # initialise stack where genomes can be pushed in
    # -------usage--------------
    # stack = [3, 4, 5]
    # stack.append(6) --> [3, 4, 5, 6]
    # stack.pop() --> [3, 4, 5]
    stack = []

    # starting point
    Fruitfly.genome = [23,1,2,11,24,22,19,6,10,7,25,20,5,8,18,12,13,14,15,16,17,21,3,4,9]
    solution = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

    while (stack not empty && solution not found):
        parent = stack.pop()
        c = GenerateAllChildren(parent)
        for i in range(c):
            if (! archief.bevat(i)):
                archief.add(i)
            else:
                if (i == solution):
                    print i
                    break
                stack.append(i)

runSimulation()
