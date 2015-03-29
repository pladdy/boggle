# test getAdjacents function

import sys
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))# go to test

sys.path.append('..') # add in previous directory to get to package
import boggle.rabbit_hole as brh
    
# build some test vars
board = [
    ['B', 'A', 'F', 'O'], ['D', 'T', 'O', 'S'], ['Y', 'I', 'S', 'N'],
    ['T', 'E', 'G', 'Z']
]
settings = {'min_len': 3, 'max_r': 4, 'max_c': 4}

#board = [['B', 'A', 'F'], ['D', 'T', 'O'], ['Y', 'I', 'S']]
#settings = {'min_len': 3, 'max_r': 3, 'max_c': 3}

#board = [['B', 'A'], ['D', 'T']]
#settings = {'min_len': 3, 'max_r': 2, 'max_c': 2}

words = []

for r_idx, row in enumerate(board):
    for c_idx, col in enumerate(row):
        position = [r_idx, c_idx] # crete start position
        path = {} # create a fresh dictionary (organic, non-gmo)
        words = brh.rabbit_hole(board, settings, position, path)

print "word count: " + str(len(words))

