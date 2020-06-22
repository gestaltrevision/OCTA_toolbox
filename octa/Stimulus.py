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
import os
from IPython.display import SVG, display

from .Positions import Positions
from .patterns.GridPattern import Pattern, RepeatAcrossElements
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
        
        
    def SaveJSON(self, filename, folder = None):
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
        csv_filename = "%s.csv"%filename
        if folder is not None:
            json_filename = os.path.join(folder, json_filename)
            csv_filename  = os.path.join(folder, csv_filename)
                    
        json_data = {'stimulus' : {'width':            self.width,
                                   'height':           self.height,
                                   'background_color': self.background_color},
                     'structure': {'class': str(type(self)),
                                   'n_rows': self._n_rows,
                                   'n_cols': self._n_cols,
                                   'row_spacing': self.row_spacing,
                                   'col_spacing': self.col_spacing,
                                   'x_offset'   : self.x_offset,
                                   'y_offset'   : self.y_offset
                                   },
                     'element_attributes': {
                                   'positions'    :    jsonpickle.encode(self.positions),
                                   'bounding_boxes' :  jsonpickle.encode(self._bounding_boxes),
                                   'shapes'       :    jsonpickle.encode(self._shapes),
                                   'fillcolor'     :  jsonpickle.encode(self._fillcolors),
                                   'bordercolor'   :  jsonpickle.encode(self._bordercolors),
                                   'orientation'  :    jsonpickle.encode(self._orientations),
                                   'data'         :    jsonpickle.encode(self._data),
                                   'overrides'    :    jsonpickle.encode(self._attribute_overrides),
                                   'element_order':    jsonpickle.encode(self._element_presentation_order)}}
        
        with open(json_filename, 'w') as output_file:
            json.dump(json_data, output_file)
            
        df = pd.DataFrame(self.dwg_elements, columns = ['shape', 'position', 'bounding_box', 'fillcolor', 'bordercolor', 'borderwidth', 'orientation', 'data'])
        df.to_csv(csv_filename)
            
        
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
            
            stimulus = Grid(data['structure']['n_rows'], data['structure']['n_cols'], data['structure']['row_spacing'],
                            data['structure']['col_spacing'], data['structure']['x_offset'], data['structure']['y_offset'])
            stimulus._positions      = jsonpickle.decode(data['element_attributes']['positions'])
            stimulus._bounding_boxes = jsonpickle.decode(data['element_attributes']['bounding_boxes'])
            stimulus._shapes         = jsonpickle.decode(data['element_attributes']['shapes'])
            stimulus._fillcolors    = jsonpickle.decode(data['element_attributes']['fillcolor'])
            stimulus._bordercolors  = jsonpickle.decode(data['element_attributes']['bordercolor'])
            stimulus._orientations   = jsonpickle.decode(data['element_attributes']['orientation'])
            stimulus._data           = jsonpickle.decode(data['element_attributes']['data'])
            stimulus._attribute_overrides = jsonpickle.decode(data['element_attributes']['overrides'])
            stimulus._element_presentation_order = jsonpickle.decode(data['element_attributes']['element_order'])
            
            
        return stimulus
    
                           
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
        fillcolors    = self.fillcolors
        bordercolors  = self.bordercolors
        borderwidths   = self.borderwidths
        orientations   = self.orientations
        datas          = self.data
        shapes         = self.shapes
        
        for i in range(len(self._element_presentation_order)):
            idx = self._element_presentation_order[i]
            x            = self.positions.x[i]
            y            = self.positions.y[i]
            
            if 'bounding_box' in self._attribute_overrides[idx]:
                bounding_box = self._attribute_overrides[idx]['bounding_box']
            else:
                bounding_box = bounding_boxes[idx]
                
            if 'fillcolor' in self._attribute_overrides[idx]:
                fillcolor = self._attribute_overrides[idx]['fillcolor']
            else:
                fillcolor = fillcolors[idx]
            
            if 'bordercolor' in self._attribute_overrides[idx]:
                bordercolor = self._attribute_overrides[idx]['bordercolor']
            else:
                bordercolor = bordercolors[idx]
            
            if 'borderwidth' in self._attribute_overrides[idx]:
                borderwidth = self._attribute_overrides[idx]['borderwidth']
            else:
                borderwidth = borderwidths[idx]
            
            if 'orientation' in self._attribute_overrides[idx]:
                orientation = self._attribute_overrides[idx]['orientation']
            else:
                orientation = orientations[idx]
            
            if 'data' in self._attribute_overrides[idx]:
                data = self._attribute_overrides[idx]['data']
            else:
                data = datas[i]
                            
            if 'shape' in self._attribute_overrides[idx]:
                shape = self._attribute_overrides[idx]['shape']
            else:
                shape = shapes[idx]
                
            element_parameters = {'shape'        : shape, 
                                  'position'     : (x, y), 
                                  'bounding_box' : bounding_box, 
                                  'fillcolor'   : fillcolor,
                                  'bordercolor' : bordercolor,
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
        
    
    
class Grid(Stimulus):
    _element_attributes = ["_bounding_boxes", "_orientations", "_bordercolors", "_borderwidths", "_fillcolors", "_shapes",
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
        self._bounding_boxes = RepeatAcrossElements([(10, 10)], self._n_rows, self._n_cols)
        self._orientations   = RepeatAcrossElements([0], self._n_rows, self._n_cols)
        self._bordercolors  = RepeatAcrossElements([""], self._n_rows, self._n_cols)
        self._borderwidths   = RepeatAcrossElements([0], self.n_rows, self.n_cols)
        self._fillcolors    = RepeatAcrossElements(["black"], self.n_rows, self.n_cols)
        self._shapes         = RepeatAcrossElements([Rectangle], self._n_rows, self._n_cols)
        self._class_labels   = RepeatAcrossElements([""], self._n_rows, self._n_cols)
        self._id_labels      = RepeatAcrossElements([""], self._n_rows, self._n_cols)
        self._mirrors        = RepeatAcrossElements([""], self._n_rows, self._n_cols)
        self._data           = RepeatAcrossElements([""], self._n_rows, self._n_cols)
        
        # Initialize a list with element attribute overrides
        self._attribute_overrides = [dict() for _ in range(self._n_cols * self._n_rows)]
        self._element_presentation_order = list(range(self._n_cols * self._n_rows))
        
    @property
    def n_rows(self):
        """
        The number of rows in the Grid
        
        """
        return self._n_rows
    
    @n_rows.setter
    def n_rows(self, n_rows):
        """
        Sets the number of rows in the grid.
        
        This only works if none of the element attributes have a fixed grid
        structure.
        """
        if not self._is_modifiable():
            print("WARNING: At least one element attribute has a fixed structure. n_rows remains unchanged.")
            return
        
        self._n_rows = n_rows
        self.positions = Positions.Create2DGrid(n_rows = self._n_rows, n_cols = self._n_cols, row_spacing = self.row_spacing, col_spacing = self.col_spacing,
                                                x_offset = self.x_offset, y_offset = self.y_offset)
        
        self._attribute_overrides = [dict() for _ in range(self._n_cols * self._n_rows)]
        self._element_presentation_order = list(range(self._n_cols * self._n_rows))
        
        for attr in Grid._element_attributes:
            setattr(getattr(self, attr), 'n_rows', self._n_rows)
        
        
    @property
    def n_cols(self):
        """
        The number of columns in the Grid
        
        """
        return self._n_cols
    
    
    @n_cols.setter
    def n_cols(self, n_cols):
        """
        Sets the number of columns in the grid.
        
        This only works if none of the element attributes have a fixed grid
        structure.
        """
        if not self._is_modifiable():
            print("WARNING: At least one element attribute has a fixed structure. n_rows remains unchanged.")
            return
        
        self._n_cols = n_cols
        
        self.positions = Positions.Create2DGrid(n_rows = self._n_rows, n_cols = self._n_cols, row_spacing = self.row_spacing, col_spacing = self.col_spacing,
                                                x_offset = self.x_offset, y_offset = self.y_offset)
        
        self._attribute_overrides = [dict() for _ in range(self._n_cols * self._n_rows)]
        self._element_presentation_order = list(range(self._n_cols * self._n_rows))
        
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
        Sets the shape of an individual element

        Parameters
        ----------
        element_id : tuple, list or int
            A tuple with the row and column index of the element. A single integer
            can also be used to refer to an element in order.
        shape_value : Shape or None
            An element shape, or None if no shape needs to be displayed.

        Returns
        -------
        None.
        """
        element_id = self._parse_element_id(element_id)
        
        self._attribute_overrides[element_id]['shape'] = shape_value
            
        
    @property
    def bordercolors(self):
        """
        The bordercolor for each element in the grid.
        
        """
        return self._bordercolors.generate().pattern
    
    
    @bordercolors.setter
    def bordercolors(self, bordercolors):
        """
        Sets the bordercolor for each grid element.
        
        If the provided pattern has a fixed grid structure, that structure
        must match the number of rows and columns of the Grid Stimulus
        
        """
        if not self._check_attribute_dimensions(bordercolors):
            return
            
        self._bordercolors = bordercolors
        self._bordercolors.n_rows = self._n_rows
        self._bordercolors.n_cols = self._n_cols
            
    def set_element_bordercolor(self, element_id, bordercolor_value):
        """
        Sets the bordercolor of an individual element

        Parameters
        ----------
        element_id : tuple, list or int
            A tuple with the row and column index of the element. A single integer
            can also be used to refer to an element in order.
        bordercolor_value : string
            color string.

        Returns
        -------
        None.

        """
        element_id = self._parse_element_id(element_id)
        
        self._attribute_overrides[element_id]['bordercolor'] = bordercolor_value
            
    @property
    def fillcolors(self):
        """
        The fillcolor for each element in the grid.
        
        """
        return self._fillcolors.generate().pattern
        
    
    @fillcolors.setter
    def fillcolors(self, fillcolors):
        """
        Sets the fillcolor for each grid element.
        
        If the provided pattern has a fixed grid structure, that structure
        must match the number of rows and columns of the Grid Stimulus
        
        """
        if not self._check_attribute_dimensions(fillcolors):
            return
        
        self._fillcolors = fillcolors
        self._fillcolors.n_rows = self._n_rows
        self._fillcolors.n_cols = self._n_cols
        
    def set_element_fillcolor(self, element_id, fillcolor_value):
        """
        Sets the fillcolor of an individual element

        Parameters
        ----------
        element_id : tuple, list or int
            A tuple with the row and column index of the element. A single integer
            can also be used to refer to an element in order.
        fillcolor_value : string
            color string.

        Returns
        -------
        None.

        """
        element_id = self._parse_element_id(element_id)
        
        self._attribute_overrides[element_id]['fillcolor'] = fillcolor_value
        
            
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
        
    def set_element_borderwidth(self, element_id, borderwidth_value):
        """
        Sets the borderwidth of an individual element

        Parameters
        ----------
        element_id : tuple, list or int
            A tuple with the row and column index of the element. A single integer
            can also be used to refer to an element in order.
        borderwidth_value : int
            Size of the border.

        Returns
        -------
        None.

        """
        element_id = self._parse_element_id(element_id)
        
        self._attribute_overrides[element_id]['borderwidth'] = borderwidth_value
                       
        
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
            
    def set_element_orientation(self, element_id, orientation_value):
        """
        Sets the orientation of an individual element

        Parameters
        ----------
        element_id : tuple, list or int
            A tuple with the row and column index of the element. A single integer
            can also be used to refer to an element in order.
        orientation_value : int
            Orientation of the element.

        Returns
        -------
        None.

        """
        element_id = self._parse_element_id(element_id)
        
        self._attribute_overrides[element_id]['orientation'] = orientation_value
            
            
    @property
    def data(self):
        """
        The data for each element in the grid.
        
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
        
    def set_element_data(self, element_id, data_value):
        """
        Sets the data of an individual element

        Parameters
        ----------
        element_id : tuple, list or int
            A tuple with the row and column index of the element. A single integer
            can also be used to refer to an element in order.
        data_value : string
            Data string for the element.

        Returns
        -------
        None.

        """
        element_id = self._parse_element_id(element_id)
        
        self._attribute_overrides[element_id]['data'] = data_value
            
            
    def swap_elements(self, n_swap_pairs = 1):
        """
        Swaps the position of two elements in the pattern. Once a position has
        been used in a swap, it will not be used again in additional swaps. 
        As a consequence, the maximum number of possible swaps is N//2, where
        N is the number of elements in the pattern.
        
        When doing multiple swaps, if two elements have been selected to be
        swapped around a first time, they will not be selected again. This
        means that subsequent swaps can never cancel out an initial swap.
        
        Parameters
        ----------
        n_swap_pairs: int 
            Number of element pairs that will be swapped. Maximum value
            is half the total number of elements

        Returns
        -------
        Pattern:
            New Pattern object instance

        """
        n_elements = self._n_rows * self._n_cols
        assert n_elements >= n_swap_pairs * 2, 'Maximal number of swaps possible is %d, but %d were requested'%(len(self.pattern)//2, n_swap_pairs)
               
        # 1. Generate all available swap positions
        candidate_swap_positions = set()
        for i in range(n_elements):
            for j in range(i+1, n_elements):
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
        for swap_pair in selected_swap_pairs:
            self._element_presentation_order[swap_pair[0]], self._element_presentation_order[swap_pair[1]] = self._element_presentation_order[swap_pair[1]], self._element_presentation_order[swap_pair[0]]

        
    def _is_modifiable(self):
        """
        Inspects the _fixed_grid attribute of each of the element properties.
        Used to determine if the stimulus n_rows and n_cols attributes can
        be modified directly.
        
        Parameters
        ----------
        None
        
        Return
        ------
        modifiable: Boolean
            True if none of the element attributes has a fixed structure. 
            False if at least one element has a fixed structure
        """
        fixed_attributes = []
        
        for attr_name in Grid._element_attributes:
            attr = getattr(self, attr_name)
            if attr._fixed_grid == True:
                print("Property %s has a fixed grid structure of %d rows and %d columns"%(attr_name, attr.n_rows, attr.n_cols))
                fixed_attributes.append(attr_name)
                
        modifiable = True if len(fixed_attributes) == 0 else False
            
        return modifiable
    
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
        