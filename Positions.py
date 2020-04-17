# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 12:33:03 2020

@author: Christophe
"""

from BasicPattern import BasicPattern

class Positions:
    def Create2DGrid(n_rows, n_cols, row_spacing, col_spacing):
        x = BasicPattern(list(range(0, n_cols * col_spacing, col_spacing)))
        x.DuplicatePattern(n_cols)
        y = BasicPattern(list(range(0, n_cols * col_spacing, col_spacing)))
        y.DuplicateElements(n_rows)
    
        
        return (x, y)
        
    
        
    
    