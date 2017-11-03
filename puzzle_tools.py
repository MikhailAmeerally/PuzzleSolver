"""
Some functions for working with puzzles
"""
from puzzle import Puzzle
from collections import deque
import sys
sys.setrecursionlimit(10**6)



            

def depth_first_solve(puzzle):
    """
    Return a path from PuzzleNode(puzzle) to a PuzzleNode containing
    a solution, with each child containing an extension of the puzzle
    in its parent.  Return None if this is not possible.

    @type puzzle: Puzzle
    @rtype: PuzzleNode | None
    
    """
    visited = set()
    visited.add(str(puzzle))
    
    def _visited(puzzle,visited):
        '''
        Checks to see if the puzzle configuration has been seen already.
        
        @type puzzle: WordLadderPuzzle | SudokuPuzzle | GridPegSolitairePuzzle | MNPuzzle
        @type visited: Set
        @rtype: True | False
        
        '''
        if str(puzzle) in visited:
            return True
        return False

    
    def _dfs(puzzle,visited):
        '''
        Function does exactly what dfs is supposed to do,
        but has the ability to check the visited nodes.
        DFS is essentially checking in an inorder traversal of
        an n-ary tree.
        
        @type puzzle: WordLadderPuzzle | SudokuPuzzle | GridPegSolitairePuzzle | MNPuzzle
        @type visited: Set
        @rtype: PuzzleNode | None
        
        '''
        if puzzle.is_solved():
            print(puzzle)
            return PuzzleNode(puzzle,None,None)
        if puzzle.fail_fast():
            return None
        else:
            children = puzzle.extensions()
            if len(children) > 0:
                
                for child in children:
                    
                    if not _visited(child,visited):
                        
                        visited.add(str(child))
                        return_val = _dfs(child,visited)
                        
                        if return_val:
                            return PuzzleNode(puzzle,return_val,None)
            
    
    sol = _dfs(puzzle,visited)
    return sol
    
    
        
def BFS_parent(PN):
    '''
    Helper function for breadth_first_solve
    gets the path back up to the parent, and creates what is, essentially,
    a complete tree node that has one child so that it is a path
    down to the solution from the parent

    @type PN: PuzzleNode
    @rtype: PuzzleNode
    
    '''
    if not PN.parent:
        return PN
    else:
        PN.parent.children = [PN]
        return BFS_parent(PN.parent)
    
def breadth_first_solve(puzzle):
    """
    Return a path from PuzzleNode(puzzle) to a PuzzleNode containing
    a solution, with each child PuzzleNode containing an extension
    of the puzzle in its parent.  Return None if this is not possible.

    @type puzzle: Puzzle
    @rtype: PuzzleNode
    
    """
    visited = []
    parent = None
    queue = deque([PuzzleNode(puzzle,None,parent)])

    
    while queue:
        PN = queue.pop()
        if PN not in visited:
            visited.append(PN)
            
            if PN.puzzle.is_solved():
                    return BFS_parent(PN)
            if PN.puzzle.fail_fast():
                return None
            else:
                children = PN.puzzle.extensions()
                
                if len(children) > 0:
                    parent = PN
                    for child in children:
                        PN_child = PuzzleNode(child,None,parent)
                        queue.appendleft(PN_child)
    return None
     
                        
                
            


class PuzzleNode:
    """
    A Puzzle configuration that refers to other configurations that it
    can be extended to.
    """

    def __init__(self, puzzle=None, children=None, parent=None):
        """
        Create a new puzzle node self with configuration puzzle.

        @type self: PuzzleNode
        @type puzzle: Puzzle | None
        @type children: list[PuzzleNode]
        @type parent: PuzzleNode | None
        @rtype: None
        """
        self.puzzle, self.parent = puzzle, parent
        if children is None:
            self.children = []
        else:
            self.children = [children]

    def __eq__(self, other):
        """
        Return whether Puzzle self is equivalent to other

        @type self: PuzzleNode
        @type other: PuzzleNode | Any
        @rtype: bool

        >>> from word_ladder_puzzle import WordLadderPuzzle
        >>> pn1 = PuzzleNode(WordLadderPuzzle("on", "no", {"on", "no", "oo"}))
        >>> pn2 = PuzzleNode(WordLadderPuzzle("on", "no", {"on", "oo", "no"}))
        >>> pn3 = PuzzleNode(WordLadderPuzzle("no", "on", {"on", "no", "oo"}))
        >>> pn1.__eq__(pn2)
        True
        >>> pn1.__eq__(pn3)
        False
        """
        return (type(self) == type(other) and
                self.puzzle == other.puzzle and
                all([x in self.children for x in other.children]) and
                all([x in other.children for x in self.children]))

    def __str__(self):
        """
        Return a human-readable string representing PuzzleNode self.

        # doctest not feasible.
        """
        return "{}\n\n{}".format(self.puzzle,
                                 "\n".join([str(x) for x in self.children]))

