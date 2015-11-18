# Groupname: Aardbeizonder
# Names: Lucas Jollie, Bart Quaink, Anneke ter Schure
#
# File: depthFirst.py
# Goal: find the best solution with the least amount of steps
#
# -------------------------------------------------------------------------------

# initialise
stack = []
archive = []
tree =
graph.unmarkAllVertices
vertex = rootVertex
stack.push(vertex)
graph.markVertex(vertex)

def GenerateAllChildren(parent):
    """
    Generates all children of parent
    Based on inversions of size 2
    """
    children = []
    real_parent = parent
    for i in range(len(parent) - 1):
        if i != 0:
            parent = real_parent
        temp = parent[i]
        parent[i] = parent[i + 1]
        parent[i + 1] = temp
        children.append(parent)

    return children


# algorithm
def runSimulation():
    """
    Returns minumum number of time steps needed to get to solution
    """

    # initialise stack where genomes can be pushed in
    # -------usage--------------
    # stack = [3, 4, 5]
    # stack.append(6) --> [3, 4, 5, 6]
    # stack.pop() --> [3, 4, 5]

    # starting point
    # Fruitfly.genome = [23,1,2,11,24,22,19,6,10,7,25,20,5,8,18,12,13,14,15,16,17,21,3,4,9]
    # solution = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    start = [4,2,3,1]
    solution = [1,2,3,4]
    solution_found = False
    stack.append(start)

    while (stack != [] && !solution_found):
        parent = stack.pop()
        c = GenerateAllChildren(parent)

        for i in range(len(c)):
            if (stack[i] not in archive):
                archive.add(i)
            elif (stack[i] == solution):
                solution_found = True
                print stack[i]
                break
            else:
                stack.append(c[i])

runSimulation()
