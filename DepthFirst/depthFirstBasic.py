# Groupname: Aardbeizonder
# Names: Lucas Jollie, Bart Quaink, Anneke ter Schure
#
# File: depthFirst.py
# Goal: find the best solution with the least amount of steps
#
# -------------------------------------------------------------------------------

# initialise
stack = []
tree = 
graph.unmarkAllVertices
vertex = rootVertex
stack.push(vertex)
graph.markVertex(vertex)

# algorithm
def runSimulation():
    """ Returns minumum number of time steps needed to get to solution"""

    # initialise stack where genomes can be pushed in
    # -------usage--------------
    # stack = [3, 4, 5]
    # stack.append(6) --> [3, 4, 5, 6]
    # stack.pop() --> [3, 4, 5]

    # starting point
    Fruitfly.genome = [23,1,2,11,24,22,19,6,10,7,25,20,5,8,18,12,13,14,15,16,17,21,3,4,9]
    solution = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

    while (stack not empty && solution not found):
        parent = stack.pop()
        c = GenerateAllChildren(parent)
        for i in range(c):
            if (i not in archive):
                archief.add(i)
            else:
                if (i == solution):
                    print i
                    break
                stack.append(i)

runSimulation()
