# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 12:33:03 2020

@author: Christophe
"""
import numpy as np
import random
# from IPython.display import SVG, display
import svgpathtools
# import svgwrite

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
    def __init__(self, x, y, positiontype = None, positionparameters = {}):
        self._x = x
        self._y = y
        self._position_type = positiontype  
        self._position_parameters = positionparameters
        self._deviation = None
        self._deviation_parameters = {}
        self._jitter = None
        self._jitter_parameters = {}
        
    @property
    def x(self):
        """
        Returns the values in the x Pattern

        Returns
        -------
        List
            List with values for the x coordinate.

        """
        # position_jitter = self._CalculatePositionJitter()
        # position_deviations = self._CalculatePositionDeviations()
        
        x = list(self._x.pattern)
        
        # for i in range(len(position_deviations['x'])):
        #     x[i] += position_deviations['x'][i]
        
        # for i in range(len(position_jitter['x'])):
        #     x[i] += position_jitter['x'][i]
            
        return x
    
    @property
    def y(self):
        """
        Returns the values in the y Pattern

        Returns
        -------
        List
            List with values for the y coordinate.

        """
        # position_jitter = self._CalculatePositionJitter()
        # position_deviations = self._CalculatePositionDeviations()
        
        y = list(self._y.pattern)
        
        # for i in range(len(position_deviations['y'])):
        #     y[i] += position_deviations['y'][i]
        
        # for i in range(len(position_jitter['y'])):
        #     y[i] += position_jitter['y'][i]

        return y
        
    def GetPositions(self):
        position_jitter = self._CalculatePositionJitter()
        position_deviations = self._CalculatePositionDeviations()
        
        x = list(self._x.pattern)
        y = list(self._y.pattern)
        
        for i in range(len(position_deviations['x'])):
            x[i] += position_deviations['x'][i]
        
        for i in range(len(position_deviations['y'])):
            y[i] += position_deviations['y'][i]
        
        for i in range(len(position_jitter['x'])):
            x[i] += position_jitter['x'][i]
        
        for i in range(len(position_jitter['y'])):
            y[i] += position_jitter['y'][i]
        
        return (x, y)
    
    def SetPositionDeviations(self, element_id = [0], x_offset = None, y_offset = None):
        """
        Add deviations to the positions.

        Parameters
        ----------

        Returns
        -------
        Positions
            The updated Positions object.

        """  
        assert type(element_id) == list or type(element_id) == int, "Element id must be int or list"
        assert type(x_offset) == list or type(x_offset) == int, "X offset must be int or list"
        assert type(y_offset) == list or type(y_offset) == int, "Y offset must be int or list"
        
        if type(element_id) == int:
            element_id = [element_id]
            
        if type(x_offset) == int:
            x_offset = [x_offset]*len(element_id)
            
        if type(y_offset) == int:
            y_offset = [y_offset]*len(element_id)
            
        if type(element_id) == list:
            assert len(element_id) == len(x_offset) or len(element_id) == len(y_offset), "Length of offset list and length of element_id list should be equal"
            
        self._deviation = True
        self._deviation_parameters = {'element_id' : element_id, 'x_offset' : x_offset, 'y_offset' : y_offset}
                                       
        return self
    
    def _CalculatePositionDeviations(self):
        x_deviations = [0 for _ in range(len(self._x.pattern))]
        y_deviations = [0 for _ in range(len(self._y.pattern))]
            
        if self._deviation == True:
            if self._deviation_parameters['x_offset'] is not None:
                for i in range(len(self._deviation_parameters['element_id'])):
                    x_deviations[self._deviation_parameters['element_id'][i]] = self._deviation_parameters['x_offset'][i]
            if self._deviation_parameters['y_offset'] is not None:
                for i in range(len(self._deviation_parameters['element_id'])):
                    y_deviations[self._deviation_parameters['element_id'][i]]  = self._deviation_parameters['y_offset'][i]
                    
        return {'x' : x_deviations, 'y' : y_deviations}
    
    def SetPositionJitter(self, axis = "xy", distribution = "normal", **kwargs):
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
                
            self._jitter = 'normal'
            self._jitter_parameters = {'mu' : mu, 'std' : std, 'axis' : axis}
                
        if distribution == 'uniform':
            min_val = -1
            max_val =  1
            
            if 'min_val' in kwargs.keys():
                min_val = kwargs['min_val']
            if 'max_val' in kwargs.keys():
                max_val = kwargs['max_val']
            
            self._jitter = 'uniform'
            self._jitter_parameters = {'min_val' : min_val, 'max_val' : max_val, 'axis' : axis}
                                       
        return self
    
    
    def _CalculatePositionJitter(self):
        x_jitter = [0 for _ in range(len(self._x.pattern))]
        y_jitter = [0 for _ in range(len(self._y.pattern))]
            
        if self._jitter == "normal":
            if self._jitter_parameters['axis'] == 'xy':
                x_jitter = [random.normalvariate(self._jitter_parameters['mu'], self._jitter_parameters['std']) for _ in range(len(self._x.pattern))]
                y_jitter = [random.normalvariate(self._jitter_parameters['mu'], self._jitter_parameters['std']) for _ in range(len(self._y.pattern))]
            elif self._jitter_parameters['axis'] == 'x=y':   
                x_jitter = [random.normalvariate(self._jitter_parameters['mu'], self._jitter_parameters['std']) for _ in range(len(self._x.pattern))]
                y_jitter = x_jitter
            elif self._jitter_parameters['axis'] == 'x':
                x_jitter = [random.normalvariate(self._jitter_parameters['mu'], self._jitter_parameters['std']) for _ in range(len(self._x.pattern))]
            elif self._jitter_parameters['axis'] == 'y':
                y_jitter = [random.normalvariate(self._jitter_parameters['mu'], self._jitter_parameters['std']) for _ in range(len(self._y.pattern))]
                
        elif self._jitter == "uniform":
            if self._jitter_parameters['axis'] == 'xy':
                x_jitter = [random.uniform(self._jitter_parameters['min_val'], self._jitter_parameters['max_val']) for _ in range(len(self._x.pattern))]
                y_jitter = [random.uniform(self._jitter_parameters['min_val'], self._jitter_parameters['max_val']) for _ in range(len(self._y.pattern))]
            elif self._jitter_parameters['axis'] == 'x=y':
                x_jitter = [random.uniform(self._jitter_parameters['min_val'], self._jitter_parameters['max_val']) for _ in range(len(self._x.pattern))]
                y_jitter = x_jitter        
            elif self._jitter_parameters['axis'] == 'x':
                x_jitter = [random.uniform(self._jitter_parameters['min_val'], self._jitter_parameters['max_val']) for _ in range(len(self._x.pattern))]
            elif self._jitter_parameters['axis'] == 'y':
                y_jitter = [random.uniform(self._jitter_parameters['min_val'], self._jitter_parameters['max_val']) for _ in range(len(self._y.pattern))]
        
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
        
        positiontype = "2DGrid"
        positionparameters = {'n_rows' : n_rows, 'n_cols' : n_cols, 'row_spacing' : row_spacing, 'col_spacing' : col_spacing}
        
        return Positions(x, y, positiontype, positionparameters)
    
    def CreateCustomPositions(x, y):
        """
        Static method for creates a 2D grid structure.

        Parameters
        ----------
        x : Pattern
            All the x-coordinates.
        y : Pattern
            All the y-coordinates.

        Returns
        -------
        x : Pattern
            All the x-coordinates.
        y : Pattern
            All the y-coordinates.

        """
        x = Pattern(list(x))
        y = Pattern(list(y))   
        
        positiontype = "CustomPositions"
        positionparameters = {'x': x, 'y': y}
        
        return Positions(x, y, positiontype, positionparameters)
        
    
    def CreateSineGrid(n_rows, n_cols, row_spacing = 50, col_spacing = 50, A = 25, f = .1, axis = "x"):
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
        
        positiontype = "SineGrid"
        positionparameters = {'n_rows' : n_rows, 'n_cols' : n_cols, 'row_spacing' : row_spacing, 
                              'col_spacing' : col_spacing, 'A' :  A, 'f' : f, 'axis' : axis}
                
        if axis == "x":
            y_mod = Pattern( list(A*np.sin(2*np.pi*f*np.array(range(n_cols)))))
            y_mod = y_mod.RepeatPattern(n_rows)
            
            return Positions(x, y + y_mod, positiontype, positionparameters)
        elif axis == "y":
            x_mod = Pattern( list(A*np.sin(2*np.pi*f*np.array(range(n_rows)))))
            x_mod = x_mod.RepeatElements(n_cols)
            
            return Positions(x + x_mod, y, positiontype, positionparameters)
        else:
            y_mod = Pattern( list(A*np.sin(2*np.pi*f*np.array(range(n_cols)))))
            y_mod = y_mod.RepeatPattern(n_rows)
            x_mod = Pattern( list(A*np.sin(2*np.pi*f*np.array(range(n_rows)))))
            x_mod = x_mod.RepeatElements(n_cols)
            
            return Positions(x + x_mod, y + y_mod, positiontype, positionparameters)
    
    def CreateCircle(radius, n_elements, starting_point = "left"):
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
        if starting_point == "left":
            idx = np.deg2rad(np.linspace(-180, 180, n_elements+1))
        elif starting_point == "top":
            idx = np.deg2rad(np.linspace(-90, 270, n_elements+1))
        elif starting_point == "right":
            idx = np.deg2rad(np.linspace(0, 360, n_elements+1))
        else: # starting_point == "bottom": 
            idx = np.deg2rad(np.linspace(-270, 90, n_elements+1))
            
        x   = Pattern(list( (radius * np.cos(idx)))[0:n_elements])
        y   = Pattern(list( (radius * np.sin(idx)))[0:n_elements])
        
        positiontype = "Circle"
        positionparameters = {'radius' : radius, 'n_elements' :  n_elements, 'starting_point' : starting_point}
        
        return Positions(x, y, positiontype, positionparameters)
    
    def CreateShape(n_elements, src = None, path = None, width = 300, height = 300):
        """
        Generates element positions on the circumference of a custom shape (path) in an equally spaced way.

        Parameters
        ----------
        n_elements : int
            Number of elements on the circle.

        Returns
        -------
        x : Pattern
            All the x-coordinates.
        y : Pattern
            All the y-coordinates.

        """
        if(src is not None):
            paths, attributes = svgpathtools.svg2paths(src)    
        else:
            paths = svgpathtools.parse_path(path)
        
        n_paths = len(paths)
        allpaths = []
        
        for i in range(0,n_paths):
            mypath = paths[i]
            xmin, xmax, ymin, ymax = mypath.bbox()
            xsize = xmax - xmin
            ysize = ymax - ymin
            allpaths.append([xsize, ysize])
            
        max_xsize = max([item[0] for item in allpaths])
        max_ysize = max([item[1] for item in allpaths])
        scale_x_parameter = width / max_xsize
        scale_y_parameter = height / max_ysize        

        step_size = float(1 / n_elements)
        
        xpositions = []
        ypositions = []
        
        for n in range(n_elements):
            coords = paths[0].point(step_size * n)
            x,y = str(coords).replace("(", "").replace(")", "").replace("j", "").split("+")
            xpositions.append(float(x))
            ypositions.append(float(y))
                
        x = Pattern(list( [xposition*scale_x_parameter for xposition in xpositions] ))
        y = Pattern(list( [yposition*scale_y_parameter for yposition in ypositions] ))
    
        # idx = np.deg2rad(np.linspace(0, 360, n_elements+1))
        # x   = Pattern(list( (radius * np.cos(idx)))[0:n_elements])
        # y   = Pattern(list( (radius * np.sin(idx)))[0:n_elements])

        positiontype = "Shape"
        positionparameters = {'n_elements' : n_elements, 'src' : src, 'path' : path, 'width' : width, 'height' : height}
        
        return Positions(x, y, positiontype, positionparameters)
    
    def CreateRandomPositions(n_elements, width = 300, height = 300, min_distance = 30, max_iterations = 10):
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
            
        assert all_elements_valid, "CreateRandomPositions failed to produce %d elements with a minimum distance %d\n. Try changin the max_iterations, or decrease the number of elements and/or minimum distance."%(n_elements, min_distance)
        
        x = Pattern(list( p[0] for p in positions))
        y = Pattern(list( p[1] for p in positions))
        
        positiontype = "RandomPositions"
        positionparameters = {'n_elements' : n_elements, 'width' : width, 'height' : height,
                              'min_distance' :  min_distance, 'max_iterations' : max_iterations}
        
        return Positions(x, y, positiontype, positionparameters)
                       

    
if __name__ == '__main__':
    positions = Positions.CreateSineGrid(3, 5, 50, 50, A = 50, f = 1/250)
    print(positions.x)
    print(positions.y)
        
    