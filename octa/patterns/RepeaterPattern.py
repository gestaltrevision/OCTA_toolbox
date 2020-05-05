"""
A class for creating repeated patterns in a 2D grid structure.
"""
from .BasicPattern import BasicPattern

class GridRepeater(BasicPattern):
    def __init__(self, pattern, n_rows, n_cols):
        """
        Initializes a GridRepeater object.

        Parameters
        ----------
        pattern : list
            A list of values to be used in the repeater pattern.
        n_rows : int
            Number of rows in the 2D grid.
        n_cols : int
            Number of columns in the 2D grid.

        """
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
    
            
    def RepeatElements(self):
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
        required_count = self.n_rows * self.n_cols
        current_count = len(self.pattern)
        
        super().DuplicatePattern(1 + int(required_count/current_count), required_count)
        
        return self
        
    
    def RepeatAcrossRows(self):
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
        if len(self.pattern) < self.n_cols:
            self.DuplicatePattern( int(self.n_cols/len(self.pattern)) + 1, self.n_cols)
        self.pattern = self.pattern[:self.n_cols]
        
        super().DuplicatePattern(self.n_rows)
        
        return self
        
    
    def RepeatAcrossColumns(self):
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
        if len(self.pattern) < self.n_rows:
            self.DuplicatePattern( int(self.n_rows/len(self.pattern)) + 1, self.n_rows)
        self.pattern = self.pattern[:self.n_rows]
        
        super().DuplicateElements(self.n_cols)
        
        return self
        
    
    def RepeatAcrossRightDiagonal(self):
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
        self.DuplicatePattern( int( self.n_cols / len(self.pattern)) + 1 )
        shifted_pattern  = list(self.pattern)
        
        result = []
        for i in range(self.n_rows):
            result.extend(shifted_pattern[:self.n_cols])
            shifted_pattern = shifted_pattern[1:]  + [shifted_pattern[0]]
        
        self.pattern = result
        
        return self
            
    
    def RepeatAcrossLeftDiagonal(self):
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
        self.pattern  = list(self.pattern[::-1])
        self.DuplicatePattern( int( self.n_cols / len(self.pattern)) + 1 )
        shifted_pattern = list(self.pattern)
        
        result = []
        for i in range(self.n_rows):
            result.extend(shifted_pattern[-self.n_cols:])
            shifted_pattern = [shifted_pattern[-1]] + shifted_pattern[:-1]
        
        self.pattern = result
        
        return self
    
    def GenerateOnAxis(self, axis):
        """
        Generates a pattern along the axis specified with the axis argument.

        Parameters
        ----------
        axis : str
            'element'   : RepeatElements
            'row'       : RepeatAcrossColumns
            'col'       : RepeatAcrossRows
            'rightdiag' : RepeatAcrossRightDiagonal
            'leftdiag'  : RepeatAcrossLeftDiagonal
                
        Returns
        -------
        A list with values representing the pattern.

        """
        if axis == 'element':
            return self.RepeatElements().pattern
        elif axis == 'row':
            return self.RepeatAcrossColumns().pattern
        elif axis == 'col':
            return self.RepeatAcrossRows().pattern
        elif axis == 'rightdiag':
            return self.RepeatAcrossRightDiagonal().pattern
        elif axis == 'leftdiag':
            return self.RepeatAcrossLeftDiagonal().pattern
    
    
if __name__ == '__main__':
    # Grid pattern parameters
    n_rows = 4
    n_cols = 5
    base_pattern= [1, 2, 3]
    
    repeat_styles = ["RepeatElements", "RepeatAcrossRows", "RepeatAcrossColumns", "RepeatAcrossRightDiagonal", "RepeatAcrossLeftDiagonal"]

    # Repeat elements
    for repeat_style in repeat_styles:
        pattern = GridRepeater(base_pattern, n_rows, n_cols)
        getattr(pattern, repeat_style)()
        print("Using repeat style %s"%repeat_style)
        print(pattern)
        print("\n\n")
    
