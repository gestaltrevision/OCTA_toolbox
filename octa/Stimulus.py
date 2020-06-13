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
        
        bounding_boxes = self.bounding_boxes
        fillcolours    = self.fillcolours
        bordercolours  = self.bordercolours
        borderwidths   = self.borderwidths
        orientations   = self.orientations
        datas          = self.data
        shapes         = self.shapes
        
        for i in range(len(shapes)):
            x            = self.positions.x[i]
            y            = self.positions.y[i]
            
            if 'bounding_box' in self._attribute_overrides[i]:
                bounding_box = self._attribute_overrides[i]['bounding_box']
            else:
                bounding_box = bounding_boxes[i]
                
            fillcolour   = fillcolours[i]
            bordercolour = bordercolours[i]
            borderwidth  = borderwidths[i]
            orientation  = orientations[i]
            data         = datas[i]
            
            if 'shape' in self._attribute_overrides[i]:
                shape = self._attribute_overrides[i]['shape']
            else:
                shape = shapes[i]
                
            element_parameters = {'shape'        : shape, 
                                  'position'     : (x, y), 
                                  'bounding_box' : bounding_box, 
                                  'fillcolour'   : fillcolour,
                                  'bordercolour' : bordercolour,
                                  'borderwidth'  : borderwidth,
                                  'orientation'  : orientation, 
                                  'data'         : data}
            
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
        self.dwg = svgwrite.Drawing(size = (self.width, self.height), profile="tiny")
        self.background = self.dwg.rect(insert = (0, 0), size = (self.width, self.height), fill = self.background_color)
        self.dwg.add(self.background)    

    def __AddDrawingElements(self):
        """
        Adds the provided stimulus elements to the svg drawing.

        Returns
        -------
        None.

        """                
        for i in range(len(self.dwg_elements)):
            if not self.dwg_elements[i]['shape'] == None:
                el = self.dwg_elements[i]['shape'](**self.dwg_elements[i])
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
    _element_attributes = ["_bounding_boxes", "_orientations", "_bordercolours", "_borderwidths", "_fillcolours", "_shapes",
                          "_class_labels", "_id_labels", "_mirrors", "_data"]
    
    def __init__(self, n_rows, n_cols, row_spacing = 50, col_spacing= 50, x_offset = 0, y_offset = 0):
        super().__init__()
        
        # Initialize the positions of each element
        self._n_rows = n_rows
        self._n_cols = n_cols
        self.row_spacing = row_spacing
        self.col_spacing = col_spacing
        self.x_offset = x_offset
        self.y_offset = y_offset
        
        self.positions = Positions.Create2DGrid(n_rows = self._n_rows, n_cols = self._n_cols, row_spacing = self.row_spacing, col_spacing = self.col_spacing,
                                                x_offset = self.x_offset, y_offset = self.y_offset)
        
        # Initialize the element attributes to their default values
        self._bounding_boxes = RepeatElements([(10, 10)], self._n_rows, self._n_cols)
        self._orientations   = RepeatElements([0], self._n_rows, self._n_cols)
        self._bordercolours  = RepeatElements([""], self._n_rows, self._n_cols)
        self._borderwidths   = RepeatElements([0], self.n_rows, self.n_cols)
        self._fillcolours    = RepeatElements(["black"], self.n_rows, self.n_cols)
        self._shapes         = RepeatElements([Rectangle], self._n_rows, self._n_cols)
        self._class_labels   = RepeatElements([""], self._n_rows, self._n_cols)
        self._id_labels      = RepeatElements([""], self._n_rows, self._n_cols)
        self._mirrors        = RepeatElements([""], self._n_rows, self._n_cols)
        self._data           = RepeatElements([""], self._n_rows, self._n_cols)
        
        # Initialize a list with element attribute overrides
        self._attribute_overrides = [dict() for _ in range(self._n_cols * self._n_rows)]
        
    @property
    def n_rows(self):
        """
        The number of columns in the Grid
        
        """
        return self._n_rows
    
    @n_rows.setter
    def n_rows(self, n_rows):
        """
        Sets the number of rows in the grid.
        
        This only works if none of the element attributes have a fixed grid
        structure.
        """
        if not self._is_modifieable():
            print("WARNING: At least one element attribute has a fixed structure. n_rows remains unchanged.")
            return
        
        self._n_rows = n_rows
        self.positions = Positions.Create2DGrid(n_rows = self._n_rows, n_cols = self._n_cols, row_spacing = self.row_spacing, col_spacing = self.col_spacing,
                                                x_offset = self.x_offset, y_offset = self.y_offset)
        self._attribute_overrides = [dict() for _ in range(self._n_cols * self._n_rows)]
        for attr in Grid._element_attributes:
            setattr(getattr(self, attr), 'n_rows', self._n_rows)
        
        
    @property
    def n_cols(self):
        """
        The number of rows in the Grid
        
        """
        return self._n_cols
    
    
    @n_cols.setter
    def n_cols(self, n_cols):
        """
        Sets the number of columns in the grid.
        
        This only works if none of the element attributes have a fixed grid
        structure.
        """
        if not self._is_modifieable():
            print("WARNING: At least one element attribute has a fixed structure. n_rows remains unchanged.")
            return
        
        self._n_cols = n_cols
        
        self.positions = Positions.Create2DGrid(n_rows = self._n_rows, n_cols = self._n_cols, row_spacing = self.row_spacing, col_spacing = self.col_spacing,
                                                x_offset = self.x_offset, y_offset = self.y_offset)
        self._attribute_overrides = [dict() for _ in range(self._n_cols * self._n_rows)]
        for attr in Grid._element_attributes:
            setattr(getattr(self, attr), 'n_cols', self._n_cols)
        
        
    @property
    def bounding_boxes(self):
        """
        The size for each element in the grid.
        
        The size is defined in terms of a rectangular bounding box that
        contains the element.
        
        """
        return self._bounding_boxes.generate().pattern
    
    
    @bounding_boxes.setter
    def bounding_boxes(self, bounding_box):
        """
        Sets the bounding box size for each grid element.
        
        If the provided pattern has a fixed grid structure, that structure
        must match the number of rows and columns of the Grid Stimulus
        
        """
        if not self._check_attribute_dimensions(bounding_box):
            return
            
        self._bounding_boxes = bounding_box
        self._bounding_boxes.n_rows = self._n_rows
        self._bounding_boxes.n_cols = self._n_cols
        
    
    def set_element_bounding_box(self, element_id, bounding_box_value):
        """
        Sets the bounding box value for an individual element
        """
        element_id = self._parse_element_id(element_id)
        bounding_box_value = Grid._check_bounding_box_value(bounding_box_value)                
        self._attribute_overrides[element_id]['bounding_box'] = bounding_box_value
        
    def _check_bounding_box_value(bounding_box_value):
        """
        Inspects the bounding_box_value and raises an error when the format
        of this value is not correct
        
        Returns
        -------
        bounding_box_value: tuple
            A valid bounding_box_value
        """
        assert type(bounding_box_value) == list or type(bounding_box_value) == tuple or type(bounding_box_value) == int, "Bounding box value must be int, list or tuple"
        
        if type(bounding_box_value) == list or type(bounding_box_value) == tuple:
            assert len(bounding_box_value) == 2, "Bounding box collection can only contain two values"
        else:
            bounding_box_value = (bounding_box_value, bounding_box_value)
            
        return bounding_box_value
          
        
    @property
    def shapes(self):
        """
        The shape for each element in the grid.
        
        """
        return self._shapes.generate().pattern
        
    
    @shapes.setter
    def shapes(self, shapes):
        """
        Sets the shape for each grid element.
        
        If the provided pattern has a fixed grid structure, that structure
        must match the number of rows and columns of the Grid Stimulus
        
        """
        if not self._check_attribute_dimensions(shapes):
            return
            
        self._shapes = shapes
        self._shapes.n_rows = self._n_rows
        self._shapes.n_cols = self._n_cols
        
        
    def set_element_shape(self, element_id, shape_value):
        """
        Sets the bounding box value for an individual element
        """
        element_id = self._parse_element_id(element_id)
        
        self._attribute_overrides[element_id]['shape'] = shape_value
            
        
    @property
    def bordercolours(self):
        """
        The bordercolour for each element in the grid.
        
        """
        return self._bordercolours.generate().pattern
    
    
    @bordercolours.setter
    def bordercolours(self, bordercolours):
        """
        Sets the bordercolour for each grid element.
        
        If the provided pattern has a fixed grid structure, that structure
        must match the number of rows and columns of the Grid Stimulus
        
        """
        if not self._check_attribute_dimensions(bordercolours):
            return
            
        self._bordercolours = bordercolours
        self._bordercolours.n_rows = self._n_rows
        self._bordercolours.n_cols = self._n_cols
            
            
    @property
    def fillcolours(self):
        """
        The fillcolour for each element in the grid.
        
        """
        return self._fillcolours.generate().pattern
        
    
    @fillcolours.setter
    def fillcolours(self, fillcolours):
        """
        Sets the fillcolour for each grid element.
        
        If the provided pattern has a fixed grid structure, that structure
        must match the number of rows and columns of the Grid Stimulus
        
        """
        if not self._check_attribute_dimensions(fillcolours):
            return
        
        self._fillcolours = fillcolours
        self._fillcolours.n_rows = self._n_rows
        self._fillcolours.n_cols = self._n_cols
        
            
    @property
    def borderwidths(self):
        """
        The borderwidths for each element in the grid.
        
        """
        return self._borderwidths.generate().pattern
        
    
    @borderwidths.setter
    def borderwidths(self, borderwidths):
        """
        Sets the borderwidths for each grid element.
        
        If the provided pattern has a fixed grid structure, that structure
        must match the number of rows and columns of the Grid Stimulus
        
        """
        if not self._check_attribute_dimensions(borderwidths):
            return
        
        self._borderwidths = borderwidths
        self._borderwidths.n_rows = self._n_rows
        self._borderwidths.n_cols = self._n_cols
                       
        
    @property
    def orientations(self):
        """
        The orientations for each element in the grid.
        
        """
        return self._orientations.generate().pattern
        
    
    @orientations.setter
    def orientations(self, orientations):
        """
        Sets the orientations for each grid element.
        
        If the provided pattern has a fixed grid structure, that structure
        must match the number of rows and columns of the Grid Stimulus
        
        """
        if not self._check_attribute_dimensions(orientations):
            return
        
        self._orientations = orientations
        if hasattr(self._orientations, 'n_rows'):
            self._orientations.n_rows = self._n_rows
            self._orientations.n_cols = self._n_cols
            
            
    @property
    def data(self):
        """
        The orientations for each element in the grid.
        
        """
        return self._data.generate().pattern
        
    @data.setter
    def data(self, data):
        """
        Sets the data for each grid element.
        
        If the provided pattern has a fixed grid structure, that structure
        must match the number of rows and columns of the Grid Stimulus
        
        """
        if not self._check_attribute_dimensions(data):
            return
        
        self._data = data
        self._data.n_rows = self._n_rows
        self._data.n_cols = self._n_cols
            
            
    def _is_modifieable(self):
        """
        Inspects the _fixed_grid attribute of each of the element properties.
        
        Parameters
        ----------
        None
        
        Return
        ------
        True if none of the element attributes has a fixed structure. 
        False if at least one element has a fixed structure
        """
        fixed_attributes = []
        
        for attr_name in Grid._element_attributes:
            attr = getattr(self, attr_name)
            if attr._fixed_grid == True:
                print("Property %s has a fixed grid structure of %d rows and %d columns"%(attr_name, attr.n_rows, attr.n_cols))
                
        modifieable = False if len(fixed_attributes) == 0 else True
            
        return modifieable
    
    def _check_attribute_dimensions(self, attr):
        """
        Checks if the dimensions of an attribute are changeable.
        
        If not, the dimensions should match those of the stimulus
        
        Parameters
        ----------
        attr:
            The attribute value that needs to be checked
            
        Return
        ------
        Boolean
            True if the attribute can be used in the current Grid
            False if the attribute cannot be used in the current Grid
        """
        if attr._fixed_grid == True:
            if not (attr.n_rows == self._n_rows and attr.n_cols == self._n_cols):
                print("WARNING: property has a fixed grid structure and does not match the stimulus structure")
                return False
            
        return True
    
    def _parse_element_id(self, element_id):
        """
        Validates and parses the element_id that is passed to functions that
        allow the manipulation of a single element in the grid.
        
        The following conditions are checked
        - element id must be int, list or tuple
        - if list or tuple, the length must be 2
        - the resulting element id cannot exceed the number of elements in the grid
        """
        assert type(element_id) == list or type(element_id) == tuple or type(element_id) == int, "Element id must be an integer, list or tuple"
        
        if type(element_id) == list or type(element_id) == tuple:
            assert len(element_id) == 2, "Element id must contain two values"
            element_id = element_id[0] * self.n_cols + element_id[1]
                
        assert 0 <= element_id < self.n_rows * self.n_cols, "Element id not in range"
        
        return element_id
        