import random
<<<<<<< HEAD
genomeFile = open("100randomgenomes.txt", 'w')
=======
# genomeFile = open("kortrandom.txt", 'w')
>>>>>>> 57d396854fb1310eb1eadd302175c706c69f7bf5

for i in range(0,100):
    random_list = random.sample(xrange(1,26),25)
    print random_list
    # genomeFile.write(str(random_list))
    # genomeFile.write("\n")
