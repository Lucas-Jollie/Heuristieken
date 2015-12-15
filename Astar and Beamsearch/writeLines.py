def writeStart(steps, counter, genome):
    """
    Writes the genome #counter to file 'steps'

    """
    # writes start of trial
    steps.write("#")
    steps.write(str(counter))
    steps.write(",")
#    for i in range(len(melan)):
#        steps.write(str(melan[i]))
#        steps.write(",")
    steps.write(str(genome))
    steps.write(", ")
    
def writeSolution(steps, solution):
    """
    Writes the amount of inversions needed
    to complete a genome to the file steps.
    """
    steps.write("Inversions: ")
    steps.write(str(solution))
    steps.write("\n")
