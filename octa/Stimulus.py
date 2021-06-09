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
from html2image import Html2Image
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
from IPython.display import SVG, display

from .Positions import Positions
from .patterns import GridPattern, Pattern
from .shapes.Polygon import Polygon

class Stimulus:
    """ Container class for creating a stimulus.
    
    """
    
    def __init__(self, background_color = "white", x_margin = 20, y_margin = 20, size = None, background_shape = None, mask = None, 
                 stim_orientation = 0, stim_mirror_value = None, stim_class_label = None, stim_id_label = None):
        """
        Instantiates a stimulus object.

        Parameters
        ----------
        background_color : STRING, optional
            Background color of the stimulus. The default is "white".
        x_margin: INT, optional
            Amount of extra space added to the stimulus in the x-direction
        y_margin: INT, optional
            Amount of extra space added to the stimulus in the y-direction
        size: TUPLE, optional
            If specified, fixes the size of the stimulus to the dimension
            given in the tuple. The center of the stimulus will be calculated
            to correspond to the average position of all the elements in the
            stimulus.
            

        Returns
        -------
        None.

        """
        if size == None:
            self._autosize = True
            self.width = -1
            self.height = -1
            self.x_margin = x_margin
            self.y_margin = y_margin
            self.size = "auto"
        else:
            self._autosize = False
            self.width = size[0]
            self.height = size[1]
            self.x_margin = "auto"
            self.y_margin = "auto"
            self.size = (size[0], size[1])
            
        self.background_color = background_color
        self.stim_orientation = stim_orientation
        self.stim_mirror_value = stim_mirror_value
        self.stim_class_label = stim_class_label
        self.stim_id_label = stim_id_label
        
        if background_shape == None:
            self.background_shape = "auto"
        else:
            self.background_shape = background_shape
        
        if mask == None:
            self.mask = "none"
        else:
            self.mask = mask
        
        # Set initial shape parameters to zero
        self.positions   = None

        self._autosize_method = "maximum_bounding_box" # can be 'tight_fit' or 'maximum_bounding_box'
        
        self.dwg_elements = None
        self.dwg = None
        

    def SaveSVG(self, filename, folder = None):
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
        
        svg_filename = "%s.svg"%filename
        if folder is not None:
            svg_filename = os.path.join(folder, svg_filename)  
            
        self.dwg.saveas(svg_filename , pretty = True)
        
    def GetSVG(self):
        """
        Gives the current stimulus as an SVG string.

        Parameters
        ----------
        None.

        Returns
        -------
        String.

        """
        self.Render()
        return self.dwg.tostring()
    
    def SavePNG(self, filename, folder = None): 
        """
        Saves the current stimulus as a PNG file.

        Parameters
        ----------
        filename : STRING
            Name of the png file.

        Returns
        -------
        None.

        """ 
        # limitations using svglib:
        # clipping is limited to single paths, no mask support
        # color gradients not supported

        svg_filename = "%s.svg"%filename
        png_filename = "%s.png"%filename
        if folder is not None:
            svg_filename = os.path.join(folder, svg_filename)  
#            png_fullfilename = os.path.join(folder, png_filename)
            hti = Html2Image(output_path = folder)
        else:
            hti = Html2Image()

        self.dwg.saveas(svg_filename, pretty = True)
        
        hti.screenshot(other_file = svg_filename, 
                       size= (self.width, self.height), 
                       save_as = png_filename)
#        img = svg2rlg(svg_filename)
#        os.remove(svg_filename)
#        renderPM.drawToFile(img, png_filename, fmt="PNG")
        
    def SavePDF(self, filename, folder = None): 
        """
        Saves the current stimulus as a PDF file.

        Parameters
        ----------
        filename : STRING
            Name of the pdf file.

        Returns
        -------
        None.

        """ 
        # limitations using svglib:
        # clipping is limited to single paths, no mask support
        # color gradients not supported
            
        svg_filename = "%s.svg"%filename
        pdf_filename = "%s.pdf"%filename
        if folder is not None:
            svg_filename = os.path.join(folder, svg_filename)  
            pdf_filename = os.path.join(folder, pdf_filename)       

        self.dwg.saveas(svg_filename, pretty = True)
        img = svg2rlg(svg_filename)
        os.remove(svg_filename)
        renderPDF.drawToFile(img, pdf_filename)
        
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
                                   'background_color': self.background_color,
                                   'background_shape': self.background_shape,
                                   'mask':             self.mask},
                     'structure': {'class': str(type(self)),
                                   'n_rows': self._n_rows,
                                   'n_cols': self._n_cols,
                                   'row_spacing': self.row_spacing,
                                   'col_spacing': self.col_spacing,
                                   'x_margin'   : self.x_margin,
                                   'y_margin'   : self.y_margin,
                                   'size'       : self.size
                                   },
                     'element_attributes': {
                                   'element_id'   :    jsonpickle.encode(list(range(len(self.dwg_elements)))),
                                   'positions'    :    jsonpickle.encode(self.positions),
                                   'bounding_boxes' :  jsonpickle.encode(self._bounding_boxes),
                                   'shapes'       :    jsonpickle.encode(self._shapes),
                                   'fillcolors'     :  jsonpickle.encode(self._fillcolors),
                                   'opacities'      :  jsonpickle.encode(self._opacities),
                                   'bordercolors'   :  jsonpickle.encode(self._bordercolors),
                                   'borderwidths'   :  jsonpickle.encode(self._borderwidths),
                                   'orientations'  :   jsonpickle.encode(self._orientations),
                                   'data'         :    jsonpickle.encode(self._data),
                                   'overrides'    :    jsonpickle.encode(self._attribute_overrides),
                                   'element_order':    jsonpickle.encode(self._element_presentation_order),
                                   'id'           :    jsonpickle.encode(self._id_labels),
                                   'class'        :    jsonpickle.encode(self._class_labels),
                                   'mirror'       :    jsonpickle.encode(self._mirror_values)}}
        
        with open(json_filename, 'w') as output_file:
            json.dump(json_data, output_file, indent = 4)
            
        df = pd.DataFrame(self.dwg_elements, columns = ['element_id', 'position', 'shape', 'bounding_box', 'fillcolor', 'opacity', 'bordercolor', 'borderwidth', 'orientation', 'data'])
        df.to_csv(csv_filename, index = False)
   
    def GetJSON(self):
        """
        Gives the JSON info concerning the current stimulus.

        Parameters
        ----------
        None.

        Returns
        -------
        JSON object.

        """
                   
        json_data = {'stimulus' : {'width':            self.width,
                                   'height':           self.height,
                                   'background_color': self.background_color,
                                   'background_shape': self.background_shape,
                                   'mask':             self.mask},
                     'structure': {'class': str(type(self)),
                                   'n_rows': self._n_rows,
                                   'n_cols': self._n_cols,
                                   'row_spacing': self.row_spacing,
                                   'col_spacing': self.col_spacing,
                                   'x_margin'   : self.x_margin,
                                   'y_margin'   : self.y_margin,
                                   'size'       : self.size
                                   },
                     'element_attributes': {
                                   'element_id'     : jsonpickle.encode(list(range(len(self.dwg_elements)))),
                                   'positions'      : jsonpickle.encode(self.positions),
                                   'bounding_boxes' : jsonpickle.encode(self._bounding_boxes),
                                   'shapes'         : jsonpickle.encode(self._shapes),
                                   'fillcolors'     : jsonpickle.encode(self._fillcolors),
                                   'opacities'      :  jsonpickle.encode(self._opacities),
                                   'bordercolors'   : jsonpickle.encode(self._bordercolors),
                                   'borderwidths'   : jsonpickle.encode(self._borderwidths),
                                   'orientations'   : jsonpickle.encode(self._orientations),
                                   'data'           : jsonpickle.encode(self._data),
                                   'overrides'      : jsonpickle.encode(self._attribute_overrides),
                                   'element_order':    jsonpickle.encode(self._element_presentation_order),
                                   'id'           :    jsonpickle.encode(self._id_labels),
                                   'class'        :    jsonpickle.encode(self._class_labels),
                                   'mirror'       :    jsonpickle.encode(self._mirror_values)}}
        
        return json_data            
        
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
            
            if data['structure']['size'] == 'auto':
                stimulus_size = None
            else:
                stimulus_size = (data['stimulus']['width'], data['stimulus']['height'])
                
            stimulus = Grid(data['structure']['n_rows'], 
                            data['structure']['n_cols'], 
                            data['structure']['row_spacing'],
                            data['structure']['col_spacing'], 
                            data['stimulus']['background_color'],
                            stimulus_size,
                            data['stimulus']['background_shape'],
                            data['stimulus']['mask'],
                            data['structure']['x_margin'], 
                            data['structure']['y_margin'])
            
            stimulus.positions                   = jsonpickle.decode(data['element_attributes']['positions'])
            stimulus._bounding_boxes             = jsonpickle.decode(data['element_attributes']['bounding_boxes'])
            stimulus._shapes                     = jsonpickle.decode(data['element_attributes']['shapes'])
            stimulus._fillcolors                 = jsonpickle.decode(data['element_attributes']['fillcolors'])
            stimulus._opacities                  = jsonpickle.decode(data['element_attributes']['opacities'])
            stimulus._bordercolors               = jsonpickle.decode(data['element_attributes']['bordercolors'])
            stimulus._borderwidths               = jsonpickle.decode(data['element_attributes']['borderwidths'])
            stimulus._orientations               = jsonpickle.decode(data['element_attributes']['orientations'])
            stimulus._data                       = jsonpickle.decode(data['element_attributes']['data'])
            stimulus._attribute_overrides        = jsonpickle.decode(data['element_attributes']['overrides'])
            stimulus._element_presentation_order = jsonpickle.decode(data['element_attributes']['element_order'])
            stimulus._id_labels                  = jsonpickle.decode(data['element_attributes']['id'])
            stimulus._class_labels               = jsonpickle.decode(data['element_attributes']['class'])
            stimulus._mirror_values              = jsonpickle.decode(data['element_attributes']['mirror'])
            
            
#            for i in range(len(stimulus.data)):
#                if stimulus.data[i] != "":
#                    if "Polygon" in str(stimulus.shapes[i]):
#                        stimulus.shapes[i] = eval(str(stimulus._shapes.patterntype) + str(stimulus._shapes.patternorientation) + "(Polygon(" + str(stimulus.data[i]) + "))")
#                        print(stimulus.data)
                        
#            origshapelist = stimulus._shapes.pattern          
#            shapelist = []
#            for i in range(len(origshapelist)):
#                if origshapelist[i] is not None:
#                    if ".Polygon." in str(origshapelist[i]):
#                        shapelist.append(str("Polygon(n_sides = " + str(stimulus._data.pattern[i][0]) + ", name = '" + str(stimulus._data.pattern[i][1]) + "')"))
#                    elif str(stimulus._shapes.pattern[i].__bases__[0]) == "<class 'octa.shapes.RegularPolygon.RegularPolygon_'>":
#                        shapelist.append((stimulus._shapes.pattern[i].n_sides, stimulus._shapes.pattern[i].name))
#                    elif str(stimulus._shapes.pattern[i].__bases__[0]) == "<class 'octa.shapes.Image.Image_'>":
#                        shapelist.append((stimulus._shapes.pattern[i].source, stimulus._shapes.pattern[i].name))
#                    elif str(stimulus._shapes.pattern[i].__bases__[0]) == "<class 'octa.shapes.FitImage.FitImage_'>":
#                        shapelist.append((stimulus._shapes.pattern[i].source, stimulus._shapes.pattern[i].name))
#                    elif str(stimulus._shapes.pattern[i].__bases__[0]) == "<class 'octa.shapes.Text.Text_'>":
#                        shapelist.append((stimulus._shapes.pattern[i].text, stimulus._shapes.pattern[i].name))
#                    elif str(stimulus._shapes.pattern[i].__bases__[0]) == "<class 'octa.shapes.Path.Path_'>":
#                        shapelist.append((stimulus._shapes.pattern[i].path, stimulus._shapes.pattern[i].xsizepath, stimulus._shapes.pattern[i].ysizepath, stimulus._shapes.pattern[i].name))
#                    elif str(stimulus._shapes.pattern[i].__bases__[0]) == "<class 'octa.shapes.PathSvg.PathSvg_'>":
#                        shapelist.append((stimulus._shapes.pattern[i].source, stimulus._shapes.pattern[i].name))
#                    else:
#                        shapelist.append("")
#                else:
#                    shapelist.append("")
                        
#            stimulus.shapes = eval(str(stimulus._shapes.generate().patterntype) + str(stimulus._shapes.generate().patternorientation) + "(" + "[octa.shapes.Polygon.Polygon_8]" + ")")
 
                          
#            for d in json:
#    name = d.pop('name')
#    t = type(name, (object,), d)
            
        return stimulus
    
                           
    def Render(self):
        """
        Prepares the svg stimulus. The stimulus parameters are first parsed, then
        a new drawing is instantiated to which all the individual elements are added.

        Returns
        -------
        None.

        """
        self.__CalculateStimulusValues()
        self.__AutoCalculateSize()
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
            
        
    def __CalculateStimulusValues(self):
        self._calculated_positions = self.positions.GetPositions()
        
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
        fillcolors     = self.fillcolors
        opacities      = self.opacities
        bordercolors   = self.bordercolors
        borderwidths   = self.borderwidths
        orientations   = self.orientations
        datas          = self.data
        shapes         = self.shapes
        id_labels      = self.id_labels
        class_labels   = self.class_labels
        mirror_values  = self.mirror_values
        x, y           = self._calculated_positions
        
        for i in range(len(self._element_presentation_order)):
            idx = self._element_presentation_order[i]
            
            x_i           = x[i] + self._x_offset
            y_i           = y[i] + self._y_offset
            
            if 'bounding_box' in self._attribute_overrides[idx]:
                bounding_box = self._attribute_overrides[idx]['bounding_box']
            else:
                bounding_box = bounding_boxes[idx]
                
            if 'fillcolor' in self._attribute_overrides[idx]:
                fillcolor = self._attribute_overrides[idx]['fillcolor']
            else:
                fillcolor = fillcolors[idx]
                
            if 'opacity' in self._attribute_overrides[idx]:
                opacity = self._attribute_overrides[idx]['opacity']
            else:
                opacity = opacities[idx]
                
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
                data = datas[idx]
                            
            if 'shape' in self._attribute_overrides[idx]:
                shape = self._attribute_overrides[idx]['shape']
            else:
                shape = shapes[idx]
                
            if 'mirror_values' in self._attribute_overrides[idx]:
                mirror_value = self._attribute_overrides[idx]['mirror_values']
            else:
                mirror_value = mirror_values[idx]
                
            if 'class_labels' in self._attribute_overrides[idx]:
                class_label = self._attribute_overrides[idx]['class_labels']
            else:
                class_label = class_labels[idx]
                
            if 'id_labels' in self._attribute_overrides[idx]:
                id_label = self._attribute_overrides[idx]['id_labels']
            else:
                id_label = id_labels[idx]
                
            element_parameters = {'element_id'   : i,
                                  'shape'        : shape, 
                                  'position'     : (x_i, y_i), 
                                  'bounding_box' : bounding_box, 
                                  'fillcolor'    : fillcolor,
                                  'opacity'      : opacity,
                                  'bordercolor'  : bordercolor,
                                  'borderwidth'  : borderwidth,
                                  'orientation'  : orientation, 
                                  'class_label'  : class_label,
                                  'id_label'     : id_label,
                                  'mirror_value' : mirror_value,
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
        self.dwg = svgwrite.Drawing(size = (self.width, self.height)) #, profile="tiny"

        # ADD CLIP PATH
        if(self.background_shape != "auto"):
            self.clip_path = self.dwg.defs.add(self.dwg.clipPath(id='custom_clip_path'))
            self.clip_path.add(self.background_shape.generate(self.dwg)) #things inside this shape will be drawn
            clippath = "url(#custom_clip_path)"
        else:
            clippath = None
            
        # ADD MASK
        if(self.mask != "none"):
            self.mask_object = self.dwg.defs.add(self.dwg.mask(id='custom_mask'))
            self.mask_object.add(self.mask.generate(self.dwg))
            maskpath = "url(#custom_mask)"
        else:
            maskpath = None
            
        # ADD MIRROR VALUE  
        mirror_transform = ""
        if self.stim_mirror_value == "vertical":
            mirror_transform = "scale(-1, 1) translate(%f, 0)"%(-2*(self.width/2))
        elif self.stim_mirror_value == "horizontal":
            mirror_transform = "scale(1, -1), translate(0, %f)"%(-2*(self.height/2))
        elif self.stim_mirror_value == "horizontalvertical":
            mirror_transform = "scale(-1, -1) translate(%f, %f)"%(-2*(self.width/2), -2*(self.height/2))

        # ADD ROTATION
        if (type(self.stim_orientation) == int) or (type(self.stim_orientation) == float):
            self.rotation_animation = ""
            rotation_transform = "rotate(%d, %d, %d)"%(self.stim_orientation, self.width/2, self.height/2)
        elif type(self.stim_orientation) == list:
            self.rotation_animation = "svgwrite.animate.AnimateTransform('rotate','transform', from_= '" + self.stim_orientation[1] + " " + str(self.width/2) + " " + str(self.height/2) + "', to = '" + self.stim_orientation[2] + " " + str(self.width/2) + " " + str(self.height/2) + "', " + self.stim_orientation[3] + ")"
            rotation_transform = "rotate(%d, %d, %d)"%(int(self.stim_orientation[1]), self.width/2, self.height/2)
                        
        if(clippath != None):
            if(maskpath != None):
                self.stim = self.dwg.add(self.dwg.g(clip_path = clippath, mask = maskpath, 
                                                    transform = " ".join([mirror_transform, rotation_transform])))
            else:
                self.stim = self.dwg.add(self.dwg.g(clip_path = clippath, 
                                                    transform = " ".join([mirror_transform, rotation_transform])))
        else:
            if(maskpath != None):
                self.stim = self.dwg.add(self.dwg.g(mask = maskpath, 
                                                    transform = " ".join([mirror_transform, rotation_transform])))
            else:
                self.stim = self.dwg.add(self.dwg.g(transform = " ".join([mirror_transform, rotation_transform])))
          
        # ADD BACKGROUND COLOR
        if type(self.background_color) == str:
            self.background_color_animation = ""
            self.background = self.dwg.rect(insert = (0, 0), size = (self.width, self.height), fill = self.background_color)
            
        elif type(self.background_color) == list:
            if self.background_color[0] == "set":                
                self.background_color_animation = "svgwrite.animate.Set(attributeName = 'fill'," + self.background_color[2] + ")"
                self.background_color = self.background_color[1]
                self.background = self.dwg.rect(insert = (0, 0), size = (self.width, self.height), fill = self.background_color) 
        
            elif self.background_color[0] == "animate":
                self.background_color_animation = "svgwrite.animate.Animate(attributeName = 'fill'," + self.background_color[2] + ")"
                self.background_color = self.background_color[1]
                self.background = self.dwg.rect(insert = (0, 0), size = (self.width, self.height), fill = self.background_color) 
        
            else:
                self.background_color_animation = ""
            
                gradient = ""
                if self.background_color[0] == "radial":
                    gradient = self.dwg.radialGradient()               
                elif self.background_color[0] == "horizontal":
                    gradient = self.dwg.linearGradient((0, 0), (1, 0))
                elif self.background_color[0] == "vertical":
                    gradient = self.dwg.linearGradient((0, 0), (0, 1))
                elif self.background_color[0] == "diagonal":
                    gradient = self.dwg.linearGradient((0, 0), (1, 1))
                    
                else:
                    self.background = self.dwg.rect(insert = (0, 0), size = (self.width, self.height), fill = self.background_color) 
        
                    
                if gradient != "":
                    self.dwg.defs.add(gradient)
                    
                    # define the gradient colors
                    n_colors = len(self.background_color)-1
                    stepsize = 1 / (n_colors - 1)
                    for i in range(n_colors):
                        gradient.add_stop_color(i*stepsize, self.background_color[i+1])
            
                    self.background = self.dwg.rect(insert = (0, 0), size = (self.width, self.height), fill = gradient.get_paint_server() )
                
                
        if self.background_color_animation != "":
            self.background.add(eval(self.background_color_animation))
            
        self.stim.add(self.background)  
            
        # ADD CLASS AND ID LABEL
            
        if self.stim_class_label != None:
            self.stim['class']         = self.stim_class_label
        if self.stim_id_label != None:
            self.stim['id']        = self.stim_id_label
        
        if self.rotation_animation != "":
            self.stim.add(eval(self.rotation_animation))  
            
    @property
    def x_margin(self):
        return self._x_margin
    
    @x_margin.setter
    def x_margin(self, x_margin):
        if type(x_margin) == int or type(x_margin) == float:
            self._x_margin = (x_margin, x_margin)
        elif type(x_margin) == list or type(x_margin) == tuple:
            if len(x_margin) == 2:
                self._x_margin = x_margin
        elif type(x_margin) == str:
            self._x_margin = x_margin
                
    @property
    def y_margin(self):
        return self._y_margin
    
    @y_margin.setter
    def y_margin(self, y_margin):
        if type(y_margin) == int or type(y_margin) == float:
            self._y_margin = (y_margin, y_margin)
        elif type(y_margin) == list or type(y_margin) == tuple:
            if len(y_margin) == 2:
                self._y_margin = y_margin
        elif type(y_margin) == str:
            self._y_margin = y_margin
        
    def __AutoCalculateSize(self):
        if not self._autosize:
            x_center, y_center = self.CalculateCenter()
            self._x_offset = self.width/2 - x_center
            self._y_offset = self.height/2 - y_center
            
            return
        
        x, y = self._calculated_positions
        
        if len(x) == 0:
            return
        
        min_x = x[0]
        max_x = x[0]
        min_y = y[0]
        max_y = y[0]
        
        bounding_boxes = self.bounding_boxes
        
        if self._autosize_method == "maximum_bounding_box":
            min_position_x = min(x)
            max_position_x = max(x)
            min_position_y = min(y)
            max_position_y = max(y)
            
            max_bounding_box_x = max(list(list(zip(*bounding_boxes))[0]))
            max_bounding_box_y = max(list(list(zip(*bounding_boxes))[1]))
            
            min_x = min_position_x - max_bounding_box_x//2
            max_x = max_position_x + max_bounding_box_x//2
            
            min_y = min_position_y - max_bounding_box_y//2
            max_y = max_position_y + max_bounding_box_y//2
            
        elif self._autosize_method == "tight_fit":
            for i in range(len(x)):
                if (x[i] - bounding_boxes[i][0]//2) < min_x:
                    min_x = x[i] -  bounding_boxes[i][0]//2
                if (x[i] +  bounding_boxes[i][0]//2) > max_x:
                    max_x = x[i] +  bounding_boxes[i][0]//2 
                    
                if (y[i] -  bounding_boxes[i][1]//2) < min_y: 
                    min_y = y[i] -  bounding_boxes[i][1]//2
                if (y[i] +  bounding_boxes[i][1]//2) > max_y: 
                    max_y = y[i] +  bounding_boxes[i][1]//2
                
        self.width = abs(max_x - min_x) + sum(self.x_margin)
        self.height = abs(max_y - min_y) + sum(self.y_margin)
        
        # https://stackoverflow.com/questions/622140/calculate-bounding-box-coordinates-from-a-rotated-rectangle
        # original_width = self.width
        # original_height = self.height
        
        # orientation_radians = self.stim_orientation * (math.pi / 180)
        
        # rotated_width = abs(original_width * math.cos(orientation_radians)) + abs(original_height * math.sin(orientation_radians))
        # rotated_height = abs(original_width * math.sin(orientation_radians)) + abs(original_height * math.cos(orientation_radians))
        
        # self.width = rotated_width
        # self.height = rotated_height
        
        
        # print("min width: %f, max_width: %f"%(min_x, min_y))
        self._x_offset = -min_x + self.x_margin[0]
        self._y_offset = -min_y + self.y_margin[0]
        

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
                self.stim.add(el.generate(self.dwg))
                
    def CalculateCenter(self):
        """
        Calculates the center position based on the location of the elements
        """       
        x, y = self._calculated_positions
        
        self._x_center = sum(x)/len(x)
        self._y_center  = sum(y)/len(y)
        
        return (self._x_center, self._y_center)
        
        
    
    
class Grid(Stimulus):
    _element_attributes = ["_bounding_boxes", "_orientations", "_bordercolors", "_borderwidths", "_fillcolors", "_opacities", "_shapes",
                          "_class_labels", "_id_labels", "_mirror_values", "_data"]
    
    def __init__(self, n_rows, n_cols, row_spacing = 50, col_spacing= 50, background_color = "white", size = None, background_shape = None, mask = None, 
                 stim_orientation = 0, stim_mirror_value = None, stim_class_label = None, stim_id_label = None, x_margin = 20, y_margin = 20):
        # print("Grid constructor")
        super().__init__(background_color = background_color, x_margin = x_margin, y_margin = y_margin, size = size, background_shape = background_shape, mask = mask, 
                         stim_orientation = stim_orientation, stim_mirror_value = stim_mirror_value, stim_class_label = stim_class_label, stim_id_label = stim_id_label)
        
        # Initialize the positions of each element
        self._n_rows = n_rows
        self._n_cols = n_cols
        self.row_spacing = row_spacing
        self.col_spacing = col_spacing
        
        self.positions = Positions.Create2DGrid(n_rows = self._n_rows, n_cols = self._n_cols, row_spacing = self.row_spacing, col_spacing = self.col_spacing)
        
        # Initialize the element attributes to their default values
        self._bounding_boxes = GridPattern.RepeatAcrossElements([(45, 45)], self._n_rows, self._n_cols)
        self._orientations   = GridPattern.RepeatAcrossElements([0], self._n_rows, self._n_cols)
        self._bordercolors   = GridPattern.RepeatAcrossElements([""], self._n_rows, self._n_cols)
        self._borderwidths   = GridPattern.RepeatAcrossElements([0], self.n_rows, self.n_cols)
        self._fillcolors     = GridPattern.RepeatAcrossElements(["dodgerblue"], self.n_rows, self.n_cols)
        self._opacities      = GridPattern.RepeatAcrossElements([1], self.n_rows, self.n_cols)
        self._shapes         = GridPattern.RepeatAcrossElements([Polygon(8)], self._n_rows, self._n_cols)
        self._class_labels   = GridPattern.RepeatAcrossElements([""], self._n_rows, self._n_cols)
        self._id_labels      = GridPattern.RepeatAcrossElements([""], self._n_rows, self._n_cols)
        self._mirror_values  = GridPattern.RepeatAcrossElements([""], self._n_rows, self._n_cols)
        self._data           = GridPattern.RepeatAcrossElements(["8"], self._n_rows, self._n_cols)
        
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
        self.positions = Positions.Create2DGrid(n_rows = self._n_rows, n_cols = self._n_cols, row_spacing = self.row_spacing, col_spacing = self.col_spacing)
        
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
        
        self.positions = Positions.Create2DGrid(n_rows = self._n_rows, n_cols = self._n_cols, row_spacing = self.row_spacing, col_spacing = self.col_spacing)
        
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


        if (self._shapes.generate().patternorientation == "Grid") & (self._shapes.generate().patterntype in ["Tiled", "TiledElement"]):
            
            datalist = []
            patternlist = self._shapes.source_grid.pattern
            
            for i in range(len(patternlist)):
                if patternlist[i] is not None:
                    # add info about subclass generation to "data" argument
                    if str(patternlist[i].__bases__[0]) == "<class 'octa.shapes.Polygon.Polygon_'>":
                        datalist.append(patternlist[i].n_sides)
                    elif str(patternlist[i].__bases__[0]) == "<class 'octa.shapes.RegularPolygon.RegularPolygon_'>":
                        datalist.append(patternlist[i].n_sides)
                    elif str(patternlist[i].__bases__[0]) == "<class 'octa.shapes.Image.Image_'>":
                        datalist.append(patternlist[i].source)
                    elif str(patternlist[i].__bases__[0]) == "<class 'octa.shapes.FitImage.FitImage_'>":
                        datalist.append(patternlist[i].source)
                    elif str(patternlist[i].__bases__[0]) == "<class 'octa.shapes.Text.Text_'>":
                        datalist.append(patternlist[i].text)
                    elif str(patternlist[i].__bases__[0]) == "<class 'octa.shapes.Path.Path_'>":
                        datalist.append([patternlist[i].path, patternlist[i].xsizepath, patternlist[i].ysizepath])
                    elif str(patternlist[i].__bases__[0]) == "<class 'octa.shapes.PathSvg.PathSvg_'>":
                        datalist.append(patternlist[i].source)
                    else:
                        datalist.append("")

            self.data = eval(str(self._shapes.generate().patternclass + self._shapes.generate().patterntype) + str(self._shapes.generate().patternorientation) + "(" + str("GridPattern." + self._shapes.source_grid.patterntype) + str(self._shapes.source_grid.patternorientation) + "(" + str(datalist) + ", " + str(self._shapes.source_grid.n_rows) + ", " + str(self._shapes.source_grid.n_cols) + "), (" + str(int(self._shapes.generate().n_rows/self._shapes.source_grid.n_rows)) + ", " + str(int(self._shapes.generate().n_cols/self._shapes.source_grid.n_cols)) + "))")
        
        elif (self._shapes.generate().patternorientation == "Grid") & (self._shapes.generate().patterntype in ["Layered"]):
            
            datalist = []
            patternlist = self._shapes.center_grid.pattern
            
            for i in range(len(patternlist)):
                if patternlist[i] is not None:
                    # add info about subclass generation to "data" argument
                    if str(patternlist[i].__bases__[0]) == "<class 'octa.shapes.Polygon.Polygon_'>":
                        datalist.append(patternlist[i].n_sides)
                    elif str(patternlist[i].__bases__[0]) == "<class 'octa.shapes.RegularPolygon.RegularPolygon_'>":
                        datalist.append(patternlist[i].n_sides)
                    elif str(patternlist[i].__bases__[0]) == "<class 'octa.shapes.Image.Image_'>":
                        datalist.append(patternlist[i].source)
                    elif str(patternlist[i].__bases__[0]) == "<class 'octa.shapes.FitImage.FitImage_'>":
                        datalist.append(patternlist[i].source)
                    elif str(patternlist[i].__bases__[0]) == "<class 'octa.shapes.Text.Text_'>":
                        datalist.append(patternlist[i].text)
                    elif str(patternlist[i].__bases__[0]) == "<class 'octa.shapes.Path.Path_'>":
                        datalist.append([patternlist[i].path, patternlist[i].xsizepath, patternlist[i].ysizepath])
                    elif str(patternlist[i].__bases__[0]) == "<class 'octa.shapes.PathSvg.PathSvg_'>":
                        datalist.append(patternlist[i].source)
                    else:
                        datalist.append("")

            outerlist = []
            patternlist = self._shapes.outer_layers.pattern
            
            for i in range(len(patternlist)):
                if patternlist[i] is not None:
                    # add info about subclass generation to "data" argument
                    if str(patternlist[i].__bases__[0]) == "<class 'octa.shapes.Polygon.Polygon_'>":
                        outerlist.append(patternlist[i].n_sides)
                    elif str(patternlist[i].__bases__[0]) == "<class 'octa.shapes.RegularPolygon.RegularPolygon_'>":
                        outerlist.append(patternlist[i].n_sides)
                    elif str(patternlist[i].__bases__[0]) == "<class 'octa.shapes.Image.Image_'>":
                        outerlist.append(patternlist[i].source)
                    elif str(patternlist[i].__bases__[0]) == "<class 'octa.shapes.FitImage.FitImage_'>":
                        outerlist.append(patternlist[i].source)
                    elif str(patternlist[i].__bases__[0]) == "<class 'octa.shapes.Text.Text_'>":
                        outerlist.append(patternlist[i].text)
                    elif str(patternlist[i].__bases__[0]) == "<class 'octa.shapes.Path.Path_'>":
                        outerlist.append([patternlist[i].path, patternlist[i].xsizepath, patternlist[i].ysizepath])
                    elif str(patternlist[i].__bases__[0]) == "<class 'octa.shapes.PathSvg.PathSvg_'>":
                        outerlist.append(patternlist[i].source)
                    else:
                        outerlist.append("")

            self.data = eval(str(self._shapes.generate().patternclass + self._shapes.generate().patterntype) + str(self._shapes.generate().patternorientation) + "(" + str(self._shapes.center_grid.patternclass + self._shapes.center_grid.patterntype) + str(self._shapes.center_grid.patternorientation) + "(" + str(datalist) + ", " + str(self._shapes.center_grid.n_rows) + ", " + str(self._shapes.center_grid.n_cols) + "), " + str(self._shapes.outer_layers.patternclass + self._shapes.outer_layers.patterntype + self._shapes.outer_layers.patternorientation) + "(" + str(outerlist) + "))")

        else:
            
            datalist = []
            for i in range(len(self._shapes.pattern)):
                if self._shapes.pattern[i] is not None:
                    # add info about subclass generation to "data" argument
                    if str(self._shapes.pattern[i].__bases__[0]) == "<class 'octa.shapes.Polygon.Polygon_'>":
                        datalist.append(self._shapes.pattern[i].n_sides)
                    elif str(self._shapes.pattern[i].__bases__[0]) == "<class 'octa.shapes.RegularPolygon.RegularPolygon_'>":
                        datalist.append(self._shapes.pattern[i].n_sides)
                    elif str(self._shapes.pattern[i].__bases__[0]) == "<class 'octa.shapes.Image.Image_'>":
                        datalist.append(self._shapes.pattern[i].source)
                    elif str(self._shapes.pattern[i].__bases__[0]) == "<class 'octa.shapes.FitImage.FitImage_'>":
                        datalist.append(self._shapes.pattern[i].source)
                    elif str(self._shapes.pattern[i].__bases__[0]) == "<class 'octa.shapes.Text.Text_'>":
                        datalist.append(self._shapes.pattern[i].text)
                    elif str(self._shapes.pattern[i].__bases__[0]) == "<class 'octa.shapes.Path.Path_'>":
                        datalist.append([self._shapes.pattern[i].path, self._shapes.pattern[i].xsizepath, self._shapes.pattern[i].ysizepath])
                    elif str(self._shapes.pattern[i].__bases__[0]) == "<class 'octa.shapes.PathSvg.PathSvg_'>":
                        datalist.append(self._shapes.pattern[i].source)
                    else:
                        datalist.append("")

            self.data = eval(str(self._shapes.generate().patternclass + self._shapes.generate().patterntype) + str(self._shapes.generate().patternorientation) + "(" + str(datalist) + ")")
 
       
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
        
        if shape_value == None:
            data_value = ""        
        elif str(shape_value.__bases__[0]) == "<class 'octa.shapes.Polygon.Polygon_'>":
            data_value = shape_value.n_sides
        elif str(shape_value.__bases__[0]) == "<class 'octa.shapes.RegularPolygon.RegularPolygon_'>":
            data_value = shape_value.n_sides
        elif str(shape_value.__bases__[0]) == "<class 'octa.shapes.Image.Image_'>":
            data_value = shape_value.source
        elif str(shape_value.__bases__[0]) == "<class 'octa.shapes.FitImage.FitImage_'>":
            data_value = shape_value.source
        elif str(shape_value.__bases__[0]) == "<class 'octa.shapes.Text.Text_'>":
            data_value = shape_value.text
        elif str(shape_value.__bases__[0]) == "<class 'octa.shapes.Path.Path_'>":
            data_value = [shape_value.path, shape_value.xsizepath, shape_value.ysizepath]
        elif str(shape_value.__bases__[0]) == "<class 'octa.shapes.PathSvg.PathSvg_'>":
            data_value = shape_value.source
        else:
            data_value = ""
        
        self._attribute_overrides[element_id]['data'] = data_value
            
        
    def remove_element(self, element_id):
        """
        Removes the shape at position element_id from the display
        
        """
        self.set_element_shape(element_id, None)
        
        
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
    def opacities(self):
        """
        The opacity for each element in the grid.
        
        """
        return self._opacities.generate().pattern
        
    
    @opacities.setter
    def opacities(self, opacities):
        """
        Sets the opacity for each grid element.
        
        If the provided pattern has a fixed grid structure, that structure
        must match the number of rows and columns of the Grid Stimulus
        
        """
        if not self._check_attribute_dimensions(opacities):
            return
        
        self._opacities = opacities
        self._opacities.n_rows = self._n_rows
        self._opacities.n_cols = self._n_cols
        
    def set_element_opacity(self, element_id, opacity_value):
        """
        Sets the opacity of an individual element

        Parameters
        ----------
        element_id : tuple, list or int
            A tuple with the row and column index of the element. A single integer
            can also be used to refer to an element in order.
        opacity_value : 
            numeric value between 0 and 1.

        Returns
        -------
        None.

        """
        element_id = self._parse_element_id(element_id)
        
        self._attribute_overrides[element_id]['opacity'] = opacity_value
                    
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
            
    @property
    def class_labels(self):
        """
        The class labels for each grid element

        """
        return self._class_labels.generate().pattern
    
    @class_labels.setter
    def class_labels(self, class_labels):
        if not self._check_attribute_dimensions(class_labels):
            return
        
        self._class_labels = class_labels
        self._class_labels.n_rows = self._n_rows
        self._class_labels.n_cols = self._n_cols
        
    def set_element_class_label(self, element_id, class_label_value):
        element_id = self._parse_element_id(element_id)
        
        self._attribute_overrides[element_id]['class_labels'] = class_label_value
        
        
    @property
    def id_labels(self):
        """
        The ids for each grid element

        """
        return self._id_labels.generate().pattern
    
    @id_labels.setter
    def id_labels(self, id_labels):
        if not self._check_attribute_dimensions(id_labels):
            return
        
        self._id_labels = id_labels
        self._id_labels.n_rows = self._n_rows
        self._id_labels.n_cols = self._n_cols
        
    def set_element_id_label(self, element_id, id_label_value):
        element_id = self._parse_element_id(element_id)
        
        self._attribute_overrides[element_id]['id_labels'] = id_label_value
        
    
    @property
    def mirror_values(self):
        """
        The mirror value for each grid element

        """
        return self._mirror_values.generate().pattern
    
    @mirror_values.setter
    def mirror_values(self, mirror_values):
        if not self._check_attribute_dimensions(mirror_values):
            return
        
        self._mirror_values = mirror_values
        self._mirror_values.n_rows = self._n_rows
        self._mirror_values.n_cols = self._n_cols
        
    def set_element_mirror_value(self, element_id, mirror_value):
        element_id = self._parse_element_id(element_id)
        
        self._attribute_overrides[element_id]['mirror_values'] = mirror_value
        
        

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
            selected_swap_pairs.append(selected_pair)
            
            removable_positions = set()
            for p in candidate_swap_positions:
                if selected_pair[0] in p or selected_pair[1] in p:
                    removable_positions.add(p)
                    
            candidate_swap_positions.difference_update(removable_positions)
            
        # 3. Perform the swap
        for swap_pair in selected_swap_pairs:
            self._element_presentation_order[swap_pair[0]], self._element_presentation_order[swap_pair[1]] = self._element_presentation_order[swap_pair[1]], self._element_presentation_order[swap_pair[0]]
            
            
    def swap_distinct_elements(self, n_swap_pairs = 1, distinction_features = ['shapes', 'bounding_boxes', 'fillcolors', 'orientations', 'opacities', 'mirror_values', 'class_labels', 'id_labels']):
        """
        Swaps the position of two elements in the pattern. The elements that
        wil be swapped need to be distinct on at least one element feature
        dimension specified in the distinction_features argument. Once 
        an element is used in a swap, it will not be used in subsequent swaps.
        
        
        Parameters
        ----------
        n_swap_pairs: int 
            Number of element pairs that will be swapped. 
        distinction_features: list
            Feature dimensions that will be inspected to decide if two elements
            are the same.

        """
        
        # 0. Create a list of unique fingerprints for each element
        features = dict()
        for f in distinction_features:
            features[f] = getattr(self, f)
        
        element_fingerprints = []
        for idx in range(self.n_cols * self.n_rows):
            fingerprint = "|".join([str(features[f][idx]) for f in distinction_features])
            element_fingerprints.append(fingerprint)
            
        # 1. Generate all available swap positions
        n_elements = self.n_rows * self.n_cols
        
        candidate_swap_positions = set()
        for i in range(n_elements):
            for j in range(i+1, n_elements):
                if element_fingerprints[i] != element_fingerprints[j]:
                    candidate_swap_positions.add((i,j))
        
        # 2. Select the required number of swap positions
        selected_swap_pairs = []
        for i in range(n_swap_pairs):
            assert len(candidate_swap_positions) > 0, "Distinct swaps exhausted, try again with a lower number of pairs"
            selected_pair = random.sample(candidate_swap_positions, 1)[0]
            selected_swap_pairs.append(selected_pair)
            
            removable_positions = set()
            for p in candidate_swap_positions:
                if selected_pair[0] in p or selected_pair[1] in p:
                    removable_positions.add(p)
                    
            candidate_swap_positions.difference_update(removable_positions)
            
        # 3. Perform the swap
        for swap_pair in selected_swap_pairs:
            self._element_presentation_order[swap_pair[0]], self._element_presentation_order[swap_pair[1]] = self._element_presentation_order[swap_pair[1]], self._element_presentation_order[swap_pair[0]]

    def swap_distinct_features(self, n_swap_pairs = 1, feature_dimensions = ['fillcolors']):
        """
        Swaps the position of two element features in the pattern. The element features that
        wil be swapped need to be distinct on the element feature
        dimension specified in the feature_dimensions argument. Once 
        an element is used in a swap, it will not be used in subsequent swaps.
        
        
        Parameters
        ----------
        n_swap_pairs: int 
            Number of element pairs that will be swapped. 
        feature_dimensions: list
            Feature dimensions that will be swapped between the elements.

        """
        
        # 0. Create a list of unique fingerprints for each element
        features = dict()
        for f in feature_dimensions:
            features[f] = getattr(self, f)
        
        element_fingerprints = []
        for idx in range(self.n_cols * self.n_rows):
            fingerprint = "|".join([str(features[f][idx]) for f in feature_dimensions])
            element_fingerprints.append(fingerprint)
            
        # 1. Generate all available swap positions
        n_elements = self.n_rows * self.n_cols
        
        candidate_swap_positions = set()
        for i in range(n_elements):
            for j in range(i+1, n_elements):
                if element_fingerprints[i] != element_fingerprints[j]:
                    candidate_swap_positions.add((i,j))
        
        # 2. Select the required number of swap positions
        selected_swap_pairs = []
        for i in range(n_swap_pairs):
            assert len(candidate_swap_positions) > 0, "Distinct swaps exhausted, try again with a lower number of pairs"
            selected_pair = random.sample(candidate_swap_positions, 1)[0]
            selected_swap_pairs.append(selected_pair)
            
            removable_positions = set()
            for p in candidate_swap_positions:
                if selected_pair[0] in p or selected_pair[1] in p:
                    removable_positions.add(p)
                    
            candidate_swap_positions.difference_update(removable_positions)
            
        # 3. Perform the swap
        for swap_pair in selected_swap_pairs:
            
            swap_element_0 = self._parse_element_id(swap_pair[0])
            swap_element_1 = self._parse_element_id(swap_pair[1])
            
            if 'shapes' in feature_dimensions:
                self._attribute_overrides[swap_element_0]['shape'] , self._attribute_overrides[swap_element_1]['shape'] = self.shapes[swap_pair[1]], self.shapes[swap_pair[0]]
            if 'bounding_boxes' in feature_dimensions:
                self._attribute_overrides[swap_element_0]['bounding_box'] , self._attribute_overrides[swap_element_1]['bounding_box'] = self.bounding_boxes[swap_pair[1]], self.bounding_boxes[swap_pair[0]]
            if 'bordercolors' in feature_dimensions:
                self._attribute_overrides[swap_element_0]['bordercolor'] , self._attribute_overrides[swap_element_1]['bordercolor'] = self.bordercolors[swap_pair[1]], self.bordercolors[swap_pair[0]]
            if 'borderwidths' in feature_dimensions:
                self._attribute_overrides[swap_element_0]['borderwidth'] , self._attribute_overrides[swap_element_1]['borderwidth'] = self.borderwidths[swap_pair[1]], self.borderwidths[swap_pair[0]]
            if 'fillcolors' in feature_dimensions:
                self._attribute_overrides[swap_element_0]['fillcolor'] , self._attribute_overrides[swap_element_1]['fillcolor'] = self.fillcolors[swap_pair[1]], self.fillcolors[swap_pair[0]]
            if 'opacities' in feature_dimensions:
                self._attribute_overrides[swap_element_0]['opacity'] , self._attribute_overrides[swap_element_1]['opacity'] = self.opacities[swap_pair[1]], self.opacities[swap_pair[0]]
            if 'orientations' in feature_dimensions:
                self._attribute_overrides[swap_element_0]['orientation'] , self._attribute_overrides[swap_element_1]['orientation']  = self.orientations[swap_pair[1]], self.orientations[swap_pair[0]]
            if 'data' in feature_dimensions:
                self._attribute_overrides[swap_element_0]['data'] , self._attribute_overrides[swap_element_1]['data']  = self.data[swap_pair[1]], self.data[swap_pair[0]]
            if 'class_labels' in feature_dimensions:
                self._attribute_overrides[swap_element_0]['class_labels'] , self._attribute_overrides[swap_element_1]['class_labels']  = self.class_labels[swap_pair[1]], self.class_labels[swap_pair[0]]
            if 'id_labels' in feature_dimensions:
                self._attribute_overrides[swap_element_0]['id_labels'] , self._attribute_overrides[swap_element_1]['id_labels']  = self.id_labels[swap_pair[1]], self.id_labels[swap_pair[0]]
            if 'mirror_values' in feature_dimensions:
                self._attribute_overrides[swap_element_0]['mirror_values'] , self._attribute_overrides[swap_element_1]['mirror_values']  = self.mirror_values[swap_pair[1]], self.mirror_values[swap_pair[0]]
 
           
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
        