# BoggleTest.py
#
# Programming Rules:
#  1. Python 2.7.x or Python 3.3.x maybe used.
#     A. Please document which version was used.
#     B. Include make files or project files where appropriate.
#  2. Any core language feature may be used.
#  3. 3rd Party modules (such as Boost) are not allowed.
#  4. Sample board and dictionary files provided.
#  5. Submit all source files needed to run the solution.
#
# Game Rules:
#  Boggle is a word game.  The goal is to make as many words as possible
#  out of the given set of letters laid out in a 4x4 grid.  Words are 
#  formed by starting with any letter and moving to an adjacent letter
#  (up, down, left, right, or diagonal) and so-forth on.  Once a letter
#  is used in a word, it can not be used again.  All words must be a 
#  minimum of 3 characters in length.  Finally, in this version, a "q"
#  will always represent "qu", since "u" nearly always follows "q" in
#  English.  If a word may be formed multiple ways on the same board, it
#  only counts once.
#
# Example:
#
# Board:
#    P W Y R
#    E N T H
#    G S I Q
#    O L S A
#
# A few possible words:
#   pen
#   peg
#   quit
#   hit
#   slit
#   slits
#
# Command line arguments:
#  python BoggleTest.py <dictionary_filename> <board_filename> <output_filename>
#
# Dictionary:
#  The dictionary file is an ASCII text file that lists acceptable words.  Each word is
#  new line separated.  Words are in alphabetical order and all lowercase, utilizing
#  only letters 'a' to 'z'.
#
# Board:
#  The board file is an ASCII text file that is 4 lines of 4 characters.  These
#  represent the game board, a 4x4 matrix of characters.  These may be mixed case.
#  Whitespace is optional and should be ignored.  Only letters 'a' to 'z' or 'A'
#  to 'Z' are used.
#
# Output:
#  The output should be an ASCII text file (in alphabetical order) of all legal words
#  possible to spell on the current board that are in the given dictionary.  These
#  should be all lowercase and newline separated (same format as the dictionary).
#
# Notes:
#  Your final solution should be PRODUCTION QUALITY, as if it is getting checked
#  in to live production code.

import sys
import os

os.chdir(os.path.dirname(os.path.abspath(__file__))) # go to executable

# get modules
sys.path.append('lib')

import boggle.dictionary as bd
import boggle.location as bl
import boggle.board as bb
import boggle.rabbit_hole as brh

##
 # constants for game
 ###
MAX_R = 4 # max rows
MAX_C = 4 # max columns
MIN_LEN = 3 # min length of word

##
 # play a round of boggle and win to the nth degree!
 ###
if __name__ == '__main__':    
    if len(sys.argv) != 4:
        print "Usage: BoggleTest <dictionary_filename> <board_filename> <output_filename>"
        sys.exit(1)
    
    # bring in board
    print "making sure your board is cool..."
    
    try:
        board = bb.read_board(sys.argv[2], MAX_R, MAX_C)
    except Exception, e:
        print "error with reading board; " + str(e) 
        exit(1)
    
    settings = {
        'max_r': MAX_R, 'max_c': MAX_C, 'min_len': MIN_LEN}
    
    # generate possible word list
    print "creating possible list of words..."
    strings = []
    
    try:
        for r_idx, row in enumerate(board):
            for c_idx, col in enumerate(row):
                position = [r_idx, c_idx] # crete start position
                path = {} # create a fresh dictionary (organic, non-gmo)
                strings = brh.rabbit_hole(board, settings, position, path)    
    except Exception, e:
        print "error with creating word list; " + str(e) 
        exit(1)
        
    print "strings generated: " + str(len(strings))
    
    # bring in dicionatry
    print "reading your list, checking it twice..."
    
    try:
        dictionary = bd.read_dictionary(sys.argv[1])
    except Exception, e:
        print "error with reading dictionary; " + str(e) 
        exit(1)
        
    # compare list to dicionatry and keep matching results
    words = {} # store in a list to keep it unique
    for word in strings:
        if dictionary.has_key(word):
            words[word] = 0           
    
    # writeOutput
    if len(words) > 0:
        print "writing your answers..."
        
        try:
            output = open(sys.argv[3], 'w')
            awords = words.keys()
            awords.sort()
            output.writelines("\n".join(awords))
            output.write("\n")
            output.close
        except Exception, e:
            print "can't write " + sys.argv[3] + "; " + str(e)
            exit(1)
    else:
         print(
           "this is awkward...nothing to write; was your board all vowells"
           " or consonants?"
         )
        

    sys.exit(0)
