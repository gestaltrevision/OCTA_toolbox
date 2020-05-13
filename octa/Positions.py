# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 12:33:03 2020

@author: Christophe
"""
import numpy as np

from .patterns.BasicPattern import BasicPattern

class Positions:
    """
    The Positions object contains two BasicPattern objects for each of the
    x and y coordinates.
    
    Getters are defined to immediately access the values in the BasicPattern
    objects.
    
    Static methods are defined for generating template position structures
    
    Parameters
    ----------
    x : BasicPattern
        Object that contains the values for the x-coordinates
    y : BasicPattern
        Object that contains the values for the y-coordinates
    """
    def __init__(self, x, y):
        self._x = x
        self._y = y
        
    @property
    def x(self):
        """
        Returns the values in the x BasicPattern

        Returns
        -------
        List
            List with values for the x coordinate.

        """
        return self._x.pattern
    
    @property
    def y(self):
        """
        Returns the values in the y BasicPattern

        Returns
        -------
        List
            List with values for the y coordinate.

        """
        return self._y.pattern
    
    def JitterLocations(self, axis = "xy", distribution = "normal", **kwargs):
        """
        Add jitter to the positions.

        Parameters
        ----------
        axis : str, optional
            String that contains the axis to which jitter should be applied.
            Possible values are "x", "y", or "xy". The default is "xy".
            
        distribution : str, optional
            The type of jitter that should be used. The default is "normal".
            
        **kwargs : Additional arguments that depend on the requested jitter type:
            "normal": Specify 'mu' and 'std'
            
            "uniform": Specify 'min_val' and 'max_val'

        Returns
        -------
        Positions
            The updated Positions object.

        """
        if distribution == 'normal':
            mu = 0
            if 'mu' in kwargs.keys():
                mu = kwargs['mu']
            
            std = 1
            if 'std' in kwargs.keys():
                std = kwargs['std']
            
            if 'x' in axis:
                self._x.AddNormalJitter(mu, std)
            if 'y' in axis:
                self._y.AddNormalJitter(mu, std)
                
        if distribution == 'uniform':
            min_val = -1
            max_val =  1
            
            if 'min_val' in kwargs.keys():
                min_val = kwargs['min_val']
            if 'max_val' in kwargs.keys():
                max_val = kwargs['max_val']
                
            if 'x' in axis:
                self._x.AddUniformJitter(min_val, max_val)
            if 'y' in axis:
                self._y.AddUniformJitter(min_val, max_val)
                
        return self
        
    def Create2DGrid(n_rows, n_cols, row_spacing, col_spacing, x_offset = 0, y_offset = 0):
        """
        Static method for creates a 2D grid structure.

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
        
        return Positions(x, y)
        
    
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
        
        return Positions(x, y + y_mod)

    
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
        
        return Positions(x, y)
    
    def CreateRandomPattern(n_elements, width = 256, height = 256, min_distance = 30, max_iterations = 10):
        """
        Generates random (x,y) positions

        Parameters
        ----------
        n_elements : int
            The number of random positions.
        width : int, optional
            The width of the stimulus. The default is 256.
        height : int, optional
            The height of the stimulus. The default is 256.
        min_distance : int, optional
            Minimum distance between all generated positions. The default is 30.
        max_iterations : int, optional
            How many times the algorithm should try to generate positions if
            the min_distance criterion can not be satisfied. The default is 10.

        Returns
        -------
        Positions
            Positions object with the generated (x,y) positions.

        """
        outer_iteration_count = 0
        all_elements_valid = False
        
        while all_elements_valid == False and outer_iteration_count < max_iterations:
            positions = []
            
            # Start generating new positions
            for i in range(n_elements):
                valid_point = False
                inner_iteration_count = 0
                
                # Check if the new position is sufficiently separated from previous ones
                while valid_point == False and inner_iteration_count < max_iterations:                  
                    x = np.random.randint(0, width)
                    y = np.random.randint(0, height)
                    
                    valid_point = True
                    for p in positions:
                        if ((p[0] - x)**2 + (p[1] - y)**2)**0.5 < min_distance:
                            valid_point = False
                            break
                        
                    inner_iteration_count += 1
                        
                if valid_point:
                    positions.append((x, y))
                else:
                    break
                    
            if len(positions) == n_elements:
                all_elements_valid = True
                
            outer_iteration_count += 1
            
        assert all_elements_valid, "CreateRandomPattern failed to produce %d elements with a minimum distance %d\n. Try changin the max_iterations, or decrease the number of elements and/or minimum distance."%(n_elements, min_distance)
        
        x = BasicPattern(list( p[0] for p in positions))
        y = BasicPattern(list( p[1] for p in positions))
        
        return Positions(x, y)
                       

    
if __name__ == '__main__':
    positions = Positions.CreateSineGrid(3, 5, 50, 50, A = 50, f = 1/250)
    print(positions.x)
    print(positions.y)
        
    