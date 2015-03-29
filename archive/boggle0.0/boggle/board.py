'''
  author: matt pladna
  
  create date: 2014.05.10
  
  summary:
  handles reading the board, scrubbing it, and returning it as a list to the 
  caller.
  
  board example:
  P W Y R
  E N T H
  G S I Q
  O L S A
'''

import re
import warnings

# my own exception
class BadBoard(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
        
## 
 # readBoard takes a board file and reads/parses it
 ###
def read_board(board_file, max_r, max_c):
    board = []
    
    try:
        input = open(board_file)
        lines = input.readlines()
    except:
        raise BadBoard("can't read file, check path")
        
    ##
     # read each line and remove non letters; check count of columns and
     # rows as well
     ###
    bad_board_err = "board should be " + str(max_r) + " x " + str(max_c)
    
    for line in lines:
        p = re.compile('[^a-zA-Z]')
        if re.match(p, line): # invalid chars present, alert user
            warnings.warn("invalid chars in board, removing...")
        
        # scrub out anything not a letter and lowercase
        new_line = re.sub(p, '', line)   
        new_line = new_line.lower()
        chars = list(new_line)

        if len(chars) != max_c: # check column count
            info = count_check(len(chars), max_c)
            raise BadBoard(info + ", " + bad_board_err)
            
        board.append(chars)

    if len(board) != max_r: # check row count
        info = count_check(len(board), max_r)
        raise BadBoard(info + ", " + bad_board_err)
        
    return board

## simple function to compare counts and return a string ###
def count_check(count, max):
    if count < max:
        return "count is too low"
    elif count > max:
        return "count is too high"
    
