# import random module
import random

# define lists of melanogaster and miranda genomes
#melan = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9]
miran = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

# define inversions and genome index
inversions = 0
leng = len(miran) - 1
k = 0

for k in range(0, 1000, 1):
    melan = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9]
    # repeat until genomes equal
    while melan != miran:
        
        # generates random indices of 0 <= i < j <= leng
        i = random.randint(0, leng - 1)
        j = random.randint((i + 1), leng)
        
        # swaps if lower bound is greater than upper bound
        if melan[i] > melan[j]:
            while i < j:
                temp = melan[j]
                melan[j] = melan[i]
                melan[i] = temp
                i += 1
                j -= 1
            inversions += 1
            
            # prints genome after inverting
#            print melan
            
    # report amount of inversions
print inversions/1000.0
