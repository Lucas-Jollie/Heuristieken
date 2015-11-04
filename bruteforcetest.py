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

# def combinations(iterable, r):
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

test = list(itertools.combinations(range(1,26), 25))
print test
