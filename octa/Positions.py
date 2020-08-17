# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 12:33:03 2020

@author: Christophe
"""
import numpy as np
import random

from .patterns.Pattern import Pattern

class Positions:
    """
    The Positions object contains two Pattern objects for each of the
    x and y coordinates.
    
    Getters are defined to immediately access the values in the Pattern
    objects.
    
    Static methods are defined for generating template position structures
    
    Parameters
    ----------
    x : Pattern
        Object that contains the values for the x-coordinates
    y : Pattern
        Object that contains the values for the y-coordinates
    """
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._randomization = None
        self._randomization_parameters = {}
        
    @property
    def x(self):
        """
        Returns the values in the x Pattern

        Returns
        -------
        List
            List with values for the x coordinate.

        """
        return self._x.pattern
    
    @property
    def y(self):
        """
        Returns the values in the y Pattern

        Returns
        -------
        List
            List with values for the y coordinate.

        """
        return self._y.pattern
    
    def GetPositions(self):
        position_jitter = self._CalculateLocationJitter()
        
        x = list(self._x.pattern)
        y = list(self._y.pattern)
        
        for i in range(len(position_jitter['x'])):
            x[i] += position_jitter['x'][i]
        
        for i in range(len(position_jitter['y'])):
            y[i] += position_jitter['y'][i]
        
        return (x, y)
    
    def SetLocationJitter(self, axis = "xy", distribution = "normal", **kwargs):
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
                
            self._randomization = 'normal'
            self._randomization_parameters = {'mu' : mu, 'std' : std, 'axis' : axis}
                
        if distribution == 'uniform':
            min_val = -1
            max_val =  1
            
            if 'min_val' in kwargs.keys():
                min_val = kwargs['min_val']
            if 'max_val' in kwargs.keys():
                max_val = kwargs['max_val']
            
            self._randomization = 'uniform'
            self._randomization_parameters = {'min_val' : min_val, 'max_val' : max_val, 'axis' : axis}
                                       
        return self
    
    
    def _CalculateLocationJitter(self):
        x_jitter = [0 for _ in range(len(self._x.pattern))]
        y_jitter = [0 for _ in range(len(self._y.pattern))]
            
        if self._randomization == "normal":
            if 'x' in self._randomization_parameters['axis']:
                x_jitter = [random.normalvariate(self._randomization_parameters['mu'], self._randomization_parameters['std']) for _ in range(len(self._x.pattern))]
            if 'y' in self._randomization_parameters['axis']:
                y_jitter = [random.normalvariate(self._randomization_parameters['mu'], self._randomization_parameters['std']) for _ in range(len(self._y.pattern))]
                
        elif self._randomization == "uniform":
            if 'x' in self._randomization_parameters['axis']:
                x_jitter = [random.uniform(self._randomization_parameters['min_val'], self._randomization_parameters['max_val']) for _ in range(len(self._x.pattern))]
            if 'y' in self._randomization_parameters['axis']:
                y_jitter = [random.uniform(self._randomization_parameters['min_val'], self._randomization_parameters['max_val']) for _ in range(len(self._y.pattern))]
        
        return {'x' : x_jitter, 'y' : y_jitter}
            
        
    def Create2DGrid(n_rows, n_cols, row_spacing = 50, col_spacing= 50):
        """
        Static method for creates a 2D grid structure.

        Parameters
        ----------
        n_rows : int
            Number of rows.
        n_cols : int
            Numbr of columns.
        row_spacing : int
            Distance between column centers. The default is 50.
        col_spacing : int
            Distance between row centers. The default is 50.

        Returns
        -------
        x : Pattern
            All the x-coordinates.
        y : Pattern
            All the y-coordinates.

        """
        x = Pattern(list(range(0, n_cols * col_spacing, col_spacing)))
        x = x.RepeatPattern(n_rows)
        y = Pattern(list(range(0, n_rows * row_spacing, row_spacing)))
        y = y.RepeatElements(n_cols)    
        
        return Positions(x, y)
        
    
    def CreateSineGrid(n_rows, n_cols, row_spacing, col_spacing, A = 1, f = 1, axis = "x"):
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
        A : TYPE, float
            Amplitude of the modulation.
        f : TYPE, float
            Frequency of the modulation.

        Returns
        -------
        x : Pattern
            All the x-coordinates.
        y : Pattern
            All the y-coordinates.

        """
        x = Pattern(list(range(0, n_cols * col_spacing , col_spacing)))
        x = x.RepeatPattern(n_rows)
        
        y = Pattern(list(range(0, n_rows * row_spacing , row_spacing)))
        y = y.RepeatElements(n_cols)    
                
        if axis == "x":
            y_mod = Pattern( list(A*np.sin(2*np.pi*f*np.array(range(n_cols)))))
            y_mod = y_mod.RepeatPattern(n_rows)
            
            return Positions(x, y + y_mod)
        elif axis == "y":
            x_mod = Pattern( list(A*np.sin(2*np.pi*f*np.array(range(n_rows)))))
            x_mod = x_mod.RepeatElements(n_cols)
            
            return Positions(x + x_mod, y)
        else:
            y_mod = Pattern( list(A*np.sin(2*np.pi*f*np.array(range(n_cols)))))
            y_mod = y_mod.RepeatPattern(n_rows)
            x_mod = Pattern( list(A*np.sin(2*np.pi*f*np.array(range(n_rows)))))
            x_mod = x_mod.RepeatElements(n_cols)
            
            return Positions(x + x_mod, y + y_mod)
    
    def CreateCircle(radius, n_elements):
        """
        Generates element positions on the circumference of a regularly spaced
        circle.

        Parameters
        ----------
        radius : float
            Radius of the circle.
        n_elements : int
            Number of elements on the circle.

        Returns
        -------
        x : Pattern
            All the x-coordinates.
        y : Pattern
            All the y-coordinates.

        """
        idx = np.deg2rad(np.linspace(0, 360, n_elements+1))
        x   = Pattern(list( (radius * np.cos(idx)))[0:n_elements])
        y   = Pattern(list( (radius * np.sin(idx)))[0:n_elements])
        
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
        
        x = Pattern(list( p[0] for p in positions))
        y = Pattern(list( p[1] for p in positions))
        
        return Positions(x, y)
                       

    
if __name__ == '__main__':
    positions = Positions.CreateSineGrid(3, 5, 50, 50, A = 50, f = 1/250)
    print(positions.x)
    print(positions.y)
        
    