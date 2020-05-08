"""
A class for creating repeated patterns in a 2D grid structure.
"""
from .BasicPattern import BasicPattern

class GridRepeater(BasicPattern):
    def __init__(self, pattern, n_rows, n_cols, style = "element"):
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
        element: str
            Style of the pattern. Can be found in octa.patterns.Style class

        """
        assert type(pattern) == list, "Provided pattern must be a list"
        assert type(n_rows)  == int, "n_rows must be an integer type"
        assert type(n_cols)  == int, "n_cols must be an integer type"
        
        super().__init__(pattern)
        
        self.n_rows = n_rows
        self.n_cols = n_cols
        
        self.style  = style
        self._Generate()
        
        
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
        
    
    def RepeatAcrossRows(self, n_repeats = 1):
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
        self.DuplicateElements(n_duplications = n_repeats)
        
        if len(self.pattern) < self.n_cols:
            self.DuplicatePattern( int(self.n_cols/len(self.pattern)) + 1, self.n_cols)
        self.pattern = self.pattern[:self.n_cols]
        
        super().DuplicatePattern(self.n_rows)
        
        return self
        
    
    def RepeatAcrossColumns(self, n_repeats = 1):
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
        self.DuplicateElements(n_duplications = n_repeats)
         
        if len(self.pattern) < self.n_rows:
            self.DuplicatePattern( int(self.n_rows/len(self.pattern)) + 1, self.n_rows)
        self.pattern = self.pattern[:self.n_rows]
        
        super().DuplicateElements(self.n_cols)
        
        return self
        
    
    def RepeatAcrossRightDiagonal(self, n_repeats = 1):
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
        self.DuplicateElements(n_duplications = n_repeats)
         
        self.DuplicatePattern( int( self.n_cols / len(self.pattern)) + 1 )
        shifted_pattern  = list(self.pattern)
        
        result = []
        for i in range(self.n_rows):
            result.extend(shifted_pattern[:self.n_cols])
            shifted_pattern = shifted_pattern[1:]  + [shifted_pattern[0]]
        
        self.pattern = result
        
        return self
            
    
    def RepeatAcrossLeftDiagonal(self, n_repeats = 1):
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
        self.DuplicateElements(n_duplications = n_repeats)
         
        self.pattern  = list(self.pattern[::-1])
        self.DuplicatePattern( int( self.n_cols / len(self.pattern)) + 1 )
        shifted_pattern = list(self.pattern)
        
        result = []
        for i in range(self.n_rows):
            result.extend(shifted_pattern[-self.n_cols:])
            shifted_pattern = [shifted_pattern[-1]] + shifted_pattern[:-1]
        
        self.pattern = result
        
        return self
    
    def RepeatAcrossOutIn(self):
        """
        Repeats the provided elements outwards to inwards.
        FOR NOW ONLY WHEN 2 OR 3 VALUES PROVIDED, 
        AND WHEN EQUAL NUMBER OF ROWS AND COLUMNS, 
        AND N_ROWS or N_COLS >= 4 with 2 values and >= 5 with 3 values

        Returns
        -------
        GridRepeater
            Current instance of the GridRepeater object.
            
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
        if self.n_cols != self.n_rows:
            print("OutIn pattern is only possible when the number of rows is equal to the number of columns, therefore the pattern cannot be created.")
        elif len(self.pattern) > 3 | len(self.pattern) < 2:
            print("OutIn pattern is only possible with 2 or provided values, therefore the pattern cannot be created.")
        elif len(self.pattern) == 2 & (self.n_cols < 4 | self.n_rows < 4):
            print("If there are 2 elements provided, the OutIn pattern is only possible with a row and column number of 4 or more, therefore the pattern cannot be created")
        elif len(self.pattern) == 3 & (self.n_cols < 5 | self.n_rows < 5):
            print("If there are 3 elements provided, the OutIn pattern is only possible with a row and column number of 5 or more, therefore the pattern cannot be created")
        else:             
            if self.n_cols % 2 == 0: # if even n_rows & n_cols:
                n_rings = int(self.n_cols / 2)
            
                self.DuplicatePatternToSize(count = n_rings)
                ring_elements = self.pattern
            
                ring_pattern = list(range(n_rings)) + list(range(n_rings))[::-1]
                
            else: # if odd n_rows & n_cols
                n_rings = int(self.n_cols / 2) + 1
                
                self.DuplicatePatternToSize(count = n_rings)
                ring_elements = self.pattern
                ring_pattern = list(range(n_rings)) + list(range(n_rings-1))[::-1]
                
            result = []         

            for i in ring_pattern:
                result.append(ring_elements[0:i] + [ring_elements[i]]* (self.n_cols-2*i) + ring_elements[0:i][::-1])
        
            result = [item for items in result for item in items] # flatten list
            
            self.pattern = result
        
            return self
    
    def RepeatElementsInSubgroups(self):
        """
        Repeats the provided elements in subgroups across rows and columns.
        ONLY POSSIBLE FOR NUMBER OF ROWS AND COLUMNS THAT CAN BE DIVIDED BY THE NUMBER OF PROVIDED ELEMENTS

        Returns
        -------
        GridRepeater
            Current instance of the GridRepeater object.
            
        Example
        -------
        pattern: 
            [1, 2, 3]
        n_rows:
            6
        n_cols:
            6
            
        result:
            [1, 1, 2, 2, 3, 3,
             1, 1, 2, 2, 3, 3,
             2, 2, 3, 3, 1, 1,
             2, 2, 3, 3, 1, 1,
             3, 3, 1, 1, 2, 2, 
             3, 3, 1, 1, 2, 2]
            

        """
        if self.n_rows % len(self.pattern) != 0:
            print("The number of rows can not be divided by the number of elements given in the pattern, therefore a subgroup pattern cannot be created.")
        elif self.n_cols % len(self.pattern) != 0:
            print("The number of columns can not be divided by the number of elements given in the pattern, therefore a subgroup pattern cannot be created.")
        else:
            n_elements = len(self.pattern)
            n_elementrepeats_row = int(self.n_rows / len(self.pattern))
            n_elementrepeats_col = int(self.n_cols / len(self.pattern))
        
            self.DuplicateElements(n_duplications = n_elementrepeats_col)
            self.DuplicatePattern(n_duplications = n_elementrepeats_row)
            group_pattern = self.pattern
        
            result = []
            for i in range(n_elements):
                result.extend(group_pattern[i*n_elementrepeats_col:] + group_pattern[:i*n_elementrepeats_col])
            
            self.pattern = result
        
            return self
        
    def RepeatPatternInCheckerboard(self):
        """
        Repeats the provided elements in a checkerboard across rows and columns.
        ONLY POSSIBLE FOR 2 or 3 PROVIDED ELEMENTS; and NUMBER OF ROWS AND COLUMNS THAT IS EVEN (could be changed later on)

        Returns
        -------
        GridRepeater
            Current instance of the GridRepeater object.
            
        Example
        -------
        pattern: 
            [1, 2, 3]
        n_rows:
            6
        n_cols:
            6
            
        result:
            [1, 2, 1, 2, 1, 2,
             3, 1, 3, 1, 3, 1, 
             1, 2, 1, 2, 1, 2,
             3, 1, 3, 1, 3, 1, 
             1, 2, 1, 2, 1, 2,
             3, 1, 3, 1, 3, 1]
            

        """
        if len(self.pattern) > 3 | len(self.pattern) < 2:
            print("Checkerboard patterns can only be made with 2 or 3 provided elements, therefore a checkerboard pattern cannot be created.")
        elif self.n_rows % 2 != 0:
            print("The number of rows is not even, therefore a checkerboard pattern cannot be created.")
        elif self.n_cols % 2 != 0:
            print("The number of columns is not even, therefore a checkerboard pattern cannot be created.")
        elif len(self.pattern) == 2:
            self.DuplicatePattern(n_duplications = int(self.n_cols / len(self.pattern)))
            group_pattern = self.pattern
            
            result = group_pattern
            result.extend(group_pattern[1:] + group_pattern[:1])
            
            self.pattern = result
            self.DuplicatePattern(n_duplications = int(self.n_rows / 2))
            
            return self
            
        elif len(self.pattern) == 3:
            pattern_1 = self.pattern[0:2] * int(self.n_cols / 2)
            pattern_2 = [self.pattern[2], self.pattern[0]] * int(self.n_cols / 2)
            
            self.pattern = pattern_1 + pattern_2
            self.DuplicatePattern(n_duplications = int(self.n_rows / 2))
            
            return self
    
    def _Generate(self):
        """
        Generates a pattern with the style specified in the style property

        Parameters
        ----------
        axis : str
            'element'    : RepeatElements
            'row'        : RepeatAcrossColumns
            'col'        : RepeatAcrossRows
            'right_diag' : RepeatAcrossRightDiagonal
            'left_diag'  : RepeatAcrossLeftDiagonal
                
        Returns
        -------
        A list with values representing the pattern.

        """
        if self.style == 'elements':
            self.RepeatElements()
        elif self.style == 'rows':
            self.RepeatAcrossColumns()
        elif self.style == 'columns':
            self.RepeatAcrossRows()
        elif self.style == 'right_diagonal':
            self.RepeatAcrossRightDiagonal()
        elif self.style == 'left_diagonal':
            self.RepeatAcrossLeftDiagonal()
    
    
if __name__ == '__main__':
    # Grid pattern parameters
    n_rows = 5
    n_cols = 5
    base_pattern= [1, 2, 3]
    
    repeat_styles = ["RepeatElements", "RepeatAcrossRows", "RepeatAcrossColumns", "RepeatAcrossRightDiagonal", "RepeatAcrossLeftDiagonal",
                     "RepeatElementsInSubgroups", "RepeatPatternInCheckerboard"]
    # Repeat elements
    for repeat_style in repeat_styles:
        pattern = GridRepeater(base_pattern, n_rows, n_cols)
        getattr(pattern, repeat_style)()
        print("Using repeat style %s"%repeat_style)
        print(pattern)
        print("\n\n")
    
