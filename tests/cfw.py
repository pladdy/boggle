''' simple test of check for word functionality
'''

import sys
import os

os.chdir(os.path.dirname(__file__)) # go to executable

# get modules
sys.path.append('..')
import boggle

board = boggle.Board()
board.FileToBoard('../board_1.txt')

word = 'list'
print(word + ' should be true:\n')
print(board.CheckForWord(word)) # should be true
print()

word = 'question'
print(word + ' should be false:\n')
print(board.CheckForWord(word))
print()
