'''
  author: matt pladna
  
  create date: 2014.05.10
  
  summary:
  rather than compute possibilities, check the dictionary against the board and
  remove words that can't match.  for words that can match go letter by letter
  and if you can complete the word add to output.
'''

import boggle.location as bl

# slow down!  there's an error!
class NotSoFast(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        print repr(self.value)
  
##
 # given a word scan for it's letters in adjacent spaces in the given board
 ###
def fast_scan(word, board, min_len = 0):
    if len(word) < min_len:
        return False
        
    chars = list(word)

    # if we have a match let's do this    
    if str(board).find(chars[0]) == -1:
        return False
        
    max_r = len(board)
    max_c = len(board[0])
    
    ## 
     # iterate through rows and their columns to see if there's a match; on a 
     # match see if word can be built with adjacent letters
     ###
    junk = None
    
    for r_idx, row in enumerate(board):        
        for c_idx, col in enumerate(row): 
            letter = board[r_idx][c_idx]
            
            # once we hit a match, look for the word            
            if letter == chars[0]:                     
                match = chars.pop(0)
                
                # if q, grab the u (it rhymes!)
                if match == 'q' and chars.index('u') == 0:
                    match = match + chars.pop(0)
                
                path = {} # set path
                path[str([r_idx, c_idx])] = letter                
                adjs = bl.get_adjs(r_idx, c_idx, board, path)
                
                # build args list for function
                opts = {
                    # constants
                    'word': word, 'board': board, 'chars': chars,
                    # dynamics
                    'row': r_idx, 'col': c_idx, 'path': path, 'adjs': adjs
                }
                
                junk = scan_adjs(opts, match)
                
                chars.insert(0, match) # put letter back
    return junk

                            
##
 # scan_adjs will go through the list of adjacent tiles and scan for matches by
 # building and testing strings. 
 ###
def scan_adjs(opts, match, words = {}):
    ## check each left over letter against the adjacents ###
    for char in opts['chars']:
        ## go through the adjacents until you get a match ###
        for adj in opts['adjs']:
            letter = opts['board'][adj[0]][adj[1]]
            
            if letter == 'q':
                letter = letter + 'u'
            
            if letter == char:
                # if we went down the wrong rabbit hole and can't match, skip
                if opts['word'].find(match + letter) != 0:
                    continue
                    
                match = match + letter
                    
                # if a match happens catalog it
                if opts['word'] == match: 
                    words[match] = len(match)
                    
                # update scan options                
                opts['path'][str([adj[0], adj[1]])] = letter
                
                opts['adjs'] = bl.get_adjs(
                    adj[0], adj[1], opts['board'], opts['path'])                
                
                opts['row'] = adj[0]
                opts['col'] = adj[1]

                scan_adjs(opts, match)
    
    if words.has_key(opts['word']):
        return True
    else:
        return False
