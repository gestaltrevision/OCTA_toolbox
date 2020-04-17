"""
Class for generating symmetrical patterns in 2D grid structures.
"""
from BasicPattern import BasicPattern

class SymmetryPattern(BasicPattern):
    def __init__(self, pattern, n_rows, n_cols):
        """
        Initializes a SymmetryPattern object.

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
    
    
    def MirrorElements(self):
        """
        Extends the current pattern by mirroring all the existing elements. This new pattern is then
        repeated until it fits in the 2D grid structure.

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
        required_count = self.n_rows * self.n_cols
        
        self.pattern = self.pattern + self.pattern[:-1][::-1]
        current_count = len(self.pattern)
        
        super().DuplicatePattern(1 + int(required_count/current_count), required_count)
        
        return self
    
        
    def MirrorAcrossRows(self):
        """
        Mirrors the pattern across the horizontal midline of the grid. If the pattern is shorter than
        half the total number of rows, the pattern is first duplicated.
        
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
        if len(self.pattern) < int(self.n_rows/2) + 1:
            self.DuplicatePattern(int(self.n_rows/2) + 1)
        
        if self.n_rows%2 == 0:
            m1 = self.pattern[:int(self.n_rows/2)]
            m2 = m1[::-1]
            self.pattern = m1 + m2
        else:
            m1 = self.pattern[:int((self.n_rows+1)/2)]
            m2 = m1[::-1]
            self.pattern = m1 + m2[1:]
            
        self.DuplicateElements(self.n_cols)
        
        return self
            
    
    def MirrorAcrossColumns(self):
        """
        Mirrors the pattern across the vertical midline of the grid. If the pattern is shorter than
        half the total number of rows, the pattern is first duplicated.
        
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
        if len(self.pattern) < int(self.n_cols/2) + 1:
            self.DuplicatePattern(int(self.n_cols/2) + 1)
            
        if self.n_cols%2 == 0:
            m1 = self.pattern[:int(self.n_cols/2)]
            m2 = m1[::-1]
            self.pattern = m1 + m2
        else:
            m1 = self.pattern[:int((self.n_cols+1)/2)]
            m2 = m1[::-1]
            self.pattern = m1 + m2[1:]
            
        self.DuplicatePattern(self.n_rows)
        
        return self
    
    
    def MirrorAcrossLeftDiagonal(self):
        """
        Mirrors the pattern across the diagonal running from the top left to 
        the bottom right. If the pattern is shorter than the number of elements required to
        reach the diagonal, the pattern is repeated.

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
        n = self.n_rows + self.n_cols
               
        max_elements = int(n/2)
        self.DuplicatePattern(int(n/len(self.pattern)), max_elements)
        
        
        if n%2 == 0:
            shifter = self.pattern + self.pattern[:-1][::-1]
        else:
            shifter = self.pattern + self.pattern[::-1]
          
        result = []
        for i in range(self.n_rows):
            result.extend(shifter[:self.n_cols][::-1])
            shifter = shifter[1:] + [shifter[0]]
        
        self.pattern = result
        
        return self
    
    def MirrorAcrossRightDiagonal(self):
        """
        Mirrors the pattern across the diagonal running from the top right to the bottom left.
        If the pattern is shorter than the number of elements required to reach the diagonal,
        the pattern is repeated.

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
        n = self.n_rows + self.n_cols
               
        max_elements = int(n/2)
        self.DuplicatePattern(int(n/len(self.pattern)), max_elements)
        
        
        if n%2 == 0:
            shifter = self.pattern + self.pattern[:-1][::-1]
        else:
            shifter = self.pattern + self.pattern[::-1]
            
        result = []
        for i in range(self.n_rows):
            result.extend(shifter[:self.n_cols])
            shifter = shifter[1:] + [shifter[0]]
        
        self.pattern = result
        
        return self
    
    def GenerateOnAxis(self, axis):
        """
        Generates a pattern along the axis specified with the axis argument.

        Parameters
        ----------
        axis : str
            'element'   : MirrorElements
            'row'       : MirrorAcrossColumns
            'col'       : MirrorAcrossRows
            'rightdiag' : MirrorAcrossRightDiagonal
            'leftdiag'  : MirrorAcrossLeftDiagonal
                
        Returns
        -------
        A list with values representing the pattern.

        """
        if axis == 'element':
            return self.MirrorElements().pattern
        elif axis == 'row':
            return self.MirrorAcrossColumns().pattern
        elif axis == 'col':
            return self.MirrorAcrossRows().pattern
        elif axis == 'rightdiag':
            return self.MirrorAcrossRightDiagonal().pattern
        elif axis == 'leftdiag':
            return self.MirrorAcrossLeftDiagonal().pattern
        
        

if __name__ == '__main__':
    n_rows = 4
    n_cols = 4
    base_pattern= [1, 2]
    
    symmetry_styles = ["MirrorElements", "MirrorAcrossRows", "MirrorAcrossColumns", "MirrorAcrossLeftDiagonal", "MirrorAcrossRightDiagonal"]
    
    # Construct mirror symmetry pattern
    for symmetry_style in symmetry_styles:
        pattern = SymmetryPattern(base_pattern, n_rows, n_cols)
        getattr(pattern, symmetry_style)()
        print("Using symmetry style %s"%symmetry_style)
        print(pattern)
        print("\n\n")
    
    