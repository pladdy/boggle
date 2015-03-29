import re
from collections import deque

class BoardException(Exception): 
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self)

class Board():
    '''
    The Board is a graph data structure; each node will represent a letter
    on the boggle board.  The node id is the coordinate of the letter on the
    board.  The node itself is a dictionary with the letter stored along 
    with any neighboring nodes.  The board is stored like an adjaceny list.
    Although not as memory efficient as the matrix it's more convenient
    pulling the neighbors as a word path is built with them stored in each
    node.
    
    Internally all letters are stored lowercase; words passed in are also
    made lowercase.
    
    Below is an example of a board file and how it's represented in the 
    class.
    
    board    matrix indexes*   *board is stored as a dictionary and order is
    P W Y R  0,0 0,1 0,2 0,3    not critical; using a breadth-first search
    E N T H  1,0 1,1 1,2 1,3    is fairly efficient best and worst case.
    G S I Q  2,0 2,1 2,2 2,3    the tuple indexes are used to establish
    O L S A  3,0 3,1 3,2 3,3    how far letters are from one another.
    '''
    RANGE_TO_NEIGHBORS = (-1, 0, 1)
    LETTER_REGEX = re.compile('[a-zA-Z]')
    
    def __init__(self):
        self.nodes = {}
        self.edges = {}
        
    def AddNode(self, id, letter):
        """Add nodes one at a time by assigning a tuple representing the 
           matrix index of the node on the board as the key and the 
           letter it represents.
        """
        if self.__IsALetter(letter):
            self.nodes[id] = {'letter': letter.lower(), 'neighbors': {}}
            self.__AddNeighbors(id)
        else:
            raise BoardException('board can only have letters as nodes')
    
    def CheckForWord(self, word):
        '''Given a word search the board to see if it's possible to find a
           path that allows the word to be constructed.  once the first letter
           is found, a queue is created with the matching nodes neighbors.
           first node in queue is removed and inspected with each match having
           it's neighbors inserted into the queue.
        '''
        word = word.lower()
        word = word.replace('qu', 'q') # condense qu to q for matching
        chars = list(word.lower())
        
        nodes = self.GetNodes()
        for id in nodes:
            path = neighbors = []
            queue = deque([id])
            
            while len(queue) > 0:
                id = queue.popleft()
                node = self.GetNode(id) 
                
                ## if the node letter matches the next letter in word add ndoe
                 # to path; on a failure shorten the neighborhood to track a
                 # potential dead end
                if node['letter'] == chars[len(path)]:
                    if id in path: continue # skip any node in path
                    
                    path.append(id)
                    if len(word) == len(path): return True
                    
                    neighbors = self.GetNeighbors(id)
                    queue.extendleft(neighbors)
                elif len(neighbors) > 0: 
                    neighbors.pop()                   

                ## if a dead end is reached and a path exists, back up to
                 # remove the dead end and create a new queue minus the dead
                 # end node
                if len(neighbors) == 0 and len(path) > 0:
                    bad_id = path.pop()
                    queue = []
                    if len(path) > 0:
                        neighbors = self.GetNeighbors(path[-1])
                        queue = deque(neighbors)
                        queue.remove(bad_id)
                    
        return False
        
    def GetNeighbors(self, id):
        if id in self.nodes: return list(self.nodes[id]['neighbors'].keys())
        else: return None
        
    def GetNode(self, id):
        if id in self.nodes: return self.nodes[id]
        else: return None
            
    def GetNodes(self):
        return self.nodes
        
    def FileToBoard(self, board):
        """Build a graph data structure from a board file."""
        try:
            input = open(board)
            lines = input.readlines()
        except:
            raise BoardException("can't read board")
            
        # create a node for each letter in the file
        for i in range(len(lines)):  
            # remove whitespace in line
            p = re.compile('\s+')
            line = p.sub('', lines[i])
            
            chars = list(line) 
            for j in range(len(chars)):
                if self.__IsALetter(chars[j]): self.AddNode((i, j), chars[j])
        
    ## private methods ###
    def __AddNeighbors(self, id):
        '''Given a node, add all neighboring nodes to the nodes neighbors list.
           a node is a neighbor if it's adjacent; in the matrix a neighbor
           is +/- 1 index away from the node
        '''
        owner = self.GetNode(id)
        for i in self.RANGE_TO_NEIGHBORS:
            r = i + id[0]
            
            for j in self.RANGE_TO_NEIGHBORS:
                c = j + id[1]
                if (r, c) == id: continue # skip self
                
                # check if a neighbor exists; if so add each to their neighbors
                # lists and update edges with the connections
                neighbor = self.GetNode((r, c))
                if neighbor != None:
                    owner['neighbors'][(r, c)] = 1
                    neighbor['neighbors'][id] = 1

    def __IsALetter(self, letter):
        if self.LETTER_REGEX.match(letter) and len(letter) == 1: return True
        else: return False
