from itertools import product
from bisect import bisect_left, insort_left


dictionary = []
for n in range(1, 6):
    for words in map(''.join, product('AEIOU', repeat=n)):
        insort_left(dictionary, words)

def solution(word):
    return bisect_left(dictionary, word) + 1
