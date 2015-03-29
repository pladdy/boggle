# test dictionary module

import sys
import os

os.chdir(os.path.dirname(os.path.abspath(__file__))) # go to test

sys.path.append('..') # to get to module
import boggle.dictionary as bd

# check for arguments
if len(sys.argv) != 2:
    print "need to pass in a dictionary file"
    exit(1)
    
dictionary = bd.read_dictionary(sys.argv[1])

## print 10 dictionary items to check them ###
print "here's a sample of the words and lengths"
i = 0

for k in dictionary.keys():
  print k + ", len:" + str(dictionary[k])
  i = i + 1
  if i >= 10:
      break
