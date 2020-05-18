# -*- coding: utf-8 -*-
"""
Created on Mon May 18 14:40:15 2020

@author: Christophe
"""


from .BasicPattern import BasicPattern

class GridPattern(BasicPattern):
    def __init__(self, pattern, n_rows, n_cols, style = "element"):
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