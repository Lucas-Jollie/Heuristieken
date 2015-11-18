import random
genomeFile = open("kortrandom.txt", 'w')

for i in range(0,100):
    random_list = random.sample(xrange(1,26),25)
    print random_list
    genomeFile.write(str(random_list))
    genomeFile.write("\n")
