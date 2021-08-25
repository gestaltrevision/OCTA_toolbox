"""
GridPattern code for the OCTA toolbox
Module with various algorithms for creating patterns in a rectangular 2D grid

The Order & Complexity Toolbox for Aesthetics (OCTA) Python library is a tool for researchers 
to create stimuli varying in order and complexity on different dimensions. 
Copyright (C) 2021  Eline Van Geert, Christophe Bossens, and Johan Wagemans

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

Contact: eline.vangeert@kuleuven.be

"""

from .Pattern import Pattern
# import random

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
        patterntype : string
            Indicates the pattern type used.
        patterndirection : string
            Indicates the pattern direction used.

    """      
    def __init__(self, pattern, n_rows = 5, n_cols = 5, patterntype = None, patterndirection = None, patternclass = "GridPattern."):

        #print(type(pattern))
        assert type(pattern) == list or type(pattern) == Pattern, "Provided pattern must be a list"
        assert type(n_rows)  == int, "n_rows must be an integer type"
        assert type(n_cols)  == int, "n_cols must be an integer type"
        
        super().__init__(pattern)
        
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.patternclass = patternclass
        self.patterntype = patterntype
        self.patterndirection = patterndirection
        self._jitter = None
        self._jitter_parameters = {}
        self._randomization = None
                
        
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

        """
        pass
    
    def AddNormalJitter(self, mu = 0, std = 1, axis = None):
        """
        Adds a sample from a random normal distribution to each element in the generated GridPattern.

        Parameters
        ----------
        mu : float, optional
            Mean of the normal distribution. The default is 0.
        std : float, optional
            Standard deviation of the normal distribution. The default is 1.
        axis : string, optional
            String that contains the axis to which jitter should be applied.
            Possible values are "x", "y", "xy" or "x=y". The default is "xy".

        Returns
        -------
        Pattern:
            New GridPattern object instance

        """       
        self._jitter = 'normal'
        self._jitter_parameters = {'mu' : mu, 'std' : std, 'axis' : axis}
                                       
        return self
    
    def AddUniformJitter(self, min_val = -1, max_val = 1, axis = None):
        """
        Adds a sample from a uniform distribution to each element in the pattern.

        Parameters
        ----------
        min_val : float, optional
            Lower bound of the uniform distribution. The default is -1.
        max_val : float, optional
            Upper bound of the uniform distribution. The default is 1.
        axis : string, optional
            String that contains the axis to which jitter should be applied.
            Possible values are "x", "y", "xy" or "x=y". The default is "xy".

        Returns
        -------
        Pattern:
            New Pattern object instance

        """      
        self._jitter = 'uniform'
        self._jitter_parameters = {'min_val' : min_val, 'max_val' : max_val, 'axis' : axis}
                                       
        return self
    
    def RandomizeAcrossElements(self):
        """
        Randomizes the order of the elements in the pattern.

        """      
        self._randomization = 'RandomizeAcrossElements'
                                       
        return self
    
    def RandomizeAcrossRows(self):
        """
        Randomizes the order of the elements across rows in the pattern.

        """      
        self._randomization = 'RandomizeAcrossRows'
                                       
        return self
    
    def RandomizeAcrossColumns(self):
        """
        Randomizes the order of the elements across columns in the pattern.

        """      
        self._randomization = 'RandomizeAcrossColumns'
                                       
        return self
    
    def RandomizeAcrossLeftDiagonal(self):
        """
        Randomizes the order of the elements across the left diagonal in the pattern.

        """      
        self._randomization = 'RandomizeAcrossLeftDiagonal'
                                       
        return self  
    
    def RandomizeAcrossRightDiagonal(self):
        """
        Randomizes the order of the elements across the right diagonal in the pattern.

        """      
        self._randomization = 'RandomizeAcrossRightDiagonal'
                                       
        return self   
    
    # def RandomizeAcrossLayers(self):
    #     """
    #     Randomizes the order of the elements across the layers in the pattern.

    #     """      
    #     self._randomization = 'RandomizeAcrossLayers'
                                       
    #     return self
       
class ElementRepeatAcrossElements(GridPattern):
    """
        Repeats the values in the current pattern, until the total number of elements fits into the 2D grid structure.

        Returns
        -------
        GridPattern
            Current instance of the GridPattern object.
            
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
    _fixed_grid = False
    
    def generate(self):
        required_count = self.n_rows * self.n_cols

        result = self.RepeatElementsToSize(required_count)

        if self._jitter is not None:
            result = result._CalculateJitter(distribution = self._jitter, distribution_parameters = self._jitter_parameters)                 

        if self._randomization is not None:
            if self._randomization == "RandomizeAcrossElements":
                result = result._SetRandomizeAcrossElements()    
            elif self._randomization == "RandomizeAcrossRows":
                result = result._SetRandomizeAcrossRows(n_rows = self.n_rows, n_cols = self.n_cols)     
            elif self._randomization == "RandomizeAcrossColumns":
                result = result._SetRandomizeAcrossColumns(n_rows = self.n_rows, n_cols = self.n_cols)    
            elif self._randomization == "RandomizeAcrossLeftDiagonal":
                result = result._SetRandomizeAcrossLeftDiagonal(n_rows = self.n_rows, n_cols = self.n_cols)    
            elif self._randomization == "RandomizeAcrossRightDiagonal":
                result = result._SetRandomizeAcrossRightDiagonal(n_rows = self.n_rows, n_cols = self.n_cols)    
            elif self._randomization == "RandomizeAcrossLayers":
                result = result._SetRandomizeAcrossLayers(n_rows = self.n_rows, n_cols = self.n_cols)    

        
        self.patterntype = "ElementRepeat"
        self.patterndirection = "AcrossElements"
        
        return ElementRepeatAcrossElements(result.pattern, self.n_rows, self.n_cols, self.patterntype, self.patterndirection)
    
class ElementRepeatAcrossColumns(GridPattern):
    """
        Repeats the values in the provided pattern across the rows in the grid. The provided pattern is first
        either duplicated (when #elements < n_cols) or truncated (when #elements > n_cols) to fit
        in a single row.

        Returns
        -------
        GridPattern
            Current instance of the GridPattern object.
            
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
    _fixed_grid = False
    
    def generate(self):
        p = Pattern(self.pattern)
        
        required_count = self.n_cols

        p = p.RepeatElementsToSize(required_count) 
        
        result = p.RepeatPattern(self.n_rows)

        if self._jitter is not None:
            result = result._CalculateJitter(distribution = self._jitter, distribution_parameters = self._jitter_parameters)                 

        if self._randomization is not None:
            if self._randomization == "RandomizeAcrossElements":
                result = result._SetRandomizeAcrossElements()   
            elif self._randomization == "RandomizeAcrossRows":
                result = result._SetRandomizeAcrossRows(n_rows = self.n_rows, n_cols = self.n_cols)       
            elif self._randomization == "RandomizeAcrossColumns":
                result = result._SetRandomizeAcrossColumns(n_rows = self.n_rows, n_cols = self.n_cols)     
            elif self._randomization == "RandomizeAcrossLeftDiagonal":
                result = result._SetRandomizeAcrossLeftDiagonal(n_rows = self.n_rows, n_cols = self.n_cols)    
            elif self._randomization == "RandomizeAcrossRightDiagonal":
                result = result._SetRandomizeAcrossRightDiagonal(n_rows = self.n_rows, n_cols = self.n_cols)    
            elif self._randomization == "RandomizeAcrossLayers":
                result = result._SetRandomizeAcrossLayers(n_rows = self.n_rows, n_cols = self.n_cols)      
            
        self.patterntype = "ElementRepeat"
        self.patterndirection = "AcrossColumns"

        return ElementRepeatAcrossColumns(result.pattern, self.n_rows, self.n_cols, self.patterntype, self.patterndirection)

class ElementRepeatAcrossRows(GridPattern):
    """
        Repeats the values in the provided pattern across the columns in the grid. The provided pattern is first
        either duplicated (when #elements < n_rows) or truncated (when #elements > n_rows) to fit
        in a single column.

        Returns
        -------
        GridPattern
            Current instance of the GridPattern object.
            
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
    _fixed_grid = False
    
    def generate(self):

        p = Pattern(self.pattern)
        
        required_count = self.n_rows

        p = p.RepeatElementsToSize(required_count) 
        
        result = p.RepeatElements(self.n_cols)

        if self._jitter is not None:
            result = result._CalculateJitter(distribution = self._jitter, distribution_parameters = self._jitter_parameters)                 

        if self._randomization is not None:
            if self._randomization == "RandomizeAcrossElements":
                result = result._SetRandomizeAcrossElements()   
            elif self._randomization == "RandomizeAcrossRows":
                result = result._SetRandomizeAcrossRows(n_rows = self.n_rows, n_cols = self.n_cols)     
            elif self._randomization == "RandomizeAcrossColumns":
                result = result._SetRandomizeAcrossColumns(n_rows = self.n_rows, n_cols = self.n_cols)     
            elif self._randomization == "RandomizeAcrossLeftDiagonal":
                result = result._SetRandomizeAcrossLeftDiagonal(n_rows = self.n_rows, n_cols = self.n_cols)    
            elif self._randomization == "RandomizeAcrossRightDiagonal":
                result = result._SetRandomizeAcrossRightDiagonal(n_rows = self.n_rows, n_cols = self.n_cols)    
            elif self._randomization == "RandomizeAcrossLayers":
                result = result._SetRandomizeAcrossLayers(n_rows = self.n_rows, n_cols = self.n_cols)        
         
        self.patterntype = "ElementRepeat"
        self.patterndirection = "AcrossRows"

        return ElementRepeatAcrossRows(result.pattern, self.n_rows, self.n_cols, self.patterntype, self.patterndirection)
        
class ElementRepeatAcrossRightDiagonal(GridPattern):
    """
        Repeats the values in the provided pattern across the diagonal running from the top left corner
        to the bottom right corner.

        Returns
        -------
        GridPattern
            Current instance of the GridPattern object.
            
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
    _fixed_grid = False
    
    def generate(self):       
        
        p = Pattern(self.pattern)
        
        required_count = (self.n_rows + self.n_cols) - 1

        p = p.RepeatElementsToSize(required_count) 
        
        shifted_pattern  = list(p.pattern)
        
        result = []
        for i in range(self.n_rows):
            result.extend(shifted_pattern[:self.n_cols])
            shifted_pattern = shifted_pattern[1:]  + [shifted_pattern[0]]
            
        result = Pattern(result)

        if self._jitter is not None:
            result = result._CalculateJitter(distribution = self._jitter, distribution_parameters = self._jitter_parameters)                 

        if self._randomization is not None:
            if self._randomization == "RandomizeAcrossElements":
                result = result._SetRandomizeAcrossElements()   
            elif self._randomization == "RandomizeAcrossRows":
                result = result._SetRandomizeAcrossRows(n_rows = self.n_rows, n_cols = self.n_cols)      
            elif self._randomization == "RandomizeAcrossColumns":
                result = result._SetRandomizeAcrossColumns(n_rows = self.n_rows, n_cols = self.n_cols)     
            elif self._randomization == "RandomizeAcrossLeftDiagonal":
                result = result._SetRandomizeAcrossLeftDiagonal(n_rows = self.n_rows, n_cols = self.n_cols)    
            elif self._randomization == "RandomizeAcrossRightDiagonal":
                result = result._SetRandomizeAcrossRightDiagonal(n_rows = self.n_rows, n_cols = self.n_cols)    
            elif self._randomization == "RandomizeAcrossLayers":
                result = result._SetRandomizeAcrossLayers(n_rows = self.n_rows, n_cols = self.n_cols)       
                 
        self.patterntype = "ElementRepeat"
        self.patterndirection = "AcrossRightDiagonal"

        return ElementRepeatAcrossRightDiagonal(result.pattern, self.n_rows, self.n_cols, self.patterntype, self.patterndirection)
            
    
class ElementRepeatAcrossLeftDiagonal(GridPattern):
    """
        Repeats the values in the provided pattern across the diagonal running from the top right corner
        to the bottom left corner.

        Returns
        -------
        GridPattern
            Current instance of the GridPattern object.
            
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
    _fixed_grid = False
    def generate(self):  
        
        p = Pattern(self.pattern)
        
        required_count = (self.n_rows + self.n_cols) - 1

        p = p.RepeatElementsToSize(required_count)
        
        shifted_pattern  = list(p.pattern[::-1])
        
        result = []
        for i in range(self.n_rows):
            result.extend(shifted_pattern[-self.n_cols:])
            shifted_pattern = [shifted_pattern[-1]] + shifted_pattern[:-1]
            
        result = Pattern(result)
        
        if self._jitter is not None:
            result = result._CalculateJitter(distribution = self._jitter, distribution_parameters = self._jitter_parameters)                 

        if self._randomization is not None:
            if self._randomization == "RandomizeAcrossElements":
                result = result._SetRandomizeAcrossElements()   
            elif self._randomization == "RandomizeAcrossRows":
                result = result._SetRandomizeAcrossRows(n_rows = self.n_rows, n_cols = self.n_cols)      
            elif self._randomization == "RandomizeAcrossColumns":
                result = result._SetRandomizeAcrossColumns(n_rows = self.n_rows, n_cols = self.n_cols)      
            elif self._randomization == "RandomizeAcrossLeftDiagonal":
                result = result._SetRandomizeAcrossLeftDiagonal(n_rows = self.n_rows, n_cols = self.n_cols)    
            elif self._randomization == "RandomizeAcrossRightDiagonal":
                result = result._SetRandomizeAcrossRightDiagonal(n_rows = self.n_rows, n_cols = self.n_cols)    
            elif self._randomization == "RandomizeAcrossLayers":
                result = result._SetRandomizeAcrossLayers(n_rows = self.n_rows, n_cols = self.n_cols)      
                 
        self.patterntype = "ElementRepeat"
        self.patterndirection = "AcrossLeftDiagonal"

        return ElementRepeatAcrossLeftDiagonal(result.pattern, self.n_rows, self.n_cols, self.patterntype, self.patterndirection)    
  
class ElementRepeatAcrossLayers(GridPattern):
    """
        Repeats the values in the provided pattern across the layers within the stimulus running from inside to outside layers.

        Returns
        -------
        GridPattern
            Current instance of the GridPattern object.
            
        Example
        -------
        pattern: 
            [1, 2, 3]
        n_rows:
            6
        n_cols:
            6
            
        result:
            [3, 3, 3, 3, 3, 3, 
             3, 2, 2, 2, 2, 3,
             3, 2, 1, 1, 2, 3, 
             3, 2, 1, 1, 2, 3, 
             3, 2, 2, 2, 2, 3, 
             3, 3, 3, 3, 3, 3]
            

    """ 
    _fixed_grid = False
    def generate(self):  
        assert (self.n_rows > 2), "number of rows in the Grid should be more than 2 to apply this pattern"
        assert (self.n_cols > 2), "number of columns in the Grid should be more than 2 to apply this pattern"
        
        p = Pattern(self.pattern)
        
        n_rows = self.n_rows
        n_cols = self.n_cols
        
        minimal_n = min(n_rows, n_cols)
        if minimal_n % 2 == 0: 
            n_layers = int(minimal_n / 2)
        else:
            n_layers = int((minimal_n + 1 )/2)
        
        p = p.RepeatElementsToSize(n_layers)
        # if len(p.pattern) < n_layers:
        #     p = p.RepeatPattern( int(n_layers/len(self.pattern)) + 1, n_layers)
        p.pattern = p.pattern[:n_layers][::-1]
        
        patternmatrix = [[0 for x in range(n_cols)] for y in range(n_rows)] 
        
        for layer in range(n_layers):
            width = n_cols - (2*layer)
            start_row = layer
            start_col = layer
            end_row = n_rows - layer - 1
            end_col = n_cols - layer
            patternmatrix[start_row][start_col:end_col] = [p.pattern[layer]] * (width)
            patternmatrix[end_row][start_col:end_col] = [p.pattern[layer]] * (width)
            for row in patternmatrix[start_row:end_row]:
                row[start_col] = p.pattern[layer] 
                row[end_col-1] = p.pattern[layer] 
       
        result = Pattern([item for sublist in patternmatrix for item in sublist])

        if self._jitter is not None:
            result = result._CalculateJitter(distribution = self._jitter, distribution_parameters = self._jitter_parameters)                 

        if self._randomization is not None:
            if self._randomization == "RandomizeAcrossElements":
                result = result._SetRandomizeAcrossElements()   
            elif self._randomization == "RandomizeAcrossRows":
                result = result._SetRandomizeAcrossRows(n_rows = self.n_rows, n_cols = self.n_cols)       
            elif self._randomization == "RandomizeAcrossColumns":
                result = result._SetRandomizeAcrossColumns(n_rows = self.n_rows, n_cols = self.n_cols)       
            elif self._randomization == "RandomizeAcrossLeftDiagonal":
                result = result._SetRandomizeAcrossLeftDiagonal(n_rows = self.n_rows, n_cols = self.n_cols)    
            elif self._randomization == "RandomizeAcrossRightDiagonal":
                result = result._SetRandomizeAcrossRightDiagonal(n_rows = self.n_rows, n_cols = self.n_cols)    
            elif self._randomization == "RandomizeAcrossLayers":
                result = result._SetRandomizeAcrossLayers(n_rows = self.n_rows, n_cols = self.n_cols)    
                             
        self.patterntype = "ElementRepeat"
        self.patterndirection = "AcrossLayers"

        return ElementRepeatAcrossLayers(result.pattern, self.n_rows, self.n_cols, self.patterntype, self.patterndirection) 
    
   
class RepeatAcrossElements(GridPattern):
    """
        Repeats the current pattern, until the total number of elements fits into the 2D grid structure.

        Returns
        -------
        GridPattern
            Current instance of the GridPattern object.
            
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
    _fixed_grid = False
    
    def generate(self):
        required_count = self.n_rows * self.n_cols
        current_count = len(self.pattern)
        
        result = self.RepeatPattern(1 + int(required_count/current_count), required_count)

        if self._jitter is not None:
            result = result._CalculateJitter(distribution = self._jitter, distribution_parameters = self._jitter_parameters)                 

        if self._randomization is not None:
            if self._randomization == "RandomizeAcrossElements":
                result = result._SetRandomizeAcrossElements()   
            elif self._randomization == "RandomizeAcrossRows":
                result = result._SetRandomizeAcrossRows(n_rows = self.n_rows, n_cols = self.n_cols)      
            elif self._randomization == "RandomizeAcrossColumns":
                result = result._SetRandomizeAcrossColumns(n_rows = self.n_rows, n_cols = self.n_cols)      
            elif self._randomization == "RandomizeAcrossLeftDiagonal":
                result = result._SetRandomizeAcrossLeftDiagonal(n_rows = self.n_rows, n_cols = self.n_cols)    
            elif self._randomization == "RandomizeAcrossRightDiagonal":
                result = result._SetRandomizeAcrossRightDiagonal(n_rows = self.n_rows, n_cols = self.n_cols)    
            elif self._randomization == "RandomizeAcrossLayers":
                result = result._SetRandomizeAcrossLayers(n_rows = self.n_rows, n_cols = self.n_cols)       
         
        self.patterntype = "Repeat"
        self.patterndirection = "AcrossElements"
        
        return RepeatAcrossElements(result.pattern, self.n_rows, self.n_cols, self.patterntype, self.patterndirection)
    
    
class RepeatAcrossColumns(GridPattern):
    """
        Repeats the provided pattern across the rows in the grid. The provided pattern is first
        either duplicated (when #elements < n_cols) or truncated (when #elements > n_cols) to fit
        in a single row.

        Returns
        -------
        GridPattern
            Current instance of the GridPattern object.
            
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
    _fixed_grid = False
    
    def generate(self):
        p = Pattern(self.pattern)
        
        if len(p.pattern) < self.n_cols:
            p = p.RepeatPattern( int(self.n_cols/len(self.pattern)) + 1, self.n_cols)
        p.pattern = p.pattern[:self.n_cols]
        
        result = p.RepeatPattern(self.n_rows)

        if self._jitter is not None:
            result = result._CalculateJitter(distribution = self._jitter, distribution_parameters = self._jitter_parameters)                 

        if self._randomization is not None:
            if self._randomization == "RandomizeAcrossElements":
                result = result._SetRandomizeAcrossElements()   
            elif self._randomization == "RandomizeAcrossRows":
                result = result._SetRandomizeAcrossRows(n_rows = self.n_rows, n_cols = self.n_cols)      
            elif self._randomization == "RandomizeAcrossColumns":
                result = result._SetRandomizeAcrossColumns(n_rows = self.n_rows, n_cols = self.n_cols)     
            elif self._randomization == "RandomizeAcrossLeftDiagonal":
                result = result._SetRandomizeAcrossLeftDiagonal(n_rows = self.n_rows, n_cols = self.n_cols)    
            elif self._randomization == "RandomizeAcrossRightDiagonal":
                result = result._SetRandomizeAcrossRightDiagonal(n_rows = self.n_rows, n_cols = self.n_cols)    
            elif self._randomization == "RandomizeAcrossLayers":
                result = result._SetRandomizeAcrossLayers(n_rows = self.n_rows, n_cols = self.n_cols)       
         
        self.patterntype = "Repeat"
        self.patterndirection = "AcrossColumns"

        return RepeatAcrossColumns(result.pattern, self.n_rows, self.n_cols, self.patterntype, self.patterndirection)
        
    
class RepeatAcrossRows(GridPattern):
    """
        Repeats the provided pattern across the columns in the grid. The provided pattern is first
        either duplicated (when #elements < n_rows) or truncated (when #elements > n_rows) to fit
        in a single column.

        Returns
        -------
        GridPattern
            Current instance of the GridPattern object.
            
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
    _fixed_grid = False
    
    def generate(self):
        p = Pattern(self.pattern)
        N = len(p.pattern)
        
        if N < self.n_rows:
            p = p.RepeatPattern( int(self.n_rows / N) + 1, self.n_rows)
        p.pattern = p.pattern[:self.n_rows]
        
        result = p.RepeatElements(self.n_cols)

        if self._jitter is not None:
            result = result._CalculateJitter(distribution = self._jitter, distribution_parameters = self._jitter_parameters)                 

        if self._randomization is not None:
            if self._randomization == "RandomizeAcrossElements":
                result = result._SetRandomizeAcrossElements()   
            elif self._randomization == "RandomizeAcrossRows":
                result = result._SetRandomizeAcrossRows(n_rows = self.n_rows, n_cols = self.n_cols)      
            elif self._randomization == "RandomizeAcrossColumns":
                result = result._SetRandomizeAcrossColumns(n_rows = self.n_rows, n_cols = self.n_cols)      
            elif self._randomization == "RandomizeAcrossLeftDiagonal":
                result = result._SetRandomizeAcrossLeftDiagonal(n_rows = self.n_rows, n_cols = self.n_cols)    
            elif self._randomization == "RandomizeAcrossRightDiagonal":
                result = result._SetRandomizeAcrossRightDiagonal(n_rows = self.n_rows, n_cols = self.n_cols)    
            elif self._randomization == "RandomizeAcrossLayers":
                result = result._SetRandomizeAcrossLayers(n_rows = self.n_rows, n_cols = self.n_cols)       
               
        self.patterntype = "Repeat"
        self.patterndirection = "AcrossRows"

        return RepeatAcrossRows(result.pattern, self.n_rows, self.n_cols, self.patterntype, self.patterndirection)
    
class RepeatAcrossRightDiagonal(GridPattern):
    """
        Repeats the provided pattern across the diagonal running from the top left corner
        to the bottom right corner.

        Returns
        -------
        GridPattern
            Current instance of the GridPattern object.
            
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
    _fixed_grid = False
    
    def generate(self):       
        p = Pattern(self.pattern)
        p = p.RepeatPattern( int( self.n_cols / len(self.pattern)) + 1 )
        shifted_pattern  = list(p.pattern)
        
        result = []
        for i in range(self.n_rows):
            result.extend(shifted_pattern[:self.n_cols])
            shifted_pattern = shifted_pattern[1:]  + [shifted_pattern[0]]
                    
        result = Pattern(result)

        if self._jitter is not None:
            result = result._CalculateJitter(distribution = self._jitter, distribution_parameters = self._jitter_parameters)                 

        if self._randomization is not None:
            if self._randomization == "RandomizeAcrossElements":
                result = result._SetRandomizeAcrossElements()   
            elif self._randomization == "RandomizeAcrossRows":
                result = result._SetRandomizeAcrossRows(n_rows = self.n_rows, n_cols = self.n_cols)      
            elif self._randomization == "RandomizeAcrossColumns":
                result = result._SetRandomizeAcrossColumns(n_rows = self.n_rows, n_cols = self.n_cols)      
            elif self._randomization == "RandomizeAcrossLeftDiagonal":
                result = result._SetRandomizeAcrossLeftDiagonal(n_rows = self.n_rows, n_cols = self.n_cols)    
            elif self._randomization == "RandomizeAcrossRightDiagonal":
                result = result._SetRandomizeAcrossRightDiagonal(n_rows = self.n_rows, n_cols = self.n_cols)    
            elif self._randomization == "RandomizeAcrossLayers":
                result = result._SetRandomizeAcrossLayers(n_rows = self.n_rows, n_cols = self.n_cols)      
                 
        self.patterntype = "Repeat"
        self.patterndirection = "AcrossRightDiagonal"

        return RepeatAcrossRightDiagonal(result.pattern, self.n_rows, self.n_cols, self.patterntype, self.patterndirection)
            
    
class RepeatAcrossLeftDiagonal(GridPattern):
    """
        Repeats the provided pattern across the diagonal running from the top right corner
        to the bottom left corner.

        Returns
        -------
        GridPattern
            Current instance of the GridPattern object.
            
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
    _fixed_grid = False
    def generate(self):  
        p = Pattern(self.pattern[::-1])
        p = p.RepeatPattern( int( self.n_cols / len(self.pattern)) + 1 )
        
        shifted_pattern = list(p.pattern)
        
        result = []
        for i in range(self.n_rows):
            result.extend(shifted_pattern[-self.n_cols:])
            shifted_pattern = [shifted_pattern[-1]] + shifted_pattern[:-1]
                    
        result = Pattern(result)

        if self._jitter is not None:
            result = result._CalculateJitter(distribution = self._jitter, distribution_parameters = self._jitter_parameters)                 

        if self._randomization is not None:
            if self._randomization == "RandomizeAcrossElements":
                result = result._SetRandomizeAcrossElements()   
            elif self._randomization == "RandomizeAcrossRows":
                result = result._SetRandomizeAcrossRows(n_rows = self.n_rows, n_cols = self.n_cols)       
            elif self._randomization == "RandomizeAcrossColumns":
                result = result._SetRandomizeAcrossColumns(n_rows = self.n_rows, n_cols = self.n_cols)       
            elif self._randomization == "RandomizeAcrossLeftDiagonal":
                result = result._SetRandomizeAcrossLeftDiagonal(n_rows = self.n_rows, n_cols = self.n_cols)    
            elif self._randomization == "RandomizeAcrossRightDiagonal":
                result = result._SetRandomizeAcrossRightDiagonal(n_rows = self.n_rows, n_cols = self.n_cols)    
            elif self._randomization == "RandomizeAcrossLayers":
                result = result._SetRandomizeAcrossLayers(n_rows = self.n_rows, n_cols = self.n_cols)    
                 
        self.patterntype = "Repeat"
        self.patterndirection = "AcrossLeftDiagonal"

        return RepeatAcrossLeftDiagonal(result.pattern, self.n_rows, self.n_cols, self.patterntype, self.patterndirection)    
  
class RepeatAcrossLayers(GridPattern):
    """
        Repeats the provided pattern across the layers within the stimulus running from inside to outside layers.

        Returns
        -------
        GridPattern
            Current instance of the GridPattern object.
            
        Example
        -------
        pattern: 
            [1, 2, 3]
        n_rows:
            6
        n_cols:
            6
            
        result:
            [3, 3, 3, 3, 3, 3, 
             3, 2, 2, 2, 2, 3,
             3, 2, 1, 1, 2, 3, 
             3, 2, 1, 1, 2, 3, 
             3, 2, 2, 2, 2, 3, 
             3, 3, 3, 3, 3, 3]
            

    """ 
    _fixed_grid = False
    def generate(self):  
        assert (self.n_rows > 2), "number of rows in the Grid should be more than 2 to apply this pattern"
        assert (self.n_cols > 2), "number of columns in the Grid should be more than 2 to apply this pattern"
        
        p = Pattern(self.pattern)
        
        n_rows = self.n_rows
        n_cols = self.n_cols
        
        minimal_n = min(n_rows, n_cols)
        if minimal_n % 2 == 0: 
            n_layers = int(minimal_n / 2)
        else:
            n_layers = int((minimal_n + 1 )/2)
        
        if len(p.pattern) < n_layers:
            p = p.RepeatPattern( int(n_layers/len(self.pattern)) + 1, n_layers)
        p.pattern = p.pattern[:n_layers][::-1]
        
        patternmatrix = [[0 for x in range(n_cols)] for y in range(n_rows)] 
        
        for layer in range(n_layers):
            width = n_cols - (2*layer)
            start_row = layer
            start_col = layer
            end_row = n_rows - layer - 1
            end_col = n_cols - layer
            patternmatrix[start_row][start_col:end_col] = [p.pattern[layer]] * (width)
            patternmatrix[end_row][start_col:end_col] = [p.pattern[layer]] * (width)
            for row in patternmatrix[start_row:end_row]:
                row[start_col] = p.pattern[layer] 
                row[end_col-1] = p.pattern[layer] 
       
        result = Pattern([item for sublist in patternmatrix for item in sublist])
 
        if self._jitter is not None:
            result = result._CalculateJitter(distribution = self._jitter, distribution_parameters = self._jitter_parameters)                 

        if self._randomization is not None:
            if self._randomization == "RandomizeAcrossElements":
                result = result._SetRandomizeAcrossElements()   
            elif self._randomization == "RandomizeAcrossRows":
                result = result._SetRandomizeAcrossRows(n_rows = self.n_rows, n_cols = self.n_cols)       
            elif self._randomization == "RandomizeAcrossColumns":
                result = result._SetRandomizeAcrossColumns(n_rows = self.n_rows, n_cols = self.n_cols)       
            elif self._randomization == "RandomizeAcrossLeftDiagonal":
                result = result._SetRandomizeAcrossLeftDiagonal(n_rows = self.n_rows, n_cols = self.n_cols)    
            elif self._randomization == "RandomizeAcrossRightDiagonal":
                result = result._SetRandomizeAcrossRightDiagonal(n_rows = self.n_rows, n_cols = self.n_cols)    
            elif self._randomization == "RandomizeAcrossLayers":
                result = result._SetRandomizeAcrossLayers(n_rows = self.n_rows, n_cols = self.n_cols)    
                            
        self.patterntype = "Repeat"
        self.patterndirection = "AcrossLayers"

        return RepeatAcrossLayers(result.pattern, self.n_rows, self.n_cols, self.patterntype, self.patterndirection) 
    

class MirrorAcrossElements(GridPattern):
    """
        Repeats the input pattern until there are as many elements as half the 
        number of elements in the grid. This pattern

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
            (after repetition)
            [1, 2, 3, 1, 2, 3, 1, 2]
            (after repeating to fit in the grid)
            [1, 2, 3, 1,
             2, 3, 1, 2,
             2, 1, 3, 2,
             1, 3, 2, 1]

        """
    _fixed_grid = False
        
    def generate(self):
        p = Pattern(self.pattern)
        required_count = self.n_rows * self.n_cols
        
        if len(p.pattern) < int(required_count/2) + 1:
            p = p.RepeatPattern(int(required_count/2) + 1)
        
        if required_count%2 == 0:
            m1 = p.pattern[:int(required_count/2)]
            m2 = m1[::-1]
            p.pattern = m1 + m2
        else:
            m1 = p.pattern[:int((required_count+1)/2)]
            m2 = m1[::-1]
            p.pattern = m1 + m2[1:]
            
        result = p

        if self._jitter is not None:
            result = result._CalculateJitter(distribution = self._jitter, distribution_parameters = self._jitter_parameters)                 

        if self._randomization is not None:
            if self._randomization == "RandomizeAcrossElements":
                result = result._SetRandomizeAcrossElements()   
            elif self._randomization == "RandomizeAcrossRows":
                result = result._SetRandomizeAcrossRows(n_rows = self.n_rows, n_cols = self.n_cols)      
            elif self._randomization == "RandomizeAcrossColumns":
                result = result._SetRandomizeAcrossColumns(n_rows = self.n_rows, n_cols = self.n_cols)       
            elif self._randomization == "RandomizeAcrossLeftDiagonal":
                result = result._SetRandomizeAcrossLeftDiagonal(n_rows = self.n_rows, n_cols = self.n_cols)    
            elif self._randomization == "RandomizeAcrossRightDiagonal":
                result = result._SetRandomizeAcrossRightDiagonal(n_rows = self.n_rows, n_cols = self.n_cols)    
            elif self._randomization == "RandomizeAcrossLayers":
                result = result._SetRandomizeAcrossLayers(n_rows = self.n_rows, n_cols = self.n_cols)     
         
        self.patterntype = "Mirror"
        self.patterndirection = "AcrossElements"

        return MirrorAcrossElements(result.pattern, self.n_rows, self.n_cols, self.patterntype, self.patterndirection)
    
    
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
    _fixed_grid = False
    
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
            
        result = p.RepeatElements(self.n_cols)

        if self._jitter is not None:
            result = result._CalculateJitter(distribution = self._jitter, distribution_parameters = self._jitter_parameters)                 

        if self._randomization is not None:
            if self._randomization == "RandomizeAcrossElements":
                result = result._SetRandomizeAcrossElements()   
            elif self._randomization == "RandomizeAcrossRows":
                result = result._SetRandomizeAcrossRows(n_rows = self.n_rows, n_cols = self.n_cols)      
            elif self._randomization == "RandomizeAcrossColumns":
                result = result._SetRandomizeAcrossColumns(n_rows = self.n_rows, n_cols = self.n_cols)     
            elif self._randomization == "RandomizeAcrossLeftDiagonal":
                result = result._SetRandomizeAcrossLeftDiagonal(n_rows = self.n_rows, n_cols = self.n_cols)    
            elif self._randomization == "RandomizeAcrossRightDiagonal":
                result = result._SetRandomizeAcrossRightDiagonal(n_rows = self.n_rows, n_cols = self.n_cols)    
            elif self._randomization == "RandomizeAcrossLayers":
                result = result._SetRandomizeAcrossLayers(n_rows = self.n_rows, n_cols = self.n_cols)        
         
        self.patterntype = "Mirror"
        self.patterndirection = "AcrossRows"

        return MirrorAcrossRows(result.pattern, self.n_rows, self.n_cols, self.patterntype, self.patterndirection)
            
    
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
    _fixed_grid = False
    
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
            
        result = p.RepeatPattern(self.n_rows)
 
        if self._jitter is not None:
            result = result._CalculateJitter(distribution = self._jitter, distribution_parameters = self._jitter_parameters)                 

        if self._randomization is not None:
            if self._randomization == "RandomizeAcrossElements":
                result = result._SetRandomizeAcrossElements()   
            elif self._randomization == "RandomizeAcrossRows":
                result = result._SetRandomizeAcrossRows(n_rows = self.n_rows, n_cols = self.n_cols)      
            elif self._randomization == "RandomizeAcrossColumns":
                result = result._SetRandomizeAcrossColumns(n_rows = self.n_rows, n_cols = self.n_cols)      
            elif self._randomization == "RandomizeAcrossLeftDiagonal":
                result = result._SetRandomizeAcrossLeftDiagonal(n_rows = self.n_rows, n_cols = self.n_cols)    
            elif self._randomization == "RandomizeAcrossRightDiagonal":
                result = result._SetRandomizeAcrossRightDiagonal(n_rows = self.n_rows, n_cols = self.n_cols)    
            elif self._randomization == "RandomizeAcrossLayers":
                result = result._SetRandomizeAcrossLayers(n_rows = self.n_rows, n_cols = self.n_cols)      
        
        self.patterntype = "Mirror"
        self.patterndirection = "AcrossColumns"

        return MirrorAcrossColumns(result.pattern, self.n_rows, self.n_cols, self.patterntype, self.patterndirection)
    
    
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
    _fixed_grid = False    
    
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
                    
        result = Pattern(result)

        if self._jitter is not None:
            result = result._CalculateJitter(distribution = self._jitter, distribution_parameters = self._jitter_parameters)                 

        if self._randomization is not None:
            if self._randomization == "RandomizeAcrossElements":
                result = result._SetRandomizeAcrossElements()   
            elif self._randomization == "RandomizeAcrossRows":
                result = result._SetRandomizeAcrossRows(n_rows = self.n_rows, n_cols = self.n_cols)       
            elif self._randomization == "RandomizeAcrossColumns":
                result = result._SetRandomizeAcrossColumns(n_rows = self.n_rows, n_cols = self.n_cols)     
            elif self._randomization == "RandomizeAcrossLeftDiagonal":
                result = result._SetRandomizeAcrossLeftDiagonal(n_rows = self.n_rows, n_cols = self.n_cols)    
            elif self._randomization == "RandomizeAcrossRightDiagonal":
                result = result._SetRandomizeAcrossRightDiagonal(n_rows = self.n_rows, n_cols = self.n_cols)    
            elif self._randomization == "RandomizeAcrossLayers":
                result = result._SetRandomizeAcrossLayers(n_rows = self.n_rows, n_cols = self.n_cols)      
 
        self.patterntype = "Mirror"
        self.patterndirection = "AcrossLeftDiagonal"
                
        return MirrorAcrossLeftDiagonal(result.pattern, self.n_rows, self.n_cols, self.patterntype, self.patterndirection)
    
    
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
    _fixed_grid = False
    
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
                    
        result = Pattern(result)

        if self._jitter is not None:
            result = result._CalculateJitter(distribution = self._jitter, distribution_parameters = self._jitter_parameters)                 

        if self._randomization is not None:
            if self._randomization == "RandomizeAcrossElements":
                result = result._SetRandomizeAcrossElements()   
            elif self._randomization == "RandomizeAcrossRows":
                result = result._SetRandomizeAcrossRows(n_rows = self.n_rows, n_cols = self.n_cols)       
            elif self._randomization == "RandomizeAcrossColumns":
                result = result._SetRandomizeAcrossColumns(n_rows = self.n_rows, n_cols = self.n_cols)     
            elif self._randomization == "RandomizeAcrossLeftDiagonal":
                result = result._SetRandomizeAcrossLeftDiagonal(n_rows = self.n_rows, n_cols = self.n_cols)    
            elif self._randomization == "RandomizeAcrossRightDiagonal":
                result = result._SetRandomizeAcrossRightDiagonal(n_rows = self.n_rows, n_cols = self.n_cols)    
            elif self._randomization == "RandomizeAcrossLayers":
                result = result._SetRandomizeAcrossLayers(n_rows = self.n_rows, n_cols = self.n_cols)      
         
        self.patterntype = "Mirror"
        self.patterndirection = "AcrossRightDiagonal"
               
        return MirrorAcrossRightDiagonal(result.pattern, self.n_rows, self.n_cols, self.patterntype, self.patterndirection)
  
class MirrorAcrossLayers(GridPattern):
    """
        Mirrors the provided pattern across the layers within the stimulus running from inside to outside layers.

        Returns
        -------
        GridPattern
            Current instance of the GridPattern object.
            
        Example
        -------
        pattern: 
            [1, 2]
        n_rows:
            6
        n_cols:
            6
            
        result:
            [1, 1, 1, 1, 1, 1, 
             1, 2, 2, 2, 2, 1,
             1, 2, 1, 1, 2, 1, 
             1, 2, 1, 1, 2, 1, 
             1, 2, 2, 2, 2, 1, 
             1, 1, 1, 1, 1, 1]
            

    """ 
    _fixed_grid = False
    def generate(self):  
        assert (self.n_rows > 2), "number of rows in the Grid should be more than 2 to apply this pattern"
        assert (self.n_cols > 2), "number of columns in the Grid should be more than 2 to apply this pattern"
        
        p = Pattern(self.pattern)
        
        n_rows = self.n_rows
        n_cols = self.n_cols
        
        minimal_n = min(n_rows, n_cols)
        if minimal_n % 2 == 0: 
            n_layers = int(minimal_n / 2)
        else:
            n_layers = int((minimal_n + 1 )/2)
        
        # max_elements = int(n_layers/2)
        
        if len(p.pattern) < int(n_layers/2) + 1:
            p = Pattern(p.pattern[::-1])
            p = p.RepeatPattern(int(n_layers/2) + 1)
        
        if n_layers%2 == 0:
            m1 = p.pattern[:int(n_layers/2)]
            m2 = m1[::-1]
            p.pattern = m1 + m2
        else:
            m1 = p.pattern[:int((n_layers+1)/2)]
            m2 = m1[::-1]
            p.pattern = m1 + m2[1:]
            
        patternmatrix = [[0 for x in range(n_cols)] for y in range(n_rows)] 
        
        for layer in range(n_layers):
            width = n_cols - (2*layer)
            start_row = layer
            start_col = layer
            end_row = n_rows - layer - 1
            end_col = n_cols - layer
            patternmatrix[start_row][start_col:end_col] = [p.pattern[layer]] * (width)
            patternmatrix[end_row][start_col:end_col] = [p.pattern[layer]] * (width)
            for row in patternmatrix[start_row:end_row]:
                row[start_col] = p.pattern[layer] 
                row[end_col-1] = p.pattern[layer] 
       
        result = Pattern([item for sublist in patternmatrix for item in sublist])

        if self._jitter is not None:
            result = result._CalculateJitter(distribution = self._jitter, distribution_parameters = self._jitter_parameters)                 

        if self._randomization is not None:
            if self._randomization == "RandomizeAcrossElements":
                result = result._SetRandomizeAcrossElements()   
            elif self._randomization == "RandomizeAcrossRows":
                result = result._SetRandomizeAcrossRows(n_rows = self.n_rows, n_cols = self.n_cols)       
            elif self._randomization == "RandomizeAcrossColumns":
                result = result._SetRandomizeAcrossColumns(n_rows = self.n_rows, n_cols = self.n_cols)     
            elif self._randomization == "RandomizeAcrossLeftDiagonal":
                result = result._SetRandomizeAcrossLeftDiagonal(n_rows = self.n_rows, n_cols = self.n_cols)    
            elif self._randomization == "RandomizeAcrossRightDiagonal":
                result = result._SetRandomizeAcrossRightDiagonal(n_rows = self.n_rows, n_cols = self.n_cols)    
            elif self._randomization == "RandomizeAcrossLayers":
                result = result._SetRandomizeAcrossLayers(n_rows = self.n_rows, n_cols = self.n_cols)      
                             
        self.patterntype = "Mirror"
        self.patterndirection = "AcrossLayers"

        return MirrorAcrossLayers(result.pattern, self.n_rows, self.n_cols, self.patterntype, self.patterndirection) 
        
class GradientAcrossElements(GridPattern):
    """
    Creates a gradient where the number of elements equals the total number of elements in the grid.

    Returns
    -------
    GridGradient
        Current instance of the object.

    """
    _fixed_grid = False
    
    def __init__(self, start_value, end_value, n_rows = 5, n_cols = 5):
        self.start_value = start_value
        self.end_value   = end_value
        self.n_rows = n_rows
        self.n_cols = n_cols
        self._jitter = None
        self._jitter_parameters = {}
        self._randomization = None
        
    def generate(self):
        n_elements = self.n_rows * self.n_cols
        result = Pattern.CreateGradientPattern(self.start_value, self.end_value, n_elements)

        if self._jitter is not None:
            result = result._CalculateJitter(distribution = self._jitter, distribution_parameters = self._jitter_parameters)                 

        if self._randomization is not None:
            if self._randomization == "RandomizeAcrossElements":
                result = result._SetRandomizeAcrossElements()   
            elif self._randomization == "RandomizeAcrossRows":
                result = result._SetRandomizeAcrossRows(n_rows = self.n_rows, n_cols = self.n_cols)      
            elif self._randomization == "RandomizeAcrossColumns":
                result = result._SetRandomizeAcrossColumns(n_rows = self.n_rows, n_cols = self.n_cols)      
            elif self._randomization == "RandomizeAcrossLeftDiagonal":
                result = result._SetRandomizeAcrossLeftDiagonal(n_rows = self.n_rows, n_cols = self.n_cols)    
            elif self._randomization == "RandomizeAcrossRightDiagonal":
                result = result._SetRandomizeAcrossRightDiagonal(n_rows = self.n_rows, n_cols = self.n_cols)    
            elif self._randomization == "RandomizeAcrossLayers":
                result = result._SetRandomizeAcrossLayers(n_rows = self.n_rows, n_cols = self.n_cols)       
 
        self.pattern = result.pattern
        self.patterntype = "Gradient"
        self.patterndirection = "AcrossElements"
        
        return GridPattern(result.pattern, self.n_rows, self.n_cols, self.patterntype, self.patterndirection)
    

class GradientAcrossRows(GridPattern):
    """
    Creates a gradient across the rows of the grid.

    Returns
    -------
    GridGradient
        Current instance of the object.

    """
    _fixed_grid = False
    
    def __init__(self, start_value, end_value, n_rows = 5, n_cols = 5):
        self.start_value = start_value
        self.end_value   = end_value
        self.n_rows = n_rows
        self.n_cols = n_cols
        self._jitter = None
        self._jitter_parameters = {}
        self._randomization = None
        
    def generate(self):
        p = Pattern.CreateGradientPattern(self.start_value, self.end_value, self.n_rows)
        result = p.RepeatElements(self.n_cols)

        if self._jitter is not None:
            result = result._CalculateJitter(distribution = self._jitter, distribution_parameters = self._jitter_parameters)                 

        if self._randomization is not None:
            if self._randomization == "RandomizeAcrossElements":
                result = result._SetRandomizeAcrossElements()   
            elif self._randomization == "RandomizeAcrossRows":
                result = result._SetRandomizeAcrossRows(n_rows = self.n_rows, n_cols = self.n_cols)      
            elif self._randomization == "RandomizeAcrossColumns":
                result = result._SetRandomizeAcrossColumns(n_rows = self.n_rows, n_cols = self.n_cols)        
            elif self._randomization == "RandomizeAcrossLeftDiagonal":
                result = result._SetRandomizeAcrossLeftDiagonal(n_rows = self.n_rows, n_cols = self.n_cols)    
            elif self._randomization == "RandomizeAcrossRightDiagonal":
                result = result._SetRandomizeAcrossRightDiagonal(n_rows = self.n_rows, n_cols = self.n_cols)    
            elif self._randomization == "RandomizeAcrossLayers":
                result = result._SetRandomizeAcrossLayers(n_rows = self.n_rows, n_cols = self.n_cols)    
         
        self.pattern = result.pattern
        self.patterntype = "Gradient"
        self.patterndirection = "AcrossRows"

        return GridPattern(result.pattern, self.n_rows, self.n_cols, self.patterntype, self.patterndirection)
    
    
class GradientAcrossColumns(GridPattern):
    """
    Creates a gradient across the columns of the grid.

    Returns
    -------
    GridGradient
        Current instance of the object.

    """
    _fixed_grid = False
    
    def __init__(self, start_value, end_value, n_rows = 5, n_cols = 5):
        self.start_value = start_value
        self.end_value   = end_value
        self.n_rows = n_rows
        self.n_cols = n_cols
        self._jitter = None
        self._jitter_parameters = {}
        self._randomization = None
        
    def generate(self):      
        p = Pattern.CreateGradientPattern(self.start_value, self.end_value, self.n_cols)
        result = p.RepeatPattern(self.n_rows)
 
        if self._jitter is not None:
            result = result._CalculateJitter(distribution = self._jitter, distribution_parameters = self._jitter_parameters)                 

        if self._randomization is not None:
            if self._randomization == "RandomizeAcrossElements":
                result = result._SetRandomizeAcrossElements()   
            elif self._randomization == "RandomizeAcrossRows":
                result = result._SetRandomizeAcrossRows(n_rows = self.n_rows, n_cols = self.n_cols)       
            elif self._randomization == "RandomizeAcrossColumns":
                result = result._SetRandomizeAcrossColumns(n_rows = self.n_rows, n_cols = self.n_cols)      
            elif self._randomization == "RandomizeAcrossLeftDiagonal":
                result = result._SetRandomizeAcrossLeftDiagonal(n_rows = self.n_rows, n_cols = self.n_cols)    
            elif self._randomization == "RandomizeAcrossRightDiagonal":
                result = result._SetRandomizeAcrossRightDiagonal(n_rows = self.n_rows, n_cols = self.n_cols)    
            elif self._randomization == "RandomizeAcrossLayers":
                result = result._SetRandomizeAcrossLayers(n_rows = self.n_rows, n_cols = self.n_cols)     
        
        self.pattern = result.pattern
        self.patterntype = "Gradient"
        self.patterndirection = "AcrossColumns"

        return GridPattern(result.pattern, self.n_rows, self.n_cols, self.patterntype, self.patterndirection)
    
    
class GradientAcrossLeftDiagonal(GridPattern):
    """
    Creates a diagonal gradient, starting in the top right corner and ending in the bottom left corner.

    Returns
    -------
    GridGradient
        Current instance of the object.

    """
    _fixed_grid = False
    
    def __init__(self, start_value, end_value, n_rows = 5, n_cols = 5):
        self.start_value = start_value
        self.end_value   = end_value
        self.n_rows = n_rows
        self.n_cols = n_cols
        self._jitter = None
        self._jitter_parameters = {}
        self._randomization = None
        
    def generate(self):
        n_elements = self.n_rows + self.n_cols - 1
        shifter = Pattern.CreateGradientPattern(self.start_value, self.end_value, n_elements).pattern
          
        result = []
        for i in range(self.n_rows):
            result.extend(shifter[:self.n_cols][::-1])
            shifter = shifter[1:] + [shifter[0]]
                    
        result = Pattern(result)
 
        if self._jitter is not None:
            result = result._CalculateJitter(distribution = self._jitter, distribution_parameters = self._jitter_parameters)                 

        if self._randomization is not None:
            if self._randomization == "RandomizeAcrossElements":
                result = result._SetRandomizeAcrossElements()   
            elif self._randomization == "RandomizeAcrossRows":
                result = result._SetRandomizeAcrossRows(n_rows = self.n_rows, n_cols = self.n_cols)      
            elif self._randomization == "RandomizeAcrossColumns":
                result = result._SetRandomizeAcrossColumns(n_rows = self.n_rows, n_cols = self.n_cols)      
            elif self._randomization == "RandomizeAcrossLeftDiagonal":
                result = result._SetRandomizeAcrossLeftDiagonal(n_rows = self.n_rows, n_cols = self.n_cols)    
            elif self._randomization == "RandomizeAcrossRightDiagonal":
                result = result._SetRandomizeAcrossRightDiagonal(n_rows = self.n_rows, n_cols = self.n_cols)    
            elif self._randomization == "RandomizeAcrossLayers":
                result = result._SetRandomizeAcrossLayers(n_rows = self.n_rows, n_cols = self.n_cols)       
                
        self.pattern = Pattern(result).pattern
        self.patterntype = "Gradient"
        self.patterndirection = "AcrossLeftDiagonal"

        return GridPattern(result.pattern, self.n_rows, self.n_cols, self.patterntype, self.patterndirection)
        
    
class GradientAcrossRightDiagonal(GridPattern):
    """
    Creates a diagonal gradient, starting in the top left corner and ending in the bottom right corner.

    Returns
    -------
    GridGradient
        Current instance of the object.

    """
    _fixed_grid = False
    
    def __init__(self, start_value, end_value, n_rows = 5, n_cols = 5):
        self.start_value = start_value
        self.end_value   = end_value
        self.n_rows = n_rows
        self.n_cols = n_cols
        self._jitter = None
        self._jitter_parameters = {}
        self._randomization = None
        
    def generate(self):
        n_elements = self.n_rows + self.n_cols - 1
        shifter = Pattern.CreateGradientPattern(self.start_value, self.end_value, n_elements).pattern
            
        result = []
        for i in range(self.n_rows):
            result.extend(shifter[:self.n_cols])
            shifter = shifter[1:] + [shifter[0]]
                    
        result = Pattern(result)

        if self._jitter is not None:
            result = result._CalculateJitter(distribution = self._jitter, distribution_parameters = self._jitter_parameters)                 

        if self._randomization is not None:
            if self._randomization == "RandomizeAcrossElements":
                result = result._SetRandomizeAcrossElements()   
            elif self._randomization == "RandomizeAcrossRows":
                result = result._SetRandomizeAcrossRows(n_rows = self.n_rows, n_cols = self.n_cols)       
            elif self._randomization == "RandomizeAcrossColumns":
                result = result._SetRandomizeAcrossColumns(n_rows = self.n_rows, n_cols = self.n_cols)     
            elif self._randomization == "RandomizeAcrossLeftDiagonal":
                result = result._SetRandomizeAcrossLeftDiagonal(n_rows = self.n_rows, n_cols = self.n_cols)    
            elif self._randomization == "RandomizeAcrossRightDiagonal":
                result = result._SetRandomizeAcrossRightDiagonal(n_rows = self.n_rows, n_cols = self.n_cols)    
            elif self._randomization == "RandomizeAcrossLayers":
                result = result._SetRandomizeAcrossLayers(n_rows = self.n_rows, n_cols = self.n_cols)      
                 
        self.pattern = Pattern(result).pattern
        self.patterntype = "Gradient"
        self.patterndirection = "AcrossRightDiagonal"

        return GridPattern(result.pattern, self.n_rows, self.n_cols, self.patterntype, self.patterndirection)
    
class GradientAcrossLayers(GridPattern):
    """
        Creates a gradient across the layers within the stimulus running from inside to outside layers.

        Returns
        -------
        GridPattern
            Current instance of the GridPattern object.
            
        Example
        -------
        pattern: 
            [1, 2]
        n_rows:
            6
        n_cols:
            6
            
        result:
            [1, 1, 1, 1, 1, 1, 
             1, 2, 2, 2, 2, 1,
             1, 2, 1, 1, 2, 1, 
             1, 2, 1, 1, 2, 1, 
             1, 2, 2, 2, 2, 1, 
             1, 1, 1, 1, 1, 1]
            

    """ 
    _fixed_grid = False
    
    def __init__(self, start_value, end_value, n_rows = 5, n_cols = 5):
        self.start_value = start_value
        self.end_value   = end_value
        self.n_rows = n_rows
        self.n_cols = n_cols
        self._jitter = None
        self._jitter_parameters = {}
        self._randomization = None
           
    def generate(self):  
        assert (self.n_rows > 2), "number of rows in the Grid should be more than 2 to apply this pattern"
        assert (self.n_cols > 2), "number of columns in the Grid should be more than 2 to apply this pattern"
               
        n_rows = self.n_rows
        n_cols = self.n_cols
        
        minimal_n = min(n_rows, n_cols)
        if minimal_n % 2 == 0: 
            n_layers = int(minimal_n / 2)
        else:
            n_layers = int((minimal_n + 1 )/2)
        
        p = Pattern.CreateGradientPattern(self.start_value, self.end_value, n_layers)
        p.pattern = p.pattern[::-1]
          
        patternmatrix = [[0 for x in range(n_cols)] for y in range(n_rows)] 
        
        for layer in range(n_layers):
            width = n_cols - (2*layer)
            start_row = layer
            start_col = layer
            end_row = n_rows - layer - 1
            end_col = n_cols - layer
            patternmatrix[start_row][start_col:end_col] = [p.pattern[layer]] * (width)
            patternmatrix[end_row][start_col:end_col] = [p.pattern[layer]] * (width)
            for row in patternmatrix[start_row:end_row]:
                row[start_col] = p.pattern[layer] 
                row[end_col-1] = p.pattern[layer] 
       
        result = Pattern([item for sublist in patternmatrix for item in sublist])

        if self._jitter is not None:
            result = result._CalculateJitter(distribution = self._jitter, distribution_parameters = self._jitter_parameters)                 

        if self._randomization is not None:
            if self._randomization == "RandomizeAcrossElements":
                result = result._SetRandomizeAcrossElements()   
            elif self._randomization == "RandomizeAcrossRows":
                result = result._SetRandomizeAcrossRows(n_rows = self.n_rows, n_cols = self.n_cols)       
            elif self._randomization == "RandomizeAcrossColumns":
                result = result._SetRandomizeAcrossColumns(n_rows = self.n_rows, n_cols = self.n_cols)     
            elif self._randomization == "RandomizeAcrossLeftDiagonal":
                result = result._SetRandomizeAcrossLeftDiagonal(n_rows = self.n_rows, n_cols = self.n_cols)    
            elif self._randomization == "RandomizeAcrossRightDiagonal":
                result = result._SetRandomizeAcrossRightDiagonal(n_rows = self.n_rows, n_cols = self.n_cols)    
            elif self._randomization == "RandomizeAcrossLayers":
                result = result._SetRandomizeAcrossLayers(n_rows = self.n_rows, n_cols = self.n_cols)      
                             
        self.pattern = Pattern(result).pattern
        self.patterntype = "Gradient"
        self.patterndirection = "AcrossLayers"

        return GridPattern(result.pattern, self.n_rows, self.n_cols, self.patterntype, self.patterndirection)

# class LayeredGrid(GridPattern):
#     """
#     Creates a grid that starts from a central structure, around which
#     additional layers are placed.

#     Parameters
#     ----------
#     center_grid : GridPattern
#         A grid pattern that forms the central structure
        
#     outer_layer : Pattern
#         The values for each of the outer layers. Each value in the pattern
#         becomes the next layer around the central grid structure
#     Example
#     -------
#     pattern: 
#         [1, 2, 3]
#     n_rows:
#         6
#     n_cols:
#         6
        
#     result:
#         [1, 1, 1, 1, 1, 1, 
#          1, 2, 2, 2, 2, 1, 
#          1, 2, 3, 3, 2, 1, 
#          1, 2, 3, 3, 2, 1, 
#          1, 2, 2, 2, 2, 1, 
#          1, 1, 1, 1, 1, 1]
        

#     """
#     _fixed_grid = True
    
#     def __init__(self, center_grid, outer_layers):
#         assert "GridPattern" in str(type(center_grid)), "center_grid has to be a GridPattern type"
#         # assert issubclass(type(center_grid), GridPattern), "center_grid has to be a GridPattern type"
#         assert type(outer_layers) == Pattern, "outer_layers has to be a Pattern type"
        
#         self.center_grid = center_grid
#         self.outer_layers = outer_layers        
        
#         dim = self.get_dimensions()
#         self.n_rows = dim[0]
#         self.n_cols = dim[1]
#         self._jitter = None
#         self._jitter_parameters = {}
#         self._randomization = None
        
#     def get_dimensions(self):
#         n_rows, n_cols = self.center_grid.n_rows, self.center_grid.n_cols
#         n_rows += 2 * len(self.outer_layers.pattern)
#         n_cols += 2 * len(self.outer_layers.pattern)
        
#         return n_rows, n_cols
    
#     def generate(self):
        
#         # 1. Generate the center grid pattern
#         current_center = self.center_grid.generate().pattern
#         current_rows   = self.center_grid.n_rows
#         current_cols   = self.center_grid.n_cols
        
        
#         # 2. Recursively layer each layer around the center grid
#         for value in self.outer_layers.pattern:
#             # Calculate new dimensions
#             new_rows = current_rows + 2
#             new_cols = current_cols + 2
            
#             # Fill the values in the new grid            
#             new_center = []
#             t = 0
#             for r in range(new_rows):
#                 for c in range(new_cols):
#                     if r == 0 or r == new_rows - 1:
#                         new_center.append(value)
#                     elif c == 0 or c == new_cols - 1:
#                         new_center.append(value)
#                     else:
#                         new_center.append(current_center[t])
#                         t += 1
                        
#             # Update the current values
#             current_center = new_center
#             current_rows = new_rows
#             current_cols = new_cols
             
#         self.patterntype = "Layered"
#         self.patterndirection = "Grid"
            
#         return GridPattern(current_center, current_rows, current_cols, self.patterntype, self.patterndirection)
    
    
class TiledGrid(GridPattern):
    """
    The current grid is tiled across the rows and columns using the
    values in tile_multiplier

    Parameters
    ----------
    tile_multiplier : list, tuple or int
        Two values indicating the tiling along the rows and columns
        respectively. If a single integer is provided, the tiling will
        be the same along the rows and columns

    Returns
    -------
    GridPattern.

    """
    _fixed_grid = True
    
    def __init__(self, source_grid, tile_multiplier):
        assert type(tile_multiplier) == int or type(tile_multiplier) == list or type(tile_multiplier) == tuple, "tile_multiplier needs to be int, list or tuple"
        if type(tile_multiplier) == int:
            tile_multiplier = (tile_multiplier, tile_multiplier)
        else:
            assert len(tile_multiplier) == 2, "tile_multiplier must contain two values"
        
        self.tile_multiplier = tile_multiplier
        self.source_grid = source_grid
        
        dims = self.get_dimensions()
        self.n_rows = dims[0]
        self.n_cols = dims[1]
        self._jitter = None
        self._jitter_parameters = {}
        self._randomization = None
        
    
    def get_dimensions(self):
        n_rows = self.source_grid.n_rows * self.tile_multiplier[0]
        n_cols = self.source_grid.n_cols * self.tile_multiplier[1]
        
        return (n_rows, n_cols)
    
    def generate(self):            
        result = []
        
        source_pattern = self.source_grid.generate().pattern
        n_rows, n_cols = self.source_grid.n_rows, self.source_grid.n_cols
        
        for r in range(n_rows):
            start_idx = r * n_cols
            current_row = source_pattern[ start_idx : ( start_idx + n_cols)] * self.tile_multiplier[1]
            result.extend(current_row)
            
        result.extend(result * self.tile_multiplier[0])
                    
        result = Pattern(result)

        if self._jitter is not None:
            result = result._CalculateJitter(distribution = self._jitter, distribution_parameters = self._jitter_parameters)                 

        if self._randomization is not None:
            if self._randomization == "RandomizeAcrossElements":
                result = result._SetRandomizeAcrossElements()   
            elif self._randomization == "RandomizeAcrossRows":
                result = result._SetRandomizeAcrossRows(n_rows = self.n_rows, n_cols = self.n_cols)      
            elif self._randomization == "RandomizeAcrossColumns":
                result = result._SetRandomizeAcrossColumns(n_rows = self.n_rows, n_cols = self.n_cols)       
            elif self._randomization == "RandomizeAcrossLeftDiagonal":
                result = result._SetRandomizeAcrossLeftDiagonal(n_rows = self.n_rows, n_cols = self.n_cols)    
            elif self._randomization == "RandomizeAcrossRightDiagonal":
                result = result._SetRandomizeAcrossRightDiagonal(n_rows = self.n_rows, n_cols = self.n_cols)    
            elif self._randomization == "RandomizeAcrossLayers":
                result = result._SetRandomizeAcrossLayers(n_rows = self.n_rows, n_cols = self.n_cols)     
         
        self.pattern = source_pattern #Pattern(result).pattern 
        self.patterntype = "Tiled"
        self.patterndirection = "Grid"
        
        return GridPattern(result.pattern, n_rows * self.tile_multiplier[0], n_cols * self.tile_multiplier[1], self.patterntype, self.patterndirection)
    

class TiledElementGrid(GridPattern):
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
        GridPattern.

    """
    
    _fixed_grid = True
    def __init__(self, source_grid, tile_multiplier):
        assert type(tile_multiplier) == int or type(tile_multiplier) == list or type(tile_multiplier) == tuple, "tile_multiplier needs to be int, list or tuple"
        if type(tile_multiplier) == int:
            tile_multiplier = (tile_multiplier, tile_multiplier)
        else:
            assert len(tile_multiplier) == 2, "tile_multiplier must contain two values"
            
        self.tile_multiplier = tile_multiplier
        self.source_grid     = source_grid
        
        dims = self.get_dimensions()
        
#        self.pattern = self.source_grid
        self.n_rows = dims[0]
        self.n_cols = dims[1]
        self._jitter = None
        self._jitter_parameters = {}
        self._randomization = None
        
    def get_dimensions(self):
        n_rows = self.source_grid.n_rows * self.tile_multiplier[0]
        n_cols = self.source_grid.n_cols * self.tile_multiplier[1]
        
        return (n_rows, n_cols)
    
    def generate(self):
        result = []
    
        source_pattern = self.source_grid.generate().pattern
        n_rows, n_cols = self.source_grid.n_rows, self.source_grid.n_cols
        
        for r in range(n_rows):
            current_row = []
            for c in range(n_cols):
                idx = r * n_cols + c
                current_row.extend([source_pattern[idx]] * self.tile_multiplier[1])
                
            current_row = current_row * self.tile_multiplier[0]
            result.extend(current_row)
                    
        result = Pattern(result)
 
        if self._jitter is not None:
            result = result._CalculateJitter(distribution = self._jitter, distribution_parameters = self._jitter_parameters)                 

        if self._randomization is not None:
            if self._randomization == "RandomizeAcrossElements":
                result = result._SetRandomizeAcrossElements()   
            elif self._randomization == "RandomizeAcrossRows":
                result = result._SetRandomizeAcrossRows(n_rows = self.n_rows, n_cols = self.n_cols)       
            elif self._randomization == "RandomizeAcrossColumns":
                result = result._SetRandomizeAcrossColumns(n_rows = self.n_rows, n_cols = self.n_cols)        
            elif self._randomization == "RandomizeAcrossLeftDiagonal":
                result = result._SetRandomizeAcrossLeftDiagonal(n_rows = self.n_rows, n_cols = self.n_cols)    
            elif self._randomization == "RandomizeAcrossRightDiagonal":
                result = result._SetRandomizeAcrossRightDiagonal(n_rows = self.n_rows, n_cols = self.n_cols)    
            elif self._randomization == "RandomizeAcrossLayers":
                result = result._SetRandomizeAcrossLayers(n_rows = self.n_rows, n_cols = self.n_cols)    
        
        self.pattern = source_pattern #Pattern(result).pattern    
#        self.pattern = result
        self.patterntype = "TiledElement"
        self.patterndirection = "Grid"
            
        return RepeatAcrossElements(result.pattern, self.n_rows, self.n_cols, self.patterntype, self.patterndirection)
       
class RandomPattern(GridPattern):
    """
        The provided pattern is repeated until the length is equal to the
        number of elements in the grid structure. The order of the elements 
        is then randomized. A list of proportions can be provided to decide
        how many times each element has to be repeated.

        Parameters
        ----------
        proportions : list (optional)
            Proportions for the random pattern.

        Returns
        -------
        GridPattern.
    """
    _fixed_grid = False
    
    def __init__(self, pattern, n_rows = 5, n_cols = 5, patterntype = None, patterndirection = None, counts = None):
        super().__init__(pattern, n_rows, n_cols)
        self.counts = counts
        self.patterntype = patterntype
        self.patterndirection = patterndirection
        self._jitter = None
        self._jitter_parameters = {}
        self._randomization = None
                
    def check_counts(self):
        if self.counts is not None:
            assert len(self.counts) == len(self.pattern), "Count and pattern must have same length"
            assert sum(self.counts) == self.n_rows * self.n_cols, "Counts must sum to pattern length"
            
    def generate(self):
        n_elements = self.n_rows * self.n_cols
        self.check_counts()
        
        if type(self.pattern) is not Pattern:
            p = Pattern(self.pattern)
        else:
            p = self.pattern
                        
        if self.counts is None:
            p = p.RepeatElementsToSize(n_elements)
        else:
            elements = []
            for i in range(len(self.counts)):
                elements.extend([p.pattern[i]] * self.counts[i])
                
            p.pattern = elements
            
        result = p.RandomizeOrder()

        if self._jitter is not None:
            result = result._CalculateJitter(distribution = self._jitter, distribution_parameters = self._jitter_parameters)                 

        if self._randomization is not None:
            if self._randomization == "RandomizeAcrossElements":
                result = result._SetRandomizeAcrossElements()   
            elif self._randomization == "RandomizeAcrossRows":
                result = result._SetRandomizeAcrossRows(n_rows = self.n_rows, n_cols = self.n_cols)       
            elif self._randomization == "RandomizeAcrossColumns":
                result = result._SetRandomizeAcrossColumns(n_rows = self.n_rows, n_cols = self.n_cols)        
            elif self._randomization == "RandomizeAcrossLeftDiagonal":
                result = result._SetRandomizeAcrossLeftDiagonal(n_rows = self.n_rows, n_cols = self.n_cols)    
            elif self._randomization == "RandomizeAcrossRightDiagonal":
                result = result._SetRandomizeAcrossRightDiagonal(n_rows = self.n_rows, n_cols = self.n_cols)    
            elif self._randomization == "RandomizeAcrossLayers":
                result = result._SetRandomizeAcrossLayers(n_rows = self.n_rows, n_cols = self.n_cols)   
         
        self.patterntype = "RandomPattern"
        self.patterndirection = ""
        
        return RandomPattern(result.pattern, self.n_rows, self.n_cols, self.patterntype, self.patterndirection)