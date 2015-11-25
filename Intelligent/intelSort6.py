melan = [3, 1, 2]
miran = [1, 2, 3]
options = []
shortest = len(melan)
length = len(melan) - 1

for i in range(length):
    for j in range(length):
        if i == j:
            j += 1
        elif i < j:
            while i < j:
                temp = melan[j]
                melan[j] = melan[i]
                melan[i] = temp
                i += 1
                j -= 1
            inversions += 1
        elif i > j:
            while i > j:
                temp = melan[j]
                melan[j] = melan[i]
                melan[i] = temp
                i -= 1
                j += 1
            inversions += 1
    
