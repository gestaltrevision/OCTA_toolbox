# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 12:59:09 2020

@author: u0072088
"""
import svgwrite
import random
import json
import jsonpickle
import pandas as pd
from collections import defaultdict

from IPython.display import SVG, display

from .Positions import Positions
from .patterns.GridPattern import Pattern, RepeatElements
from .shapes.Rectangle import Rectangle

class Stimulus:
    """ Container class for creating a stimulus.
    
    """
    
    def __init__(self, width = 512, height = 512, background_color = "white"):
        """
        Instantiates a stimulus object.

        Parameters
        ----------
        width : INT, optional
            Width of the stimulus. The default is 512.
        height : INT, optional
            Height of the stimulus. The default is 512.
        background_color : STRING, optional
            Background color of the stimulus. The default is "white".

        Returns
        -------
        None.

        """
        # Assign provided parameters
        self.width = width
        self.height = height
        self.background_color = background_color
        
        # Set initial shape parameters to zero
        self.positions   = None
        # self.__size        = None
        # self.__shapes      = None
        # self.__colour      = None
        # self.__orientation = None
        # self.__data        = None
        
        self.dwg_elements = None
        self.dwg = None
    
    def SaveSVG(self, filename):
        """
        Saves the current stimulus as an SVG file.

        Parameters
        ----------
        filename : STRING
            Name of the svg file.

        Returns
        -------
        None.

        """
        self.dwg.saveas('%s.svg'%filename , pretty = True)
        
        
    def SaveJSON(self, filename):
        """
        Saves the current stimulus as a JSON file.

        Parameters
        ----------
        filename : STRING
            Name of the json file.

        Returns
        -------
        None.

        """
        json_filename = "%s.json"%filename
        
        json_data = {'stimulus' : {'width':            self.width,
                                   'height':           self.height,
                                   'background_color': self.background_color,
                                   'positions'    :    jsonpickle.encode(self.positions),
                                   'size'         :    jsonpickle.encode(self.size),
                                   'shapes'       :    jsonpickle.encode(self.shapes),
                                   'colour'       :    jsonpickle.encode(self.colour),
                                   'orientation'  :    jsonpickle.encode(self.orientation),
                                   'data'         :    jsonpickle.encode(self.data)}}
                     #'dwg_elements'  : self.dwg_elements}
        
        with open(json_filename, 'w') as output_file:
            json.dump(json_data, output_file)
            
        csv_filename = "%s.csv"%filename
        df = pd.DataFrame(self.dwg_elements, columns = ['shape', 'x', 'y', 'size', 'colour', 'orientation'])
        df.to_csv(csv_filename)
            
                           
    def Render(self):
        """
        Prepares the svg stimulus. The stimulus parameters are first parsed, then
        a new drawing is instantiated to which all the individual elements are added.

        Returns
        -------
        None.

        """
        self.__ParseDrawingParameters()
        self.__StartNewDrawing()
        self.__AddDrawingElements()
        
            
    def Show(self):
        """
        Displays the current SVG stimulus in the IPython console window.

        Returns
        -------
        None.

        """
        self.Render()
        display(SVG(self.dwg.tostring()))
            
        
    def __ParseDrawingParameters(self):
        """
        Uses the stimulus parameter properties to create a dictionary with
        parameters for each individual shape.

        Returns
        -------
        None.

        """
        self.dwg_elements = []
        
        sizes = self.size
        colours = self.colours
        orientations = self.orientation
        datas = self.data
        shapes = self.shapes
        
        for i in range(len(shapes)):
            x           = self.positions.x[i]
            y           = self.positions.y[i]
            size        = sizes[i]
            colour      = colours[i]
            orientation = orientations[i]
            data        = datas[i]
            
            element_parameters = {'shape' : str(shapes[i].__name__), 'x' : x, 'y' : y, 'size' : size, 'colour' : colour, 'orientation' : orientation, 'data': data}
            
            self.dwg_elements.append(element_parameters)
            
            
    def __StartNewDrawing(self):        
        """
        Instantiates a new drawing canvas to which elements can be added. Executing
        this function will result in a blank canvas with the provided size and
        background color.

        Returns
        -------
        None.

        """
        self.dwg = svgwrite.Drawing(size = (self.width, self.height))
        self.background = self.dwg.rect(insert = (0, 0), size = (self.width, self.height), fill = self.background_color)
        self.dwg.add(self.background)    

    def __AddDrawingElements(self):
        """
        Adds the provided stimulus elements to the svg drawing.

        Returns
        -------
        None.

        """
        shapes = self.shapes
        
        for i in range(len(shapes)):
            el = shapes[i](**self.dwg_elements[i])
            self.dwg.add(el.generate(self.dwg))
        
    def LoadFromJSON(filename):
        """
        Creates a stimulus object from a JSON file.

        Parameters
        ----------
        filename : STRING
            JSON file that needs to be loaded.

        Returns
        -------
        stimulus : STIMULUS
            A stimulus object with parameters extracted from the JSON file.

        """
        stimulus = None
        
        with open(filename, 'r') as input_file:
            data = json.load(input_file)
            
            stimulus = Stimulus(width = data['stimulus']['width'], height = data['stimulus']['height'], background_color = data['stimulus']['background_color'])
            stimulus.positions   = jsonpickle.decode(data['stimulus']['positions'])
            stimulus.size        = jsonpickle.decode(data['stimulus']['size'])
            stimulus.shapes      = jsonpickle.decode(data['stimulus']['shapes'])
            stimulus.colour      = jsonpickle.decode(data['stimulus']['colour'])
            stimulus.orientation = jsonpickle.decode(data['stimulus']['orientation'])
            stimulus.data        = jsonpickle.decode(data['stimulus']['data'])
            
            # stimulus.dwg_elements = data['dwg_elements']
            
        return stimulus
    
    def CalculateElementsLOCE(self):
        """
        Calculate how many different elements are present in the display.

        Returns
        -------
        LOCE value.

        """     
        
        elements = [ "|".join([str(i), str(j), str(k), str(l), str(m)]) for i, j, k, l, m in zip(self.shapes.pattern, self.size.pattern, self.colour.pattern, self.orientation.pattern, self.data.pattern)] 
        
        d = defaultdict(list)
        for i, x in enumerate(elements):
            d[x].append(i)
            
        LOCE = len(d)
        
        return LOCE
    
    def SwitchElements(self, n_switches = 1):
        """
        Switches an element in the pattern with another element in the pattern.
        
        Parameters
        ----------
        n_switches: int 
            Number of switches that will take place.

        Returns
        -------
        A Stimulus object.

        """
        
        elements = [ "|".join([str(i), str(j), str(k), str(l), str(m)]) for i, j, k, l, m in zip(self.shapes.pattern, self.size.pattern, self.colour.pattern, self.orientation.pattern, self.data.pattern)] 
        
        d = defaultdict(list)
        for i, x in enumerate(elements):
            d[x].append(i)
            
        idx_elementgroups = list(d.values())
        elements_to_pick = idx_elementgroups
        switch = list()
        conducted_switches = 0
        
        if len(elements_to_pick) < 2:
            print("SwitchElements failed, because to switch elements at least 2 different elements need to be in the pattern.")
        else:
        
            for i in range(n_switches):

                if len(elements_to_pick) < 2:
                    print("Not possible to conduct so many switches! Pattern created with only " + str(conducted_switches) + " switches.")
                    break
                else:
                    groups_to_switch = random.sample(range(len(elements_to_pick)),2)
                    element_group1_to_switch = random.sample(range(len(elements_to_pick[groups_to_switch[0]])),1)
                    element_group2_to_switch = random.sample(range(len(elements_to_pick[groups_to_switch[1]])),1)
                    switch.append(elements_to_pick[groups_to_switch[0]][element_group1_to_switch[0]])
                    switch.append(elements_to_pick[groups_to_switch[1]][element_group2_to_switch[0]])
                    conducted_switches += 1
                
                    elements_to_pick = list()
                    for i in range(len(idx_elementgroups)): 
                        elements_to_pick.append([value for value in idx_elementgroups[i] if value not in switch])
                        
                    elements_to_pick = [x for x in elements_to_pick if x != []]
    
            for i in range(conducted_switches):
                pos1, pos2  = switch[(i*2)-2], switch[(i*2)-1]
#                shape1, size1, color1, orientation1 =  elements[pos1].split("|")
#                shape2, size2, color2, orientation2 =  elements[pos2].split("|")
                
                self.shapes.pattern[pos1], self.shapes.pattern[pos2] = self.shapes.pattern[pos2], self.shapes.pattern[pos1]
                self.size.pattern[pos1], self.size.pattern[pos2] = self.size.pattern[pos2], self.size.pattern[pos1]
                self.colour.pattern[pos1], self.colour.pattern[pos2] = self.colour.pattern[pos2], self.colour.pattern[pos1]
                self.orientation.pattern[pos1], self.orientation.pattern[pos2] = self.orientation.pattern[pos2], self.orientation.pattern[pos1]
                self.data.pattern[pos1], self.data.pattern[pos2] = self.data.pattern[pos2], self.data.pattern[pos1]
            
        return self
    
    
    
class Grid(Stimulus):
    def __init__(self, n_rows, n_cols, row_spacing = 50, col_spacing= 50, x_offset = 0, y_offset = 0):
        super().__init__()
        
        self._n_rows = n_rows
        self._n_cols = n_cols
        self.row_spacing = row_spacing
        self.col_spacing = col_spacing
        self.x_offset = x_offset
        self.y_offset = y_offset
        
        self.positions = Positions.Create2DGrid(n_rows = self._n_rows, n_cols = self._n_cols, row_spacing = self.row_spacing, col_spacing = self.col_spacing,
                                                x_offset = self.x_offset, y_offset = self.y_offset)
        
        self._size        = RepeatElements([5], self._n_rows, self._n_cols)
        self._shapes      = RepeatElements([Rectangle], self._n_rows, self._n_cols)
        self._colour      = RepeatElements(["black"], self._n_rows, self._n_cols)
        self._orientation = RepeatElements([0], self._n_rows, self._n_cols)
        self._data        = RepeatElements([""], self._n_rows, self._n_cols)
        
    @property
    def n_rows(self):
        return self._n_rows
    
    @n_rows.setter
    def n_rows(self, n_rows):
        self._n_rows = n_rows
        
        self.positions = Positions.Create2DGrid(n_rows = self._n_rows, n_cols = self._n_cols, row_spacing = self.row_spacing, col_spacing = self.col_spacing,
                                                x_offset = self.x_offset, y_offset = self.y_offset)
        
        for attr in ['_size', '_shapes', '_colour', '_orientation', '_data']:
            a = getattr(self, attr)
            if hasattr(a, 'n_rows'):
                setattr(a, 'n_rows', self._n_rows)
        
    @property
    def n_cols(self):
        return self._n_cols
    
    @n_cols.setter
    def n_cols(self, n_cols):
        self._n_cols = n_cols
        
        self.positions = Positions.Create2DGrid(n_rows = self._n_rows, n_cols = self._n_cols, row_spacing = self.row_spacing, col_spacing = self.col_spacing,
                                                x_offset = self.x_offset, y_offset = self.y_offset)
        
        for attr in ['_size', '_shapes', '_colour', '_orientation', '_data']:
            a = getattr(self, attr)
            if hasattr(a, 'n_rows'):
                setattr(a, 'n_rows', self._n_rows)
        
    @property
    def size(self):
        return self._size.generate().pattern
    
    @size.setter
    def size(self, size):
        self._size = size
        if hasattr(self._size, 'n_rows'):
            self._size.n_rows = self._n_rows
            self._size.n_cols = self._n_cols
            
    @property
    def shapes(self):
        return self._shapes.generate().pattern
        
    @shapes.setter
    def shapes(self, shapes):
        self._shapes = shapes
        if hasattr(self._shapes, 'n_rows'):
            self._shapes.n_rows = self._n_rows
            self._shapes.n_cols = self._n_cols
                    
    @property
    def colours(self):
        return self._colour.generate().pattern
        
    @colours.setter
    def colours(self, colour):
        self._colour = colour
        if hasattr(self._colour, 'n_rows'):
            self._colour.n_rows = self._n_rows
            self._colour.n_cols = self._n_cols
            
    @property
    def orientation(self):
        return self._orientation.generate().pattern
        
    @orientation.setter
    def orientation(self, orientation):
        self._orientation = orientation
        if hasattr(self._orientation, 'n_rows'):
            self._orientation.n_rows = self._n_rows
            self._orientation.n_cols = self._n_cols
            
    @property
    def data(self):
        return self._data.generate().pattern
        
    @data.setter
    def data(self, data):
        self._data = data
        if hasattr(self._data, 'n_rows'):
            self._data.n_rows = self._n_rows
            self._data.n_cols = self._n_cols
          
        
class Circles(Stimulus):
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
    x : Pattern
        All the x-coordinates.
    y : Pattern
        All the y-coordinates.

    """
    def __init__(self, radius, n_elements, x_offset = 0, y_offset = 0):
        super().__init__()
        
        self.radius = radius
        self.n_elements = n_elements
        self.x_offset = x_offset
        self.y_offset = y_offset
        
        self.positions = Positions.CreateCircle(self.radius, self.n_elements, self.x_offset, self.y_offset)
        
        self._size        = Pattern([5]).RepeatElementsToSize(self.n_elements)
        self._shapes      = Pattern([Rectangle]).RepeatElementsToSize(self.n_elements)
        self._colour      = Pattern(["black"]).RepeatElementsToSize(self.n_elements)
        self._orientation = Pattern([0]).RepeatElementsToSize(self.n_elements)
        self._data        = Pattern([""]).RepeatElementsToSize(self.n_elements)
        
        
    @property
    def size(self):
        if type(self._size) == Pattern:
            return self._size.pattern
        else:
            return self._size.generate().pattern
    
    @size.setter
    def size(self, size):
        self._size = size
        if hasattr(self.__size, 'n_rows'):
            self._size.n_rows = self.n_rows
            self._size.n_cols = self.n_cols
            
    @property
    def shapes(self):
        if type(self._shapes) == Pattern:
            return self._shapes.pattern
        else:
            return self._shape.generate().pattern
        
    @shapes.setter
    def shapes(self, shapes):
        self._shapes = shapes
        if hasattr(self._shapes, 'n_rows'):
            self._shapes.n_rows = self.n_rows
            self._shapes.n_cols = self.n_cols
                    
    @property
    def colours(self):
        if type(self._colour) == Pattern:
            return self._colour.pattern
        else:
            return self._colour.generate().pattern
        
    @colours.setter
    def colours(self, colour):
        self._colour = colour
        if hasattr(self._colour, 'n_rows'):
            self._colour.n_rows = self.n_rows
            self._colour.n_cols = self.n_cols
            
    @property
    def orientation(self):
        if type(self._orientation) == Pattern:
            return self._orientation.pattern
        else:
            return self._orientation.generate().pattern
        
    @orientation.setter
    def orientation(self, orientation):
        self._orientation = orientation
        if hasattr(self._orientation, 'n_rows'):
            self._orientation.n_rows = self.n_rows
            self._orientation.n_cols = self.n_cols
            
    @property
    def data(self):
        if type(self._data) == Pattern:
            return self._data.pattern
        else:
            return self._data.generate().pattern
        
    @data.setter
    def data(self, data):
        self._data = data
        if hasattr(self.__data, 'n_rows'):
            self._data.n_rows = self.n_rows
            self._data.n_cols = self.n_cols
    