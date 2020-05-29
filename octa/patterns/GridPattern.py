# -*- coding: utf-8 -*-
"""
Module with various algorithms for creating patterns in a 2D grid

@author: Christophe
"""


from .Pattern import Pattern

class GridPattern(Pattern):
    """
        Base class for GridPatterns

        Parameters
        ----------
        pattern : list, Pattern
            Values to be used in the repeater pattern.
        n_rows : int
            Number of rows in the 2D grid.
        n_cols : int
            Number of columns in the 2D grid.

    """
    def __init__(self, pattern, n_rows = 5, n_cols = 5):

        assert type(pattern) == list or type(pattern) == Pattern, "Provided pattern must be a list"
        assert type(n_rows)  == int, "n_rows must be an integer type"
        assert type(n_cols)  == int, "n_cols must be an integer type"
        
        super().__init__(pattern)
        
        self.n_rows = n_rows
        self.n_cols = n_cols
                
        
    def __str__(self):
        """
        Creates a string representation of the 2D grid structure.

        Returns
        -------
        result : str
            String representation.

        """        
        result = ""
        for i in range(self.n_rows):
            result += ' '.join([str(x) for x in self.pattern[(i*self.n_cols) : (i+1)*self.n_cols]]) + "\n"
            
        return result
    
    
    def generate(self):
        """
        Abstract method. Needs to be implemented by specific grid pattern
        generation algorithms.

        Returns
        -------
        None.

        """
        pass
    
    def tile_elements(self, tile_multiplier):
        """
        Each element in the grid is expanded across rows and columns using the
        values in tile_multiplier

        Parameters
        ----------
        tile_multiplier : list, tuple or int
            Two values indicating the tiling along the rows and columns
            respectively. If a single integer is provided, the tiling will
            be the same along the rows and columns

        Returns
        -------
        None.

        """
        assert type(tile_multiplier) == int or type(tile_multiplier) == list or type(tile_multiplier) == tuple, "tile_multiplier needs to be int, list or tuple"
        if type(tile_multiplier) == int:
            tile_multiplier = (tile_multiplier, tile_multiplier)
        else:
            assert len(tile_multiplier) == 2, "tile_multiplier must contain two values"
            
            
        result = []
        
        for r in range(self.n_rows):
            current_row = []
            for c in range(self.n_cols):
                idx = r*(self.n_cols) + c
                current_row.extend([self.pattern[idx]] * tile_multiplier[1])
                
            current_row = current_row * tile_multiplier[0]
            result.extend(current_row)
            
        return GridPattern(result, self.n_rows * tile_multiplier[0], self.n_cols * tile_multiplier[1])
                
    
    
class RepeatElements(GridPattern):
    """
        Repeats the current pattern, until the total number of elements fits into the 2D grid structure.

        Returns
        -------
        GridRepeater
            Current instance of the GridRepeater object.
            
        Example
        -------
        pattern:
            [1, 2, 3]
        n_rows:
            4
        n_cols:
            3
        result:    
            [1, 2, 3, 1, 
             2, 3, 1, 2, 
             3, 1, 2, 3]

        """
        
    def generate(self):
        required_count = self.n_rows * self.n_cols
        current_count = len(self.pattern)
        
        result = self.RepeatPattern(1 + int(required_count/current_count), required_count)
        
        return RepeatElements(result.pattern, self.n_rows, self.n_cols)
    
    
class RepeatAcrossRows(GridPattern):
    """
        Repeats the provided pattern across the rows in the grid. The provided pattern is first
        either duplicated (when #elements < n_cols) or truncated (when #elements > n_cols) to fit
        in a single row.

        Returns
        -------
        GridRepeater
            Current instance of the GridRepeater object.
            
        Example
        -------
        pattern:
            [1, 2, 3]
        n_rows:
            3
        n_cols:
            4
        
        result:
            (First fit into number of columns)
            [1, 2, 3, 1]
            (Then replicate across rows)
            [1, 2, 3, 1,
             1, 2, 3, 1,
             1, 2, 3, 1]

    """    
    def generate(self):
        p = Pattern(self.pattern)
        
        if len(p.pattern) < self.n_cols:
            p = p.RepeatPattern( int(self.n_cols/len(self.pattern)) + 1, self.n_cols)
        p.pattern = p.pattern[:self.n_cols]
        
        p = p.RepeatPattern(self.n_rows)
        
        return RepeatAcrossRows(p, self.n_rows, self.n_cols)
        
    
class RepeatAcrossColumns(GridPattern):
    """
        Repeats the provided pattern across the columns in the grid. The provided pattern is first
        either duplicated (when #elements < n_rows) or truncated (when #elements > n_rows) to fit
        in a single column.

        Returns
        -------
        GridRepeater
            Current instance of the GridRepeater object.
            
        Example
        -------
        pattern: 
            [1, 2, 3]
        n_rows: 
            4
        n_cols:
            3
            
        result:
            (First fit into number of rows)
            [1, 2, 3, 1]
            (Then replicate across columns)
            [1, 1, 1, 1,
             2, 2, 2, 2,
             3, 3, 3, 3,
             1, 1, 1, 1]
        """   
    def generate(self):
        p = Pattern(self.pattern)
        N = len(p.pattern)
        
        if N < self.n_rows:
            p = p.RepeatPattern( int(self.n_rows / N) + 1, self.n_rows)
        p.pattern = p.pattern[:self.n_rows]
        
        p = p.RepeatElements(self.n_cols)
        
        return RepeatAcrossColumns(p, self.n_rows, self.n_cols)
    
    
class RepeatAcrossRightDiagonal(GridPattern):
    """
        Repeats the provided pattern across the diagonal running from the top left corner
        to the bottom right corner.

        Returns
        -------
        GridRepeater
            Current instance of the GridRepeater object.
            
        Example
        -------
        pattern:
            [1, 2, 3]
        n_rows:
            4
        n_cols:
            4
            
        result:
            [1, 2, 3, 1,
             2, 3, 1, 2,
             3, 1, 2, 3,
             1, 2, 3, 1]

        """    
    def generate(self):       
        p = Pattern(self.pattern)
        p = p.RepeatPattern( int( self.n_cols / len(self.pattern)) + 1 )
        shifted_pattern  = list(p.pattern)
        
        result = []
        for i in range(self.n_rows):
            result.extend(shifted_pattern[:self.n_cols])
            shifted_pattern = shifted_pattern[1:]  + [shifted_pattern[0]]
                
        return RepeatAcrossRightDiagonal(result, self.n_rows, self.n_cols)
            
    
class RepeatAcrossLeftDiagonal(GridPattern):
    """
        Repeats the provided pattern across the diagonal running from the top right corner
        to the bottom left corner.

        Returns
        -------
        GridRepeater
            Current instance of the GridRepeater object.
            
        Example
        -------
        pattern: 
            [1, 2, 3]
        n_rows:
            4
        n_cols:
            4
            
        result:
            [1, 3, 2, 1,
             2, 1, 3, 2,
             3, 2, 1, 3,
             1, 3, 2, 1]
            

        """ 
    def generate(self):  
        p = Pattern(self.pattern[::-1])
        p = p.RepeatPattern( int( self.n_cols / len(self.pattern)) + 1 )
        
        shifted_pattern = list(p.pattern)
        
        result = []
        for i in range(self.n_rows):
            result.extend(shifted_pattern[-self.n_cols:])
            shifted_pattern = [shifted_pattern[-1]] + shifted_pattern[:-1]
                
        return RepeatAcrossLeftDiagonal(result, self.n_rows, self.n_cols)    
    
    
class MirrorElements(GridPattern):
    """
        Extends the current pattern by mirroring all the existing elements. This new pattern is then
        repeated until the number of elements equals the number of elements in the corresponding grid,
        optionally truncating if the number of elements after a repetition exceeds the number of 
        elements in the grid.

        Returns
        -------
        SymmetryPattern.
            Current instance of the SymmetryPattern.
            
        Example
        -------
        pattern:
            [1, 2, 3]
        n_rows:
            4
        n_cols:
            4
            
        result:
            (after mirroring)
            [1, 2, 3, 2, 1]
            (after repeating to fit in the grid)
            [1, 2, 3, 2,
             1, 1, 2, 3,
             2, 1, 1, 2,
             3, 2, 1, 1]

        """
    def generate(self):
        
        required_count = self.n_rows * self.n_cols
        
        p = Pattern(self.pattern + self.pattern[:-1][::-1])
        current_count = len(p.pattern)
        
        p = p.RepeatPattern(1 + int(required_count/current_count), required_count)
        
        return MirrorElements(p, self.n_rows, self.n_cols)
    
    
class MirrorAcrossRows(GridPattern):
    """
        Mirrors the pattern across the horizontal midline of the grid. If the input
        pattern is not equal to half the number of rows (+1 if the number of rows is uneven),
        two manipulations can take place:
            1. If the provided pattern is shorter in length, the pattern as a whole is duplicated
               until it matches half the number of rows (+1 if uneven)
            2. If the provided pattern is longer, it is truncated to half the number of rows (+1)
        
        Returns
        -------
        SymmetryPattern.
            Current instance of the SymmetryPattern.
            
        Example
        -------
        pattern:
            [1, 2]
        n_rows:
            4
        n_cols:
            4
            
        result:
            [1, 1, 1, 1,
             2, 2, 2, 2,
             2, 2, 2, 2,
             1, 1, 1, 1]

    """
    def generate(self):
        p = Pattern(self.pattern)
        
        if len(p.pattern) < int(self.n_rows/2) + 1:
            p = p.RepeatPattern(int(self.n_rows/2) + 1)
        
        if self.n_rows%2 == 0:
            m1 = p.pattern[:int(self.n_rows/2)]
            m2 = m1[::-1]
            p.pattern = m1 + m2
        else:
            m1 = p.pattern[:int((self.n_rows+1)/2)]
            m2 = m1[::-1]
            p.pattern = m1 + m2[1:]
            
        p = p.RepeatElements(self.n_cols)
        
        return MirrorAcrossRows(p, self.n_rows, self.n_cols)
            
    
class MirrorAcrossColumns(GridPattern):
    """
        Mirrors the pattern across the horizontal midline of the grid. If the input
        pattern is not equal to half the number of columns (+1 if the number of columns is uneven),
        two manipulations can take place:
            1. If the provided pattern is shorter in length, the pattern as a whole is duplicated
               until it matches half the number of columns (+1 if uneven)
            2. If the provided pattern is longer, it is truncated to half the number of columns (+1)
        
        Returns
        -------
        SymmetryPattern.
            Current instance of the SymmetryPattern.
            
        Example
        -------
        pattern:
            [1, 2]
        n_rows:
            4
        n_cols:
            4
            
        result:
            [1, 2, 2, 1,
             1, 2, 2, 1,
             1, 2, 2, 1,
             1, 2, 2, 1]
    """
    def generate(self):
        p = Pattern(self.pattern)
        if len(p.pattern) < int(self.n_cols/2) + 1:
            p = p.RepeatPattern(int(self.n_cols/2) + 1)
            
        if self.n_cols%2 == 0:
            m1 = p.pattern[:int(self.n_cols/2)]
            m2 = m1[::-1]
            p.pattern = m1 + m2
        else:
            m1 = p.pattern[:int((self.n_cols+1)/2)]
            m2 = m1[::-1]
            p.pattern = m1 + m2[1:]
            
        p = p.RepeatPattern(self.n_rows)
        
        return MirrorAcrossColumns(p, self.n_rows, self.n_cols)
    
    
class MirrorAcrossLeftDiagonal(GridPattern):
    """
        Mirrors the pattern across the diagonal running from the top left to the bottom right. 
        If the pattern is shorter than the number of elements required to reach the diagonal,
        which is (n_rows + n_cols - 1) / 2, the pattern is repeated. If it is longer, the pattern
        is truncated.

        Returns
        -------
        SymmetryPattern.
            Current instance of the SymmetryPattern.
            
        Example
        -------
        pattern: 
            [1, 2, 3]
        n_rows:
            4
        n_cols: 
            5
            
        result:
            [1, 1, 3, 2, 1,
             3, 1, 1, 3, 2,
             2, 3, 1, 1, 3,
             1, 2, 3, 1, 1]
        """
    def generate(self):
        p = Pattern(self.pattern)
        n = self.n_rows + self.n_cols
               
        max_elements = int(n/2)
        p = p.RepeatPattern(int(n/len(p.pattern)), max_elements)
        
        
        if n%2 == 0:
            shifter = p.pattern + p.pattern[:-1][::-1]
        else:
            shifter = p.pattern + p.pattern[::-1]
          
        result = []
        for i in range(self.n_rows):
            result.extend(shifter[:self.n_cols][::-1])
            shifter = shifter[1:] + [shifter[0]]
                
        return MirrorAcrossLeftDiagonal(result, self.n_rows, self.n_cols)
    
    
class MirrorAcrossRightDiagonal(GridPattern):
    """
        Mirrors the pattern across the diagonal running from the top right to the bottom left.
        If the pattern is shorter than the number of elements required to reach the diagonal,
        which is (n_rows + n_cols - 1) / 2, the pattern is repeated. If it is longer, the pattern
        is truncated.

        Returns
        -------
        SymmetryPattern.
            Current instance of the SymmetryPattern.
            
        Example
        -------
        pattern: 
            [1, 2, 3]
        n_rows:
            4
        n_cols: 
            5
            
        result:
            [1, 2, 3, 1, 1,
             2, 3, 1, 1, 3,
             3, 1, 1, 3, 2,
             1, 1, 3, 2, 1]
    """
    def generate(self):
        p = Pattern(self.pattern)
        n = self.n_rows + self.n_cols
               
        max_elements = int(n/2)
        p = p.RepeatPattern(int(n/len(p.pattern)), max_elements)
        
        
        if n%2 == 0:
            shifter = p.pattern + p.pattern[:-1][::-1]
        else:
            shifter = p.pattern + p.pattern[::-1]
            
        result = []
        for i in range(self.n_rows):
            result.extend(shifter[:self.n_cols])
            shifter = shifter[1:] + [shifter[0]]
               
        return MirrorAcrossRightDiagonal(result, self.n_rows, self.n_cols)
    
class LayeredGrid(GridPattern):
    """
    Creates a grid that starts from a central structure, around which
    additional layers are placed.

    Parameters
    ----------
    center_grid : GridPattern
        A grid pattern that forms the central structure
        
    outer_layer : Pattern
        The values for each of the outer layers. Each value in the pattern
        becomes the next layer around the central grid structure
    Example
    -------
    pattern: 
        [1, 2, 3]
    n_rows:
        6
    n_cols:
        6
        
    result:
        [1, 1, 1, 1, 1, 1, 
         1, 2, 2, 2, 2, 1, 
         1, 2, 3, 3, 2, 1, 
         1, 2, 3, 3, 2, 1, 
         1, 2, 2, 2, 2, 1, 
         1, 1, 1, 1, 1, 1]
        

    """
    def __init__(self, center_grid, outer_layers):
        assert issubclass(type(center_grid), GridPattern), "center_grid has to be a GridPattern type"
        assert type(outer_layers) == Pattern, "outer_layers has to be a Pattern type"
        
        self.center_grid = center_grid
        self.outer_layers = outer_layers        
        
    def generate(self):
        # 1. Generate the center grid pattern
        current_center = self.center_grid.generate().pattern
        current_rows   = self.center_grid.n_rows
        current_cols   = self.center_grid.n_cols
        
        print(current_center)
        
        # 2. Recursively layer each layer ourind the center grid
        for value in self.outer_layers.pattern:
            # Calculate new dimensions
            new_rows = current_rows + 2
            new_cols = current_cols + 2
            
            # Fill the values in the new grid            
            new_center = []
            t = 0
            for r in range(new_rows):
                for c in range(new_cols):
                    if r == 0 or r == new_rows - 1:
                        new_center.append(value)
                    elif c == 0 or c == new_cols - 1:
                        new_center.append(value)
                    else:
                        new_center.append(current_center[t])
                        t += 1
                        
            # Update the current values
            current_center = new_center
            current_rows = new_rows
            current_cols = new_cols
            
        return GridPattern(current_center, current_rows, current_cols)
        
        