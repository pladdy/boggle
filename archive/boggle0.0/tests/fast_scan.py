# test getAdjacents function

import sys
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))# go to test

sys.path.append('..') # add in previous directory to get to package
import boggle.faster as bf

# check for arguments
if len(sys.argv) != 2:
    print "need to pass in a word to match"
    exit(1)
    
board = [
    ['p', 'w', 'y', 'r'], 
    ['e', 'n', 't', 'h'], 
    ['g', 's', 'i', 'q'], 
    ['o', 'l', 's', 'a']
]

MIN_LEN = 3

check = bf.fast_scan(sys.argv[1], board, MIN_LEN)

print check

