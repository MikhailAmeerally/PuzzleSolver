from puzzle import Puzzle


class MNPuzzle(Puzzle):
    """
    An nxm puzzle, like the 15-puzzle, which may be solved, unsolved,
    or even unsolvable.
    """

    def __init__(self, from_grid, to_grid):
        """
        MNPuzzle in state from_grid, working towards
        state to_grid

        @type self: this MNPuzzle
        @type from_grid: tuple[tuple[str]] current configuration
        @type to_grid: tuple[tuple[str]] solution configuration
        @rtype: None
        """
        # represent grid symbols with letters or numerals
        # represent the empty space with a "*"
        assert len(from_grid) > 0
        assert all([len(r) == len(from_grid[0]) for r in from_grid])
        assert all([len(r) == len(to_grid[0]) for r in to_grid])
        self.n, self.m = len(from_grid), len(from_grid[0])
        self.from_grid, self.to_grid = from_grid, to_grid


    def __str__(self):
        '''
        Returns a string representation of the MNPuzzle's current configuration
        @type self: MNPuzzle
        @rtype: str
        '''
        
        elements = ""
        for sub_grid in self.from_grid:
            
            for element in sub_grid:
                elements += "{}  ".format(element)
            elements += "\n"
            
        return elements
        
    def __eq__(self,other):
        '''
        @type self: MNPuzzle
        @type other: MNPuzzle
        @rtype: True | False
        '''
        
        if type(self) == type(other) == MNPuzzle:
            
            if self.from_grid == other.from_grid:
                
                if self.to_grid == other.to_grid:
                    return True
                
        return False

    def _new_puzzle(self,new_row,new_col):
        sub = ()
        ret = (sub)
        for i in range(self.n):
            for j in range(self.m):
                if i is new_row, and j is new_col:
                    sub += ("*")
                else:
                    sub += (self.from_grid[i][j])
        
                        
        
    def _moves(self,tup,sub_tup):
        legals = []
        row, colomn = self.n, self.m
        if (tup-1 >=0):
            pass # use _new_puzzle
        if (tup+1 < row):
            pass # use _new_puzzle
        
        
                            
    def extensions(self):
        pass
        
            
                

    
    def is_solved(self):
        '''
        @type self: MNPuzzle
        @rtype: True | False
        '''
        return self.from_grid == self.to_grid
    


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    target_grid = (("1", "2", "3"), ("4", "5", "*"))
    start_grid = (("*", "2", "3"), ("1", "4", "5"))
    print(MNPuzzle(start_grid,target_grid))
    '''
    from puzzle_tools import breadth_first_solve, depth_first_solve
    from time import time
    start = time()
    solution = breadth_first_solve(MNPuzzle(start_grid, target_grid))
    end = time()
    print("BFS solved: \n\n{} \n\nin {} seconds".format(
        solution, end - start))
    start = time()
    solution = depth_first_solve((MNPuzzle(start_grid, target_grid)))
    end = time()
    print("DFS solved: \n\n{} \n\nin {} seconds".format(
        solution, end - start))'''
