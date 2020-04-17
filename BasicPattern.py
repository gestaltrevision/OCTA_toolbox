"""
This module contains a base class with several essential functions for patterns.
More complex patterns (e.g., grid based patterns) can be derived from this class.
"""
import colour

class BasicPattern:
    def __init__(self, pattern):
        """
        Initialises a BasicPattern object

        Parameters
        ----------
        pattern : list
            List object with initial values for the pattern.

        """
        assert type(pattern) == list, "BasicPattern needs to be initialized with a list"
        self.pattern = pattern
        
        
    def __str__(self):
        """
        Creates a string representation of the pattern

        Returns
        -------
        str
            String representation of the pattern.

        """
        return str(self.pattern)
    
    
    def DuplicateElements(self, n_duplications, max_elements = None):
        """
        Duplicates each element in the pattern

        Parameters
        ----------
        n_duplications : int
            How many times each elements needs to be duplicated.
        max_elements : int, optional
            Maximum number of elements in the resulting pattern. The default is None.

        Returns
        -------
        BasicPattern
            Current instance of BasicPattern.
            
        Examples
        --------
        initial pattern:
            [1, 2, 3]
        n_duplications:
            3
        resulting pattern:
            [1, 1, 1, 2, 2, 2, 3, 3, 3]
        """
        duplicated_list = []
        for el in self.pattern:
            duplicated_list.extend([el]*n_duplications)
        
        self.pattern = duplicated_list
        if max_elements != None:
            self.pattern = duplicated_list[:max_elements]
            
        return self
            
            
    def DuplicatePattern(self, n_duplications, max_elements = None):
        """
        Repeats the pattern as a whole.

        Parameters
        ----------
        n_duplications : int
            How many times the pattern needs to be duplicated.
        max_elements : int, optional
            Maximum number of elements in the resulting pattern. The default is None.

        Returns
        -------
        BasicPattern
            Current instance of BasicPattern

        """
        duplicated_list = []
        
        for i in range(n_duplications):
            duplicated_list.extend(self.pattern)
        
        self.pattern = duplicated_list
        if max_elements != None:
            self.pattern = duplicated_list[:max_elements]
            
        return self
    
    def DuplicateElementsToSize(self, count):
        """
        Duplicates the number of elements in the pattern until the total pattern length
        is equal or exceeds to the requested count. If the total pattern length exceeds the count,
        the pattern is truncated

        Parameters
        ----------
        count : int
            Required number of elements in the pattern.

        Returns
        -------
        BasicPattern
            Current instance of BasicPattern

        """
        n_duplications = int(count/len(self.pattern)) + 1
        self.DuplicateElements(n_duplications, count)
        
        return self
        
    def DuplicatePatternToSize(self, count):
        """
        Duplicates the pattern until the total pattern length is equal to or exceeds
        the requested count. If the total pattern length exceeds the count, the pattern
        is truncated

        Parameters
        ----------
        count : int
            Required number of elements in thep pattern

        Returns
        -------
        BasicPattern
            Current instance of BasicPattern

        """
        n_duplications = int(count/len(self.pattern)) + 1
        self.DuplicatePattern(n_duplications, count)
        
        return self
            
    def CreateColorRangeList(start_colour, end_colour, n_elements):
        """
        Creates a range of colours

        Parameters
        ----------
        start_colour : string
            Name of the first colour in the list.
        end_colour : string
            Name of the final color in the list.
        n_elements : TYPE
            Total amount of colours in the list. Value must be >= 2

        Returns
        -------
        colour_range : list
            A list with hexadecimal colour values.

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
            Total amount of numbers in the list. Value must be >= 2

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
            
    

if __name__ == '__main__':
    # 1. Demonstrating duplicate elements
    p = BasicPattern([1,2,3]).DuplicateElements(3)
    print("Duplicating elements: ")
    print(p)
    print("\n\n")
    
    # 2. Demonstrating duplicate pattern
    p = BasicPattern([1,2,3]).DuplicatePattern(3)
    print("Duplicating Pattern: ")
    print(p)
    print("\n\n")
    
    # 3. Demonstration colour range
    p = BasicPattern(BasicPattern.CreateColorRangeList("red", "green", 5))
    print("Creating colour range: ")
    print(p)
    print("\n\n")
    
    # 4. Demonstrating number range
    p = BasicPattern(BasicPattern.CreateNumberRangeList(1, 10, 4))
    print("Creating number range: ")
    print(p)
    print("\n\n")