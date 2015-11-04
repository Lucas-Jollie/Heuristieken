# Lucas Jollie
# 10456201
# Creates random genomes of length 25 dependent on user input
# Can be tested in genetic inversions project
# results are stored in genome.txt


# import random module
import random

# ask amount of genomes to generate
amount = input("How many genomes? ")

# create file containing genomes
genomeFile = open("genome.txt", 'w')

for i in range(amount):
    
    # initialize list genome
    genome = []
    # continues while genome not complete
    while len(genome) != 25:
        
        # random int and append if not present
        gene = random.randint(1,25)
        
        if gene not in genome:
            genome.append(gene)
            
    # write genome and newline to file
    genomeFile.write(str(genome))
    genomeFile.write("\n")
