'''
  author: matt pladna
  
  create date: 2014.05.10
  
  summary:
  given a position (row, col) this will return the valid adjacent tiles you can
  can use to check for a word.  it takes a path dictionary as well so it knows
  what positions you've checked (so it won't include them as adjacents to check)
  
  grid example:  
  0,0 0,1 0,2 0,3
  1,0 1,1 1,2 1,3
  2,0 2,1 2,2 2,3
  3,0 3,1 3,2 3,3
  
'''

# where my error at?
class BadLoc(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
        
##
 # get_adjs will return the possible adjacent locations given a row position
 # and a column position
 ###
def get_adjs(row, col, board, path={}):    
    adjs = []
    
    max_r = len(board) - 1 # offset to match array indices
    max_c = len(board[0]) - 1
    
    # check for valid index ranges
    info = "value must be array index between 0 and "
    
    if row > max_r or row < 0:
        raise BadLoc("row = " + str(row) + "; " + info + str(max_r))
    if col > max_c or col < 0:
        raise BadLoc("col = " + str(col) + "; " + info + str(max_c))
        
    rows = get_combo(row, max_r)    
    cols = get_combo(col, max_c)
    
    ## go through rows and columns and build list
    for i in rows:
        for j in cols:
            if i == row and j == col: # skip self
                next
            else:
                if "[%s, %s]" %(i, j) not in path.keys():
                    adjs.append([i, j])
                
    return adjs
    
## 
 # given an integer and a ceiling (int) attempt to provide one number less and
 # one number more of the integer.  this uses the boards maximum rows/columns
 # to see what tiles can be adjacent to a position on the board.
 #
 # ex: get_combo(0, 1)
 #
 # returns 1
 ###
def get_combo(i, max_i):
    combos = [i]
    
    if i < max_i:
        combos.append(i + 1)
    if i > 0:
        combos.append(i - 1)
        
    return combos

