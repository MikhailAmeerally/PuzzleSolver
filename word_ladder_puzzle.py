from puzzle import Puzzle



class WordLadderPuzzle(Puzzle):
    """

    A word-ladder puzzle that may be solved, unsolved, or even unsolvable.
    
    """

    def __init__(self, from_word, to_word, ws):
        """

        Create a new word-ladder puzzle with the aim of stepping
        from from_word to to_word using words in ws, changing one
        character at each step.

        @type from_word: str
        @type to_word: str
        @type ws: set[str]
        @rtype: None
        
        """
        (self._from_word, self._to_word, self._word_set) = (from_word,
                                                            to_word, ws)
        # set of characters to use for 1-character changes
        self._chars = "abcdefghijklmnopqrstuvwxyz"
        

        
    def __eq__(self,other):
        '''
        Magic function to check if one Word Ladder Puzzle equals another.

        @type self: WordLadderPuzzle
        @type other: WordLadderPuzzle
        @rtype: True | False
        
        >>> word_set = ['apt', 'opt', 'oat', 'mat', 'man']
        >>> p1 = WordLadderPuzzle("ape", "man", word_set)
        >>> p2 = WordLadderPuzzle("ape", "man", word_set)
        >>> p1 == p2
        True
        
        '''
        if self._from_word == other._from_word:
            
            if self._to_word == other._to_word:
                
                if self._word_set == other._word_set:
                    return True
                
        return False
    def __str__(self):
        '''
        how all WordLadderPuzzle objects are meant to be represented.

        @type self: WordLadderPuzzle
        @rtype: str

        '''
        return "{} --> {}".format(self._from_word,self._to_word)

    def extensions(self):
        '''
        Gets all of the possible words that can be made from self._from_word by
        changing one letter at a time and checking if it is in the word set.
        If it is, then create a new WordLadderPuzzle and append it to the
        list of allowed moves.

        @type self: WordLadderPuzzle
        @rtype: list (could be an empty list)
        
        
        >>> puzzle = WordLadderPuzzle("ape","man",["apt","opt","oat","mat", "ace"])
        >>> puzzle.is_solved()
        False
        >>> c = puzzle.extensions()
        >>> for i in c: print(i)
        ace --> man
        apt --> man
        
        '''
        allowed = []

        for i in range(len(self._from_word)):

            for letter in self._chars:
                to_add = self._from_word.replace(self._from_word[i],letter)
                
                if to_add in self._word_set and not to_add is self._from_word:
                    allowed.append(WordLadderPuzzle(to_add,self._to_word,self._word_set))

        return allowed
                        

    def is_solved(self):
        '''
        is_solved will check to see if the from_word is the last word in the sequence,
        i.e. the puzzle has reached the end.
        
        @type self: WordLadderPuzzle
        @rtype: True | False

        >>> me = WordLadderPuzzle('ape','ape',['lst','of','wrds'])
        >>> me.is_solved()
        True
        
        '''
        
        return self._from_word == self._to_word


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
    from puzzle_tools import breadth_first_solve, depth_first_solve
    from time import time
    with open("words.txt", "r", encoding = 'latin-1') as words:
        word_set = words.read().split()
        word_set = set(word_set)
        word_set = set(word_set)
    w = WordLadderPuzzle("same", "cost", word_set)
    
    start = time()
    sol = breadth_first_solve(w)
    end = time()
    print("Solving word ladder from same->cost")
    print("...using breadth-first-search")
    print("Solutions: {} took {} seconds.".format(sol, end - start))
    
    start = time()
    sol = depth_first_solve(w)
    end = time()
    print("Solving word ladder from same->cost")
    print("...using depth-first-search")
    print("Solutions: {} took {} seconds.".format(sol, end - start))
