# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 12:33:03 2020

@author: Christophe
"""
import numpy as np

from BasicPattern import BasicPattern

class Positions:
    def Create2DGrid(n_rows, n_cols, row_spacing, col_spacing, x_offset = 0, y_offset = 0):
        """
        Creates a 2D regularly spaced grid.

        Parameters
        ----------
        n_rows : int
            Number of rows.
        n_cols : int
            Numbr of columns.
        row_spacing : int
            Distance between column centers.
        col_spacing : int
            Distance between row centers.
        x_offset : int, optional
            x position offset for all elements. The default is 0.
        y_offset : int, optional
            y position offset for all elements. The default is 0.

        Returns
        -------
        x : BasicPattern
            All the x-coordinates.
        y : BasicPattern
            All the y-coordinates.

        """
        x = BasicPattern(list(range(x_offset, n_cols * col_spacing + (x_offset), col_spacing)))
        x.DuplicatePattern(n_rows)
        y = BasicPattern(list(range(y_offset, n_rows * row_spacing + (y_offset), row_spacing)))
        y.DuplicateElements(n_cols)    
        
        return (x, y)
        
    
    def CreateSineGrid(n_rows, n_cols, row_spacing, col_spacing, x_offset = 0, y_offset = 0, A = 1, f = 1):
        """
        Creates a 2D regularly spaced grid and adds a sine wave modulation to the y-axis.

        Parameters
        ----------
        n_rows : int
            Number of rows.
        n_cols : int
            Number of columns.
        row_spacing : int
            Distance between column centers.
        col_spacing : int
            Distance between row centers.
        x_offset : int, optional
            x position offset for all elements. The default is 0.
        y_offset : int, optional
            y position offset for all elements. The default is 0.
        A : TYPE, float
            Amplitude of the modulation.
        f : TYPE, float
            Frequency of the modulation.

        Returns
        -------
        x : BasicPattern
            All the x-coordinates.
        y : BasicPattern
            All the y-coordinates.

        """
        x = BasicPattern(list(range(x_offset, n_cols * col_spacing + (x_offset), col_spacing)))
        x.DuplicatePattern(n_rows)
        
        y = BasicPattern(list(range(y_offset, n_rows * row_spacing + (y_offset), row_spacing)))
        y.DuplicateElements(n_cols)    
                
        y_mod = BasicPattern( list(A*np.sin(2*np.pi*f*np.array(range(n_cols)))))
        y_mod.DuplicatePattern(n_rows)
        
        return (x, y + y_mod)
    
    def CreateCircle(radius, n_elements, x_offset = 0, y_offset = 0):
        """
        Generates element positions on the circumference of a regularly spaced
        circle.

        Parameters
        ----------
        radius : float
            Radius of the circle.
        n_elements : int
            Number of elements on the circle.
        x_offset : int, optional
            x position offset for all elements. The default is 0.
        y_offset : int, optional
            y position offset for all elements. The default is 0.

        Returns
        -------
        x : BasicPattern
            All the x-coordinates.
        y : BasicPattern
            All the y-coordinates.

        """
        idx = np.deg2rad(np.linspace(0, 360, n_elements+1))
        x   = BasicPattern(list( (radius * np.cos(idx)) + (x_offset))[0:n_elements])
        y   = BasicPattern(list( (radius * np.sin(idx)) + (y_offset))[0:n_elements])
        
        return (x, y)
    
if __name__ == '__main__':
    (x,y) = Positions.CreateSineGrid(3, 5, 50, 50, A = 50, f = 1/250)
    print(x.pattern)
    print(y.pattern)
        
    