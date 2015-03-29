# test getAdjacents function

import sys
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))# go to test

sys.path.append('..') # add in previous directory to get to package
import boggle.board as bb

# constants for board
MAX_C = 4
MAX_R = 4

# check for arguments
if len(sys.argv) != 2:
    print "need to pass in a board file"
    exit(1)
    
# test adjacents
board = bb.read_board(sys.argv[1], MAX_R, MAX_C)

print board
print "verify row 0, column 1 is " + board[0][1]

