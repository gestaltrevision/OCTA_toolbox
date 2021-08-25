"""
Pattern code for the OCTA toolbox
This module contains a base class with several essential functions for patterns.
More complex patterns (e.g., grid based patterns) can be derived from this class.

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
import colour
import random
import types

class Pattern:
    def __init__(self, pattern, patterntype = "", patterndirection = "", patternclass = "Pattern"):
        """
        Initializes a Pattern object. If the provided input is not a list,
        the pattern will be initialized with a list that contains the provided
        input as the first and only element.

        Parameters
        ----------
        pattern : any type
            List object with initial values for the pattern.
        patterntype : string
            Indicates the pattern type used.
        patterndirection : string
            Indicates the pattern direction used.
        patternclass : string
            Indicates the pattern class used.
        """
        
        if type(pattern) == list:
            self.pattern = pattern
        elif type(pattern) == Pattern:
            self.pattern = pattern.pattern
        else:
            self.pattern = [pattern]
            
        self.patternclass = patternclass        
        self.patterntype = patterntype
        self.patterndirection = patterndirection
        
        
    def __str__(self):
        """
        Creates a string representation of the pattern.

        Returns
        -------
        string
            String representation of the pattern.

        """
        return str(self.pattern)
    
    def __add__(self, o):
        """
        The + operator can be used to add the values in two patterns
        element-wise.

        Parameters
        ----------
        o : Pattern object
            The object with values that need to be added to the current pattern.

        Returns
        -------
        Pattern
            Pattern object.

        """
        assert len(self.pattern) == len(o.pattern), "Pattern length must be equal"
        
        numerical_values = True
        for i in range(len(self.pattern)):
            if not (isinstance(self.pattern[i], (int, float)) and isinstance(self.pattern[i], (int, float))):
                numerical_values = False        
        assert numerical_values == True, "Pattern values must be numerical values"
        
        
        result = [self.pattern[i] + o.pattern[i] for i in range(len(self.pattern))]
            
        return Pattern(result)
    
    
    def RepeatElements(self, n_repeats, max_elements = None):
        """
        Repeats each element in the pattern.

        Parameters
        ----------
        n_repeats : int
            How many times each elements needs to be repeated.
        max_elements : int, optional
            Maximum number of elements in the resulting pattern. If specified,
            the pattern will be truncated to this number of elements if the total
            length is exceeded after applying the repetition. 
            The default is None.

        Returns
        -------
        Pattern
            Current instance of Pattern.
            
        Examples
        --------
        initial pattern:
            [1, 2, 3]
        n_duplications:
            3
        resulting pattern:
            [1, 1, 1, 2, 2, 2, 3, 3, 3]
        """
        result = []
        for el in self.pattern:
            result.extend([el]*n_repeats)
        
        if max_elements != None:
            result = result[:max_elements]
            
        patterntype = "RepeatElements"
        patterndirection = ""
            
        return Pattern(result, patterntype, patterndirection)
            
            
    def RepeatPattern(self, n_repeats, max_elements = None):
        """
        Repeats the pattern as a whole.

        Parameters
        ----------
        n_repeats : int
            How many times the pattern needs to be repeated.
        max_elements : int, optional
            Maximum number of elements in the resulting pattern. The default is None.

        Returns
        -------
        Pattern
            Current instance of Pattern.

        """
        result = []
        
        for i in range(n_repeats):
            result.extend(self.pattern)
        
        
        if max_elements != None:
            result = result[:max_elements]
            
        patterntype = "RepeatPattern"
        patterndirection = ""
        
        return Pattern(result, patterntype, patterndirection)
    
    def RepeatElementsToSize(self, count):
        """
        Repeats the elements in the pattern until the total pattern length
        is equal or exceeds to the requested count. If the total pattern length 
        exceeds the count, the pattern is truncated.

        Parameters
        ----------
        count : int
            Required number of elements in the pattern.

        Returns
        -------
        Pattern
            New Pattern object instance

        """
        if count % len(self.pattern) != 0:
            n_repeats = int(count/len(self.pattern)) + 1
        else:
            n_repeats = int(count/len(self.pattern))
        
        new_pattern = self.RepeatElements(n_repeats, count)
        
        return new_pattern
        
    
    def RepeatPatternToSize(self, count):
        """
        Repeats the pattern until the total pattern length is equal to or 
        exceeds the requested count. If the total pattern length exceeds the 
        count, the pattern is truncated.

        Parameters
        ----------
        count : int
            Required number of elements in the pattern.

        Returns
        -------
        Pattern
            New Pattern object instance

        """
        if count % len(self.pattern) != 0:
            n_repeats = int(count/len(self.pattern)) + 1
        else:
            n_repeats = int(count/len(self.pattern))
        
        new_pattern = self.RepeatPattern(n_repeats, count)
        
        return new_pattern
    
    def _CalculateJitter(self, distribution, distribution_parameters):
        """
        Adds a sample from a random normal distribution to each element in the pattern.

        Parameters
        ----------
        distribution :  string
            Options are 'normal' or 'uniform'
        distribution_parameters : dictionary
            Provides parameters for the specified distribution.

        Returns
        -------
        Pattern:
            New Pattern object instance

        """
        p = self
        
        if distribution == "normal":
     
             values = p.pattern
             mu = distribution_parameters['mu']
             std = distribution_parameters['std'] 
             axis = distribution_parameters['axis'] 
         
             p = Pattern(values).AddNormalJitter(mu = mu , std = std, axis = axis)  
             
        if distribution == "uniform":
     
             values = p.pattern
             min_val = distribution_parameters['min_val']
             max_val = distribution_parameters['max_val']  
             axis = distribution_parameters['axis']        
         
             p = Pattern(values).AddUniformJitter(min_val = min_val, max_val = max_val, axis = axis) 
             
        return p
            
    
    def AddNormalJitter(self, mu = 0, std = 1, axis = None):
        """
        Adds a sample from a random normal distribution to each element in the pattern.

        Parameters
        ----------
        mu : float, optional
            Mean of the normal distribution. The default is 0.
        std : float, optional
            Standard deviation of the normal distribution. The default is 1.
        axis : string, optional
            String that contains the axis to which jitter should be applied.
            Possible values are "x", "y", "xy" or "x=y". 

        Returns
        -------
        Pattern:
            New Pattern object instance

        """
        result = []
        if type(self.pattern[0]) == int or type(self.pattern[0]) == float:
            for i in range(len(self.pattern)):
                result.append(self.pattern[i] + random.normalvariate(mu, std))
        elif type(self.pattern[0]) == tuple:
            if axis is None:
                for i in range(len(self.pattern)):
                    xresult = self.pattern[i][0] + random.normalvariate(mu, std)
                    yresult = self.pattern[i][1] + random.normalvariate(mu, std)
                    result.append((xresult, yresult))
            elif axis == 'x':
                for i in range(len(self.pattern)):
                    xresult = self.pattern[i][0] + random.normalvariate(mu, std)
                    yresult = self.pattern[i][1]
                    result.append((xresult, yresult))
            elif axis == 'y':
                for i in range(len(self.pattern)):
                    xresult = self.pattern[i][0]
                    yresult = self.pattern[i][1] + random.normalvariate(mu, std)
                    result.append((xresult, yresult))
            elif axis == 'xy':
                for i in range(len(self.pattern)):
                    xresult = self.pattern[i][0] + random.normalvariate(mu, std)
                    yresult = self.pattern[i][1] + random.normalvariate(mu, std)
                    result.append((xresult, yresult)) 
            elif axis == 'x=y':
                for i in range(len(self.pattern)):
                    randomvalue = random.normalvariate(mu, std)
                    xresult = self.pattern[i][0] + randomvalue
                    yresult = self.pattern[i][1] + randomvalue
                    result.append((xresult, yresult))            
        
        return Pattern(result)
    
    
    def AddUniformJitter(self, min_val = -1, max_val = 1, axis = None):
        """
        Adds a sample from a uniform distribution to each element in the pattern.

        Parameters
        ----------
        min_val : float, optional
            Lower bound of the uniform distribution
        max_val : float, optional
            Upper bound of the uniform distribution
        axis : string, optional
            String that contains the axis to which jitter should be applied.
            Possible values are "x", "y", "xy" or "x=y". 

        Returns
        -------
        Pattern:
            New Pattern object instance

        """
        result = []
        if type(self.pattern[0]) == int or type(self.pattern[0]) == float:
            for i in range(len(self.pattern)):
                result.append(self.pattern[i] + random.uniform(min_val, max_val))
        elif type(self.pattern[0]) == tuple:
            if axis is None:
                for i in range(len(self.pattern)):
                    xresult = self.pattern[i][0] + random.uniform(min_val, max_val)
                    yresult = self.pattern[i][1] + random.uniform(min_val, max_val)
                    result.append((xresult, yresult))
            elif axis == 'x':
                for i in range(len(self.pattern)):
                    xresult = self.pattern[i][0] + random.uniform(min_val, max_val)
                    yresult = self.pattern[i][1]
                    result.append((xresult, yresult))
            elif axis == 'y':
                for i in range(len(self.pattern)):
                    xresult = self.pattern[i][0]
                    yresult = self.pattern[i][1] + random.uniform(min_val, max_val)
                    result.append((xresult, yresult))
            elif axis == 'xy':
                for i in range(len(self.pattern)):
                    xresult = self.pattern[i][0] + random.uniform(min_val, max_val)
                    yresult = self.pattern[i][1] + random.uniform(min_val, max_val)
                    result.append((xresult, yresult)) 
            elif axis == 'x=y':
                for i in range(len(self.pattern)):
                    randomvalue = random.uniform(min_val, max_val)
                    xresult = self.pattern[i][0] + randomvalue
                    yresult = self.pattern[i][1] + randomvalue
                    result.append((xresult, yresult)) 
        
        return Pattern(result)
    
    def RandomizeOrder(self):
        """
        Randomizes the order of the elements in the pattern.

        Returns
        -------
        Pattern:
            New Pattern object instance

        """
        idx = list(range(len(self.pattern)))
        random.shuffle(idx)
        
        result = []
        for i in range(len(self.pattern)):
            result.append(self.pattern[idx[i]])
        
        return Pattern(result)
    
    def _SetRandomizeAcrossElements(self):
        """
        Randomizes the order of the elements in the pattern.

        Returns
        -------
        Pattern:
            New Pattern object instance

        """        
        idx = list(range(len(self.pattern)))
        random.shuffle(idx)
        
        result = []
        for i in range(len(self.pattern)):
            result.append(self.pattern[idx[i]])
        
        return Pattern(result)
    
    def _SetRandomizeAcrossColumns(self, n_rows, n_cols):
        """
        Randomizes the order of the elements across the columns of the pattern.
        """   
   
        p = self.pattern
        result = []
        for row in range(n_rows):
            
            startindex = row * n_cols
            endindex = (row * n_cols) + n_cols
            rowvalues = p[startindex:endindex]
            
            idx = list(range(n_cols))
            random.shuffle(idx)
            
            for i in range(len(rowvalues)):
                result.append(rowvalues[idx[i]])
            
        return Pattern(result)
    
    def _SetRandomizeAcrossRows(self, n_rows, n_cols):
        """
        Randomizes the order of the elements across the rows of the pattern.
        """   
   
        p = self.pattern
        result = p.copy()
        for column in range(n_cols):
            
            indices = []
            for row in range(n_rows):
                indices.append(column + row * n_cols)
            
            idx = list(range(n_rows))
            random.shuffle(idx)
            
            for i in range(n_rows):
                value = p[indices[i]]
                result[indices[idx[i]]] = value
            
        return Pattern(result)
    
    def _SetRandomizeAcrossRightDiagonal(self, n_rows, n_cols):
        """
        Randomizes the order of the elements across the left diagonal of the pattern.
        """   
   
        p = self.pattern
        newp = p.copy()
        required_count = (n_rows + n_cols) - 1
        
        s = Pattern(list(range(required_count)))        
        shifted_pattern  = list(s.pattern[::-1])
        result = []
        for i in range(n_rows):
            result.extend(shifted_pattern[-n_cols:])
            shifted_pattern = [shifted_pattern[-1]] + shifted_pattern[:-1]          
        result = Pattern(result)
        
        for serie in range(required_count):
            
            indices = []
            for i in range(len(result.pattern)):
                if result.pattern[i] == serie:
                    indices.append(i)
                
            n_elements = len(indices)
                
            if n_elements > 1:
                
                idx = list(range(n_elements))
                random.shuffle(idx)
                
                for i in range(n_elements):
                    newp[indices[idx[i]]] = p[indices[i]]
            
        return Pattern(newp)        

    def _SetRandomizeAcrossLeftDiagonal(self, n_rows, n_cols):
        """
        Randomizes the order of the elements across the right diagonal of the pattern.
        """   
   
        p = self.pattern
        newp = p.copy()
        required_count = (n_rows + n_cols) - 1
        
        s = Pattern(list(range(required_count)))        
        shifted_pattern  = list(s.pattern)        
        result = []
        for i in range(n_rows):
            result.extend(shifted_pattern[:n_cols])
            shifted_pattern = shifted_pattern[1:]  + [shifted_pattern[0]]                    
        result = Pattern(result)
        
        for serie in range(required_count):
            
            indices = []
            for i in range(len(result.pattern)):
                if result.pattern[i] == serie:
                    indices.append(i)
                
            n_elements = len(indices)
                
            if n_elements > 1:
                
                idx = list(range(n_elements))
                random.shuffle(idx)
                
                for i in range(n_elements):
                    newp[indices[idx[i]]] = p[indices[i]]
            
        return Pattern(newp)   
    
    # def _SetRandomizeAcrossLayers(self, n_rows, n_cols):
    #     """
    #     Randomizes the order of the elements across the layers of the pattern.
    #     """   
   
    #     p = self.pattern
    #     # newp = p.copy()
    #     # minimal_n = min(n_rows, n_cols)
    #     # if minimal_n % 2 == 0: 
    #     #     n_layers = int(minimal_n / 2)
    #     # else:
    #     #     n_layers = int((minimal_n + 1 )/2)
        

    #     return Pattern(p) 
    
    def CreateGradientPattern(start_value, end_value, n_elements):
        """
        Private method for creating a list of gradient values, taking into account
        the type of start and end value.

        Parameters
        ----------
        start_value : string, int, float, or tuple
            Value for the first element in the list.
        end_value : string, int, float, or tuple
            Value for the last element in the list.
        n_elements : int
            Total number of elements in the list of gradient values.

        Returns
        -------
        Pattern : Pattern
            A list of size n_elements.

        """
        gradient = None
        if type(start_value) == str:
            gradient = Pattern.CreateColorRangeList(start_value, end_value, n_elements)
        elif type(start_value) == int or type(start_value) == float:
            gradient = Pattern.CreateNumberRangeList(start_value, end_value, n_elements)
        elif type(start_value) == tuple:
            gradient = Pattern.Create2DGradient(x = LinearGradient(start = start_value[0], end = end_value[0], n_elements = n_elements), 
                                                y = LinearGradient(start = start_value[1], end = end_value[1], n_elements = n_elements), 
                                                n_elements = n_elements)
        
        return Pattern(gradient)
    
    def CreateColorRangeList(start_color, end_color, n_elements):
        """
        Creates a range of colors.

        Parameters
        ----------
        start_color : string
            Name of the first color in the list.
        end_color : string
            Name of the final color in the list.
        n_elements : int
            Total number of colors in the list. Value must be >= 2.

        Returns
        -------
        color_range : list
            A list with hexadecimal color values.

        """
        start_color = colour.Color(start_color)
        end_color   = colour.Color(end_color)
        
        color_range = [c.hex for c in start_color.range_to(end_color, n_elements)]
        
        return color_range
    
    
    def CreateNumberRangeList(start_number, end_number, n_elements):
        """
        Creates a range of numbers, starting at start_number and ending with
        end_number (included). 

        Parameters
        ----------
        start_number : int or float
            First number in the list.
        end_number : int or float
            Final number in the list.
        n_elements : int
            Total number of elements in the list. Value must be >= 2.

        Returns
        -------
        number_range : list
            A range of numbers.

        """
        step_size = (end_number - start_number)/(n_elements-1)
        
        number_range = [start_number]
        for i in range(1,n_elements):
            number_range.append(number_range[-1] + step_size)
        
        return number_range
    
    def Create2DGradient(x, y, n_elements):
        """
        Creates a 2D gradient
        
        Parameters
        ----------
        x : list
            List of x coordinates (can also be a Sequence or LinearGradient)
        y : list
            List of y coordinates (can also be a Sequence or LinearGradient)
        n_elements : int
            Total number of elements in the list. 
        """
        result = []
        for i in range(n_elements):
            if isinstance(x, types.GeneratorType):
                x_i = next(x)
            else:
                x_i = x
            
            if isinstance(y, types.GeneratorType):
                y_i = next(y)
            else:
                y_i = y
                
            result.append((x_i, y_i))
            
        return result
        
        
def Sequence(start, step):
    """
    Creates a sequence based on a start value and a step size.
    
    Parameters
    ----------
    start : int or float
        Numeric start value.
    step : int or float
        Numeric step size.
    """
    i = start
    
    while True:
        yield i 
        i += step
        
def LinearGradient(start, end, n_elements, invert = False):
    """
    Creates a linear gradient based on a start value, an end value, and a number of elements.
    Parameters
    ----------
    start : int or float
        Numeric value for the first element in the list.
    end : list
        Numeric value for the last element in the list.
    n_elements : int
        Total number of elements in the list. 
    invert : Boolean
        Indicates whether the gradient needs to be inverted. Default is false.
    """
    
    if start > end:
        orig_start = start
        orig_end = end
        start = orig_end
        end = orig_start
        invert = True
        
    step_size = (end - start) / (n_elements - 1)
    
    if invert == True:
        current_number = end
    
        while current_number >= start:
            yield current_number
            current_number -= step_size
    else:
        current_number = start
    
        while current_number <= end:
            yield current_number
            current_number += step_size
        