import time
from functools import wraps
import cProfile
import numpy
import Levenshtein


def acquaintance(a, b):
    l_result = Levenshtein.distance(a,b)
    print(l_result)
    result = Levenshtein.ratio(a, b)
    print(result)

a = 'newspapers'
b = 'text'
acquaintance(a, b)


#
# def levenshtein2(s1, s2):
#     if len(s1) < len(s2):
#         return levenshtein2(s2, s1)
#
#     # len(s1) >= len(s2)
#     if len(s2) == 0:
#         return len(s1)
#
#     previous_row = range(len(s2) + 1)
#     for i, c1 in enumerate(s1):
#         current_row = [i + 1]
#         for j, c2 in enumerate(s2):
#             insertions = previous_row[
#                              j + 1] + 1  # j+1 instead of j since previous_row and current_row are one character longer
#             deletions = current_row[j] + 1  # than s2
#             substitutions = previous_row[j] + (c1 != c2)
#             current_row.append(min(insertions, deletions, substitutions))
#         previous_row = current_row
#
#     return previous_row[-1]
# result1 = Levenshtein.distance('picture','no')
# #result = levenshtein2('picture','well')
# print(result1)
