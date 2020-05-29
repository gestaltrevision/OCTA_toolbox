"""
This module contains a base class with several essential functions for patterns.
More complex patterns (e.g., grid based patterns) can be derived from this class.
"""
import colour
import random

class Pattern:
    def __init__(self, pattern):
        """
        Initializes a Pattern object. If the provided input is not a list,
        the pattern will be initialized with a list that contains the provided
        input as the first and only element.

        Parameters
        ----------
        pattern : any type
            List object with initial values for the pattern.

        """
        if type(pattern) == list:
            self.pattern = pattern
        elif type(pattern) == Pattern:
            self.pattern = pattern.pattern
        else:
            self.pattern = [pattern]
        
        
    def __str__(self):
        """
        Creates a string representation of the pattern.

        Returns
        -------
        str
            String representation of the pattern.

        """
        return str(self.pattern)
    
    def __add__(self, o):
        """
        

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
            
            
        return Pattern(result)
            
            
    def RepeatPattern(self, n_repeats, max_elements = None):
        """
        Repeats the pattern as a whole.

        Parameters
        ----------
        n_duplications : int
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
        
        return Pattern(result)
    
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
        n_repeats = int(count/len(self.pattern)) + 1
        
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
        n_repeats = int(count/len(self.pattern)) + 1
        
        new_pattern = self.RepeatPattern(n_repeats, count)
        
        return new_pattern
            
    
    def AddNormalJitter(self, mu = 0, std = 1):
        """
        Adds a sample from a random normal distribution to each element in the pattern.

        Parameters
        ----------
        mu : float, optional
            Mean of the normal distribution. The default is 0.
        std : float, optional
            Standard deviation of the normal distribution. The default is 1.

        Returns
        -------
        Pattern:
            New Pattern object instance

        """
        result = []
        for i in range(len(self.pattern)):
            result.append(self.pattern[i] + random.normalvariate(mu, std))
        
        return Pattern(result)
    
    
    def AddUniformJitter(self, min_val = -1, max_val = 1):
        """
        Adds a sample from a uniform distribution to each element in the pattern.

        Parameters
        ----------
        min_val : float, optional
            Lower bound of the uniform distribution
        max_val : float, optional
            Upper bound of the uniform distribution

        Returns
        -------
        Pattern:
            New Pattern object instance

        """
        result = []
        for i in range(len(self.pattern)):
            result.append(self.pattern[i] + random.uniform(min_val, max_val))
        
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
        
            
    def SwapElements(self, n_swap_pairs = 1):
        """
        Swaps the values of two positions in the pattern. Once a position has
        been used in a swap, it will not be used again in additional swaps. 
        As a consequence, the maximum number of possible swaps is N//2, where
        N is the number of elements in the pattern.
        
        When doing multiple swaps, if two elements have been selected to be
        swapped around a first time, they will not be selected again. This
        means that subsequent swaps can never cancel out an initial swap
        
        Parameters
        ----------
        n_swap_pairs: int 
            Number of element pairs that will be swapped. Maximum value
            is half the number of elements in the Pattern.

        Returns
        -------
        Pattern:
            New Pattern object instance

        """
        assert len(self.pattern) >= n_swap_pairs * 2, 'Maximal number of swaps possible is %d, but %d were requested'%(len(self.pattern)//2, n_swap_pairs)
               
        # 1. Generate all available swap positions
        candidate_swap_positions = set()
        for i in range(len(self.pattern)):
            for j in range(i+1, len(self.pattern)):
                candidate_swap_positions.add((i,j))
            
        # 2. Select the required number of swap positions
        selected_swap_pairs = []
        for i in range(n_swap_pairs):
            selected_pair = random.sample(candidate_swap_positions, 1)[0]
            print(selected_pair)
            selected_swap_pairs.append(selected_pair)
            
            removable_positions = set()
            for p in candidate_swap_positions:
                if selected_pair[0] in p or selected_pair[1] in p:
                    removable_positions.add(p)
                    
            candidate_swap_positions.difference_update(removable_positions)
            
        # 3. Perform the swap
        result = list(self.pattern)
        for swap_pair in selected_swap_pairs:
            result[swap_pair[0]], result[swap_pair[1]] = result[swap_pair[1]], result[swap_pair[0]]
        
        return Pattern(result)
    
    
    def CreateGradientPattern(start_value, end_value, n_elements):
        """
        Private method for creating a list of gradient values, taking into account
        the type of start and end value.

        Parameters
        ----------
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
        
        return Pattern(gradient)
    
    def CreateColorRangeList(start_colour, end_colour, n_elements):
        """
        Creates a range of colors.

        Parameters
        ----------
        start_colour : string
            Name of the first color in the list.
        end_colour : string
            Name of the final color in the list.
        n_elements : TYPE
            Total number of colors in the list. Value must be >= 2.

        Returns
        -------
        colour_range : list
            A list with hexadecimal color values.

        """
        start_colour = colour.Color(start_colour)
        end_colour   = colour.Color(end_colour)
        
        colour_range = [c.hex for c in start_colour.range_to(end_colour, n_elements)]
        
        return colour_range
    
    
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
            Total number of numbers in the list. Value must be >= 2.

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
    