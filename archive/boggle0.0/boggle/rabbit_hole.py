'''
  author: matt pladna
  
  create date: 2014.05.10
  
  summary:
  go down the rabbit hole...goal is exhaust every possible adjacent character
  and build a word list.  this function is recursive and should track positions
  visited and the letters as it goes.
  
  note: this is not efficient...it's purely brute force and takes a long time
  to run. 
  
  note 2.0: this won't scale with boggle boards that need to get bigger for 
  smartypants people to make words off of (go play scrabble people).
  
  note 3.0: see faster.py...it's faster
'''

import copy
import boggle.location as bl

# there has to be a better way...
class BadRabbit(Exception):
  def __init__(self, value):
      self.value = value
  def __str__(self):
      print repr(self.value)
      
##
 # rabbit_hole takes the board, game settings, and a path dictionary to track
 # the positions moved to create words.
 #
 # goal is to call the function for each adjacent letter recursively and produce
 # word lists
 ### 
def rabbit_hole(board, settings, position, path = {}, word = '', words = []):
    # get adjacent tiles for the position
    (row, col) = position
    adjs = bl.get_adjs(row, col, settings['max_r'], settings['max_c'], path)

    # update path and word
    letter = board[row][col]
    
    if letter == 'q':
        letter = letter + 'u'
        
    path[str(position)] = letter
    word = word + letter
    
    if len(word) >= settings['min_len']:
        words.append(word)
        
    for position in adjs:
        path_copy = copy.copy(path) # create a copy so each call gets it's own
        rabbit_hole(board, settings, position, path_copy, word)
    
    return words
