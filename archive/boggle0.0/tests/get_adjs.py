# test getAdjacents function

import sys
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))# go to test

sys.path.append('..') # add in previous directory to get to package
import boggle.location as bl


# check for arguments
if len(sys.argv) != 4:
    print "need to pass in a position: ex: 0 0 board_file"
    exit(1)
    
# test adjacents
throw_out = {'0,0': 0} # throw this key out for testing

adjacents = bl.get_adjs(
    int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], throw_out)

print "positions should exclude 0,0 as part of the test"

for position in adjacents:
    print "%s,%s" %(position[0], position[1])

