import random

melan = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9]
miran = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
inversions = 0
leng = len(melan) - 1
while melan != miran:
    i = random.randint(0, leng - 1)
    j = random.randint((i + 1), leng)
    if melan[i] > melan[j]:
        while i < j:
            temp = melan[j]
            melan[j] = melan[i]
            melan[i] = temp
            i += 1
            j -= 1
            inversions += 1
        print melan
print inversions
