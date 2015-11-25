
# def sort(ins, i):
#     if i == 0: return
#     sort(ins, i-1)
#     j = i
#     while j > 0 and ins[j-1] > ins[j]:
#         ins[j-1], ins[j] = ins[j], ins[j-1]
#         j -= 1
#     return ins
#
# a = [3,4,5,2,1]
# i = 1

# print sort(a,i)

# def sort2(ins):
#     for i in range(1, len(ins)):
#         j = i
#         while j > 0 and ins[j-1] > ins[j]:
#             ins[j-1], ins[j] = ins[j], ins[j-1]
#             j -= 1
#
# print sort2(a)

# def combinations(iterable, r) van der sende:
#     # combinations('ABCD', 2) --> AB AC AD BC BD CD
#     pool = tuple(iterable)
#     n = len(pool)
#     if r > n:
#         return
#     indices = range(r)
#     yield tuple(pool[i] for i in indices)
#     while True:
#         for i in reversed(range(r)):
#             if indices[i] != i + n - r:
#                 break
#         else:
#             return
#         indices[i] += 1
#         for j in range(i+1, r):
#             indices[j] = indices[j-1] + 1
#         yield tuple(pool[i] for i in indices)
#
# print combinations(range(4), 3)

import itertools

genomes = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

# test = list(itertools.combinations(range(1,26), 25))
# print test == genomes
#
# bla = list(range(1,10))
# print bla

import random
# trial = ' '
# while trial != genomes:
#     trial = str(random.randint(1,25))
#     print trial
#     if trial == genomes:
#         print('Forced match found:' + trial)
#         input()

# bforce = []
# while bforce != genomes:
#         while len(bforce) != 25:
#             gene = random.randint(1,25)
#             if gene not in bforce:
#                 bforce.append(gene)
#         print bforce

import logging
import time

# BRUTE FORCE SHORT
# genomes = [1,2,3,4,5]
# random_list = []
loops = 0
# while random_list != genomes:
#     random_list = random.sample(xrange(1,6),5)
#     print random_list
#     loops += 1
#     if random_list == genomes:
#         print 'SUCCCES, number of loops: ', loops

# logger
# create logger
# logger = logging.getLogger("logging_tryout2")
# logger.setLevel(logging.DEBUG)
#
# # create console handler and set level to debug
# ch = logging.StreamHandler()
# ch.setLevel(logging.DEBUG)
#
# # create formatter
# formatter = logging.Formatter("%(asctime)s;%(levelname)s;%(message)s")
#
# # add formatter to ch
# ch.setFormatter(formatter)
#
# # add ch to logger
# logger.addHandler(ch)

# BRUTE FORCE LONG
random_list = []

solved_list = []

# begin = logger.info("Started")

# while random_list != genomes:
#     random_list = random.sample(xrange(1,26),25)
#     print random_list
#     loops += 1
#     if random_list == genomes:
#         print 'SUCCCES, number of loops: ', loops
#         break

# # "application" code
# print 'FINISHED:    ' , logger.info('done')

# Brute force test 2
# random_list = random.sample(xrange(1,26),25)
# for i in genomes:
#     while genomes[i] != random_list[i]:
#         if i == len(random_list):
#             i = 0
#         temp  = random_list[i]
#         random_list[i] = random_list[i+1]
#         random_list[i+1] = temp
#         i += 1
#         print i

# Extreem brute force test -----------------------------------------------------
# maakt een random list en shuffelt deze totdat hij klopt
from random import shuffle
random_list = random.sample(xrange(1,6),5)
start_time = time.time()
while random_list != genomes:
    if random_list != solved_list:
        shuffle(random_list)
        solved_list.append(random_list)
        print random_list
if random_list == genomes:
    elapsed_time = time.time() - start_time
    print elapsed_time, ' seconds'

# breadth first
breadth_list = []
