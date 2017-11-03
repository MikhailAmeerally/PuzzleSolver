from puzzle import Puzzle


class GridPegSolitairePuzzle(Puzzle):
    """
    Snapshot of peg solitaire on a rectangular grid. May be solved,
    unsolved, or even unsolvable.
    """

    def __init__(self, marker, marker_set):
        """
        Create a new GridPegSolitairePuzzle self with
        marker indicating pegs, spaces, and unused
        and marker_set indicating allowed markers.

        @type marker: list[list[str]]
        @type marker_set: set[str]
                          "#" for unused, "*" for peg, "." for empty
        """
        assert isinstance(marker, list)
        assert len(marker) > 0
        assert all([len(x) == len(marker[0]) for x in marker[1:]])
        assert all([all(x in marker_set for x in row) for row in marker])
        assert all([x == "*" or x == "." or x == "#" for x in marker_set])
        self._marker, self._marker_set = marker, marker_set

    def __eq__(self,other):
        '''
        @type self,other: GridPegSolitairePuzzle
        @rtype: True | False

        >>> grid = [["*", "*", "*", "*", "*"]]
        >>> GridPegSolitaire(grid, {"*",".","#"}) == GridPegSolitaire(grid, {"*",".","#"})
        True
        
        '''
        if self._marker == other._marker and self._marker_set == other._marker_set:
            return True
        return False
    def __str__(self):
        s=""
        for x in self._marker:
            
            for y in x:
                s = s + str(y) + " "
            s = s + "\n"
        return s


    def extensions(self):
        '''
        @type self: GridPegSolitairePuzzle
        @rtype: lst[GridPegSolitaire]
        '''
        grid = self._marker
        marker_set = self._marker_set
        def hardcopy(lst1):
            '''
            @type lst1: list
            @rtype: list copy of lst1
            '''
            lst2=[x[:] for x in lst1]
            return lst2

        moves = []
        temp = []
        for x in range(len(grid)-1):
            
            for y in range(len(grid[x])-1):
                
                if grid[x][y]==".":
                    
                    if x+2<=len(grid)-1:
                        
                        if grid[x+1][y] == "*" and grid[x+2][y] == "*":
                            temp=hardcopy(grid)
                            temp[x][y]="*"
                            temp[x+1][y]="."
                            temp[x+2][y]="."
                            moves.append(GridPegSolitairePuzzle(temp,marker_set))

                            
                    if x-2>=0:
                        
                        if grid[x-1][y] == "*" and grid[x-2][y] == "*":
                            temp=hardcopy(grid)
                            temp[x][y]="*"
                            temp[x-1][y]="."
                            temp[x-2][y]="."
                            moves.append(GridPegSolitairePuzzle(temp,marker_set))

                            
                    if y+2<=(len(grid[x])-1):
                        
                        if grid[x][y+1] == "*" and grid[x][y+2] == "*":
                            temp=hardcopy(grid)
                            temp[x][y]="*"
                            temp[x][y+1]="."
                            temp[x][y+2]="."
                            moves.append(GridPegSolitairePuzzle(temp,marker_set))

                            
                    if y-2>=0:
                        
                        if grid[x][y-1] == "*" and grid[x][y-2] == "*":
                            temp=hardcopy(grid)
                            temp[x][y]="*"
                            temp[x][y-1]="."
                            temp[x][y-2]="."
                            moves.append(GridPegSolitairePuzzle(temp,marker_set))

        return moves

        

    def is_solved(self):
        '''
        @type self: GridPegSolitaire
        @rtype: True | False
        
        >>> grid = [["*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*"], ["*", "*", ".", "*", "*"], ["*", "*", "*", "*", "*"]]
        >>> gpsp = GridPegSolitairePuzzle(grid, {"*", ".", "#"})
        >>> gpsp.is_solved()
        False
        
        '''
        peg_count = 0
        
        for sub in self._marker:
            
            for element in sub:
                
                if element is "*":
                    peg_count +=1
                    
        return peg_count == 1

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    from puzzle_tools import depth_first_solve, breadth_first_solve

    grid = [["*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*"],
            ["*", "*", ".", "*", "*"],
            ["*", "*", "*", "*", "*"]]
    gpsp = GridPegSolitairePuzzle(grid, {"*", ".", "#"})
    import time

    start = time.time()
    solution = depth_first_solve(gpsp)
    end = time.time()
    print("Solved 5x5 peg solitaire in {} seconds.".format(end - start))
    print("Using depth-first: \n{}".format(solution))
    children = gpsp.extensions()
