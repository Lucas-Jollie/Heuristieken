# beamSearch(problemSet, ruleSet, memorySize):
#     openMemory = new memory of size memorySize
#     nodeList = problemSet.listOfNodes
#     node = root or initial search node
#     Add node to openMemory;
#     while (node is not a goal node)
#          Delete node from openMemory;
#          Expand node and obtain its children, evaluate those children;
#          If a child node is pruned according to a rule in ruleSet, delete it;
#          Place remaining, non-pruned children into openMemory;
#          If memory is full and has no room for new nodes, remove the worst
#              node, determined by ruleSet, in openMemory;
#          node = the least costly node in openMemory;


def beamsearch(cost, extra, intitial, B, E):
    melano = []
    B = max(B, len(intitial))
    hlist = [(0, tmp) for tmp in initial]
    while len(hlist) > 0:
            hlist.sort
