"""
This module contains a class for creating gradient pattern in 2D grid structures.
"""
from .BasicPattern import BasicPattern

class GridGradient(BasicPattern):   
    def __init__(self, start_val, end_val, n_rows, n_cols, style = "elements"):
        """
        Initializes the parameters for a gradient pattern.

        Parameters
        ----------
        start_val : int, float or string
            Starting value for the gradient.
        end_val : int, float or string (must match start_val)
            End value for the gradient.
        n_rows : int
            Number of rows.
        n_cols : int
            Number of columns.

        Returns
        -------
        None.

        """
        assert type(start_val) in [int, float, str], "start_val must be an integer, float, or string type"
        assert type(end_val) in [int, float, str], "end_val must be an integer, float, or string type"
        assert type(start_val) == type(end_val), "start_val and end_val must be of the same type"
        assert type(n_rows) == int, "n_rows must be an integer type"
        assert type(n_cols) == int, "n_cols must be an integer type"
        
        self.start_val = start_val
        self.end_val   = end_val
        self.n_rows    = n_rows
        self.n_cols    = n_cols
        
        self.style = style
        self._Generate()
            
    def __str__(self):
        """
        Generates a string representation of the grid. Used for printing
        in the IPython console window.

        Returns
        -------
        result : str
            String representation of the 2D grid.

        """
        result = ""
        if type(self.start_val) == str:
            for i in range(self.n_rows):
                result += ' '.join([str(x) for x in self.pattern[(i*self.n_cols) : (i+1)*self.n_cols]]) + "\n"
        else:
            for i in range(self.n_rows):
                result += ' '.join(['%.2f'%x for x in self.pattern[(i*self.n_cols) : (i+1)*self.n_cols]]) + "\n"
            
        return result
    
    
    def GradientElements(self):
        """
        Creates a gradient where the number of elements equals the total number of elements in the grid.

        Returns
        -------
        GridGradient
            Current instance of the object.

        """
        n_elements = self.n_rows * self.n_cols
        self.pattern = self.__CreateGradientValues(n_elements)
        
        return self
        
        
    def GradientAcrossRows(self):
        """
        Creates a gradient across the rows of the grid.

        Returns
        -------
        GridGradient
            Current instance of the object.

        """
        self.pattern = self.__CreateGradientValues(self.n_rows)
        self.DuplicateElements(self.n_cols)
        
        return self
            
        
    def GradientAcrossColumns(self):      
        """
        Creates a gradient across the columns of the grid.

        Returns
        -------
        GridGradient
            Current instance of the object.

        """
        self.pattern = self.__CreateGradientValues(self.n_cols)
        self.DuplicatePattern(self.n_rows)
        
        return self
    
    def GradientAcrossLeftDiagonal(self):
        """
        Creates a diagonal gradient, starting in the top right corner and ending in the bottom left corner.

        Returns
        -------
        GridGradient
            Current instance of the object.

        """
        n_elements = self.n_rows + self.n_cols - 1
        shifter = self.__CreateGradientValues(n_elements)
          
        result = []
        for i in range(self.n_rows):
            result.extend(shifter[:self.n_cols][::-1])
            shifter = shifter[1:] + [shifter[0]]
        
        self.pattern = result
        
        return self
    
    def GradientAcrossRightDiagonal(self):
        """
        Creates a diagonal gradient, starting in the top left corner and ending in the bottom right corner.

        Returns
        -------
        GridGradient
            Current instance of the object.

        """
        n_elements = self.n_rows + self.n_cols - 1
        shifter = self.__CreateGradientValues(n_elements)
            
        result = []
        for i in range(self.n_rows):
            result.extend(shifter[:self.n_cols])
            shifter = shifter[1:] + [shifter[0]]
        
        self.pattern = result
        
        return self
        
