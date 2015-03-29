'''
  author: matt pladna
  
  create date: 2014.05.10
  
  summary:
  handle reading and processing the dictionary/list of words
'''

# to handle the naughtiness
class BadDictionary(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
##
 # read in dictionary and return dictionary of the dictionary (mind = blown);
 # also calculate max length so we don't compute words that can't be used
 ###
def read_dictionary(dictionary_file):
    dictionary = {}
    
    try:
        input = open(dictionary_file)
    except:
        raise BadDictionary("can't open dictionary file")
         
    ## go through lines and load into memory ###
    max_len = 0 # track max length of words
    
    for line in input.readlines():
        line = line.strip() # clobber whitespace

        dictionary[line.lower()] = len(line) # lowercase the key, store length
        
    return dictionary
