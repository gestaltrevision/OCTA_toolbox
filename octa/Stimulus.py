# -*- coding: utf-8 -*-
"""
Stimulus code for the OCTA toolbox

The Order & Complexity Toolbox for Aesthetics (OCTA) Python library is a tool for researchers 
to create stimuli varying in order and complexity on different dimensions. 
Copyright (C) 2021  Eline Van Geert, Christophe Bossens, and Johan Wagemans

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

Contact: eline.vangeert@kuleuven.be

"""
import svgwrite
import svgutils
import random
import csv
import math
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
from .shapes import Ellipse, Rectangle, Triangle, Polygon
from .shapes.Image import Image_
from .shapes.FitImage import FitImage_
from .shapes.Text import Text_
from .shapes.Polygon import Polygon_
from .shapes.RegularPolygon import RegularPolygon_
from .shapes.Path import Path_
from .shapes.PathSvg import PathSvg_

class Stimulus:
    """ 
    Container class for creating a stimulus.
        
    Parameters
    ----------
    x_margin: int, float, or tuple, optional
        Amount of extra space added to both sides of the stimulus in the x-direction. The default is 20.
    y_margin: int, float, or tuple, optional
        Amount of extra space added to both sides of the stimulus in the y-direction. The default is 20.
    size: tuple, optional
        If specified, fixes the size of the stimulus to the dimension
        given in the tuple. The center of the stimulus will be calculated
        to correspond to the center of all element positions in the
        stimulus.
    background_color: string or list, optional
        Background color of the stimulus. The default is "white".
    background_shape: string or octa.shapes object, optional
        If specified, clips the stimulus to the specified shape (only the part of the stimulus that falls within the 
        background shape will be visible). The center of the background shape 
        will correspond to the center of all element positions in the stimulus.
        If a shape name is provided as string, the boundingbox of the shape will be equal to the stimulus size.
    stim_mask: string or octa.shapes object, optional
        If specified, clips the stimulus to the specified shape. The center of the background shape 
        will correspond to the center of all element positions in the stimulus.
        If a shape name is provided as string, the boundingbox of the shape will be equal to the stimulus size.   
    stim_orientation: int, float, or list, optional
        If not equal to 0, the stimulus will be rotated around its center according to the specified degree value. The default is 0.
    stim_mirrorvalue: string, optional
        If specified, defines the way the stimulus will be mirrored (none, horizontal, vertical, or horizontalvertical).   
    stim_link: string, optional
        If specified, defines the hyperlink that will be activated when the stimulus is clicked.   
    stim_classlabel: string, optional
        If specified, defines the class label that can be used to add javascript or css changes to the stimulus. 
    stim_idlabel: string, optional
        If specified, defines the id label that can be used to add javascript or css changes to the stimulus.        

    """
    
    def __init__(self, x_margin = 20, y_margin = 20, size = None, 
                 background_color = "white", background_shape = None, 
                 stim_mask = None, stim_orientation = 0, stim_mirrorvalue = None, 
                 stim_link = None, stim_classlabel = None, stim_idlabel = None):
        """
        Instantiates a stimulus object.

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
        self.stim_mirrorvalue = stim_mirrorvalue
        self.stim_link = stim_link
        self.stim_classlabel = stim_classlabel
        self.stim_idlabel = stim_idlabel
        
        if background_shape == None:
            self.background_shape = "auto"
        else:
            self.background_shape = background_shape
        
        if stim_mask == None:
            self.stim_mask = "none"
        else:
            self.stim_mask = stim_mask
        
        # Set initial shape parameters to zero
        self.positions   = None

        self._autosize_method = "maximum_boundingbox" # can be 'tight_fit' or 'maximum_boundingbox'
        
        self.dwg_elements = None
        self.dwg = None
        

    def SaveSVG(self, filename, scale = None, folder = None):
        """
        Saves the current stimulus as an SVG file.

        Parameters
        ----------
        filename : string
            Name of the svg file.
        scale : int or float, optional
            Number that indicates the scaling factor to use on the original SVG size.
        folder : string, optional
            Name of the folder in which the svg file needs to be saved.

        """
        
        svg_filename = "%s.svg"%filename
        if folder is not None:
            svg_filename = os.path.join(folder, svg_filename)  
            
        if self.dwg_elements is None:
            self.Render() 
            
        self.dwg.saveas(svg_filename , pretty = True)
        
        if scale is not None:
            originalSVG = svgutils.compose.SVG(svg_filename)
            originalSVG.scale(scale)
            newSVG = svgutils.compose.Figure(float(self.width) * scale, float(self.height) * scale, originalSVG)
            newSVG.save(svg_filename)
            
    def GetSVG(self):
        """
        Gives the current stimulus as an SVG string.

        """
        # if self.dwg_elements is None:
        self.Render() 
            
        return self.dwg.tostring()
    
    def SavePNG(self, filename, scale = None, folder = None): 
        """
        Saves the current stimulus as a PNG file.

        Parameters
        ----------
        filename : string
            Name of the png file.
        scale : int or float, optional
            Number that indicates the scaling factor to use on the original SVG size.
        folder : string, optional
            Name of the folder in which the png file needs to be saved.

        """ 
        # limitations using svglib:
        # clipping is limited to single paths, no mask support
        # color gradients not supported

        svg_filename = "%s_scaled.svg"%filename
        png_filename = "%s.png"%filename
        if folder is not None:
            svg_filename = os.path.join(folder, svg_filename) 
            hti = Html2Image(output_path = folder)
        else:
            hti = Html2Image()
            
        # if self.dwg_elements is None:
        self.Render() 
            
        self.dwg.saveas(svg_filename , pretty = True)
        
        if scale is not None:
            originalSVG = svgutils.compose.SVG(svg_filename)
            originalSVG.scale(scale)
            newSVG = svgutils.compose.Figure(float(self.width) * scale, float(self.height) * scale, originalSVG)
            newSVG.save(svg_filename)
        else:
            scale = 1
            
        hti.screenshot(other_file = svg_filename, 
                       size= (math.ceil(self.width*scale), math.ceil(self.height*scale)), 
                       save_as = png_filename)

        os.remove(svg_filename)
        
    def SavePDF(self, filename, scale = None, folder = None): 
        """
        Saves the current stimulus as a PDF file.

        Parameters
        ----------
        filename : string
            Name of the pdf file.
        scale : int or float, optional
            Number that indicates the scaling factor to use on the original SVG size.
        folder : string, optional
            Name of the folder in which the pdf file needs to be saved.

        """ 
        # limitations using svglib:
        # clipping is limited to single paths, no mask support
        # color gradients not supported
            
        svg_filename = "%s.svg"%filename
        pdf_filename = "%s.pdf"%filename
        if folder is not None:
            svg_filename = os.path.join(folder, svg_filename)  
            pdf_filename = os.path.join(folder, pdf_filename) 
            
        self.Render() 
            
        self.dwg.saveas(svg_filename, pretty = True)
        
        if scale is not None:
            originalSVG = svgutils.compose.SVG(svg_filename)
            originalSVG.scale(scale)
            newSVG = svgutils.compose.Figure(float(self.width) * scale, float(self.height) * scale, originalSVG)
            newSVG.save(svg_filename)
        else:
            scale = 1
            
        img = svg2rlg(svg_filename)
        os.remove(svg_filename)
        renderPDF.drawToFile(img, pdf_filename)
        
        
    def SaveTIFF(self, filename, scale = None, folder = None): 
        """
        Saves the current stimulus as a TIFF file.

        Parameters
        ----------
        filename : string
            Name of the tiff file.
        scale : int or float, optional
            Number that indicates the scaling factor to use on the original SVG size.
        folder : string, optional
            Name of the folder in which the tiff file needs to be saved.

        """ 
        # limitations using svglib:
        # clipping is limited to single paths, no mask support
        # color gradients not supported

        svg_filename = "%s.svg"%filename
        tiff_filename = "%s.tiff"%filename
        if folder is not None:
            svg_filename = os.path.join(folder, svg_filename)  
            hti = Html2Image(output_path = folder)
        else:
            hti = Html2Image()

        self.Render() 
            
        self.dwg.saveas(svg_filename, pretty = True)
        
        if scale is not None:
            originalSVG = svgutils.compose.SVG(svg_filename)
            originalSVG.scale(scale)
            newSVG = svgutils.compose.Figure(float(self.width) * scale, float(self.height) * scale, originalSVG)
            newSVG.save(svg_filename)
        else:
            scale = 1
                  
        hti.screenshot(other_file = svg_filename, 
                       size= (math.ceil(self.width*scale), math.ceil(self.height*scale)), 
                       save_as = tiff_filename)

    def SaveJPG(self, filename, scale = None, folder = None): 
        """
        Saves the current stimulus as a JPG file.

        Parameters
        ----------
        filename : string
            Name of the jpg file.
        scale : int or float, optional
            Number that indicates the scaling factor to use on the original SVG size.
        folder : string, optional
            Name of the folder in which the jpg file needs to be saved.

        """ 
        # limitations using svglib:
        # clipping is limited to single paths, no mask support
        # color gradients not supported

        svg_filename = "%s.svg"%filename
        jpg_filename = "%s.jpg"%filename
        if folder is not None:
            svg_filename = os.path.join(folder, svg_filename)  
            hti = Html2Image(output_path = folder)
        else:
            hti = Html2Image()

        self.Render() 
            
        self.dwg.saveas(svg_filename, pretty = True)
        
        if scale is not None:
            originalSVG = svgutils.compose.SVG(svg_filename)
            originalSVG.scale(scale)
            newSVG = svgutils.compose.Figure(float(self.width) * scale, float(self.height) * scale, originalSVG)
            newSVG.save(svg_filename)
        else:
            scale = 1
                  
        hti.screenshot(other_file = svg_filename, 
                       size= (math.ceil(self.width*scale), math.ceil(self.height*scale)), 
                       save_as = jpg_filename)
        
    def SaveJSON(self, filename, folder = None):
        """
        Saves the current stimulus as a JSON file.

        Parameters
        ----------
        filename : string
            Name of the json file.
        folder : string, optional
            Name of the folder in which the json file needs to be saved.

        """
        json_filename = "%s.json"%filename
        csv_filename = "%s.csv"%filename
        if folder is not None:
            json_filename = os.path.join(folder, json_filename)
            csv_filename  = os.path.join(folder, csv_filename)

        self.Render() 
                    
        json_data = {'stimulus' : {'stimulustype':     str(type(self))[str(type(self)).find("'")+1:str(type(self)).find(">")-1].replace("octa.Stimulus.", ""),
                                   'n_elements'   :    self._n_elements if hasattr(self, '_n_elements') else None,
                                   'n_rows'   :        self._n_rows if hasattr(self, '_n_rows') else None,
                                   'n_cols'   :        self._n_cols if hasattr(self, '_n_cols') else None,
                                   'row_spacing'   :   self.row_spacing if hasattr(self, 'row_spacing') else None,
                                   'col_spacing'   :   self.col_spacing if hasattr(self, 'col_spacing') else None,
                                   'shape'   :         self._shape if hasattr(self, '_shape') else None,
                                   'shape_boundingbox': self._shape_boundingbox if hasattr(self, '_shape_boundingbox') else None,
                                   'autosize_method'   : self._autosize_method,
                                   'x_margin'   :      self.x_margin,
                                   'y_margin'   :      self.y_margin,
                                   'size'       :      self.size,                                   
                                   'width':            self.width,
                                   'height':           self.height,
                                   'background_color': self.background_color,
                                   'background_shape': jsonpickle.encode(self.background_shape),
                                   'stim_mask':        jsonpickle.encode(self.stim_mask),
                                   'stim_orientation': self.stim_orientation,
                                   'stim_mirrorvalue':self.stim_mirrorvalue,
                                   'stim_link'       : self.stim_link,
                                   'stim_classlabel': self.stim_classlabel,
                                   'stim_idlabel':    self.stim_idlabel
                                   },
                     'positions': {'positiontype':          self.positions._position_type,
                                   'positionparameters':    jsonpickle.encode(self.positions._position_parameters),
                                   'jitter':         self.positions._jitter,
                                   'jitterparameters': jsonpickle.encode(self.positions._jitter_parameters),                                   
                                   'deviation':             self.positions._deviation,
                                   'deviationparameters':   jsonpickle.encode(self.positions._deviation_parameters)                                   
                                   },
                     'elements': { 'element_id'   :    jsonpickle.encode(list(range(len(self.dwg_elements)))),
                                   'positions'    :    jsonpickle.encode(self.positions),
                                   'shapes'       :    jsonpickle.encode(self._shapes) if hasattr(self, '_shapes') else jsonpickle.encode(self.shapes),
                                   'boundingboxes' :  jsonpickle.encode(self._boundingboxes) if hasattr(self, '_boundingboxes') else jsonpickle.encode(self.boundingboxes),
                                   'fillcolors'     :  jsonpickle.encode(self._fillcolors) if hasattr(self, '_fillcolors') else jsonpickle.encode(self.fillcolors),
                                   'orientations'  :   jsonpickle.encode(self._orientations) if hasattr(self, '_orientations') else jsonpickle.encode(self.orientations),
                                   'borderwidths'   :  jsonpickle.encode(self._borderwidths) if hasattr(self, '_borderwidths') else jsonpickle.encode(self.borderwidths),
                                   'bordercolors'   :  jsonpickle.encode(self._bordercolors) if hasattr(self, '_bordercolors') else jsonpickle.encode(self.bordercolors),
                                   'opacities'      :  jsonpickle.encode(self._opacities) if hasattr(self, '_opacities') else jsonpickle.encode(self.opacities),
                                   'mirrorvalues'       :    jsonpickle.encode(self._mirrorvalues) if hasattr(self, '_mirrorvalues') else jsonpickle.encode(self.mirrorvalues),
                                   'links'       :      jsonpickle.encode(self._links) if hasattr(self, '_links') else jsonpickle.encode(self.links),
                                   'idlabels'           :    jsonpickle.encode(self._idlabels) if hasattr(self, '_idlabels') else jsonpickle.encode(self.idlabels),
                                   'classlabels'        :    jsonpickle.encode(self._classlabels) if hasattr(self, '_classlabels') else jsonpickle.encode(self.classlabels),
                                   'data'         :    jsonpickle.encode(self._data) if hasattr(self, '_data') else jsonpickle.encode(self.data),
                                   'overrides'    :    jsonpickle.encode(self._attribute_overrides),
                                   'element_order':    jsonpickle.encode(self._element_presentation_order)
                                   }}
        
        with open(json_filename, 'w') as output_file:
            json.dump(json_data, output_file, indent = 4)
        
    def GetElementsDF(self):
        """
        Gets a dataframe with all element information.

        """
        self.Render() 
            
        df = pd.DataFrame(self.dwg_elements, columns = ['element_id', 'position', 'shape', 'boundingbox', 'fillcolor', 'orientation', 'borderwidth', 'bordercolor', 'opacity', 'mirrorvalue', 'link', 'idlabel', 'classlabel', 'data'])
        
        return df
    
    def SaveElementsDF(self, filename, folder = None):
        """
        Saves a dataframe with all element information as CSV file.

        Parameters
        ----------
        filename : string
            Name of the csv file.
        folder : string, optional
            Name of the folder in which the csv file needs to be saved.

        """        
        csv_filename = "%s.csv"%filename
        if folder is not None:
            csv_filename  = os.path.join(folder, csv_filename)
        
        # if self.dwg_elements is None:
        self.Render()  
                             
        df = pd.DataFrame(self.dwg_elements, columns = ['element_id', 'position', 'shape', 'boundingbox', 'fillcolor', 'orientation', 'borderwidth', 'bordercolor', 'opacity', 'mirrorvalue', 'link', 'idlabel', 'classlabel', 'data'])
        df.to_csv(csv_filename, index = False)
   
    def GetJSON(self):
        """
        Gives the JSON info concerning the current stimulus.

        """
        
        self.Render()  
                 
        json_data = {'stimulus' : {'stimulustype':     str(type(self))[str(type(self)).find("'")+1:str(type(self)).find(">")-1].replace("octa.Stimulus.", ""),
                                   'n_elements'   :    self._n_elements if hasattr(self, '_n_elements') else None,
                                   'n_rows'   :        self._n_rows if hasattr(self, '_n_rows') else None,
                                   'n_cols'   :        self._n_cols if hasattr(self, '_n_cols') else None,
                                   'row_spacing'   :   self.row_spacing if hasattr(self, 'row_spacing') else None,
                                   'col_spacing'   :   self.col_spacing if hasattr(self, 'col_spacing') else None,
                                   'shape'   :         self._shape if hasattr(self, '_shape') else None,
                                   'shape_boundingbox': self._shape_boundingbox if hasattr(self, '_shape_boundingbox') else None,
                                   'autosize_method'   : self._autosize_method,
                                   'x_margin'   :      self.x_margin,
                                   'y_margin'   :      self.y_margin,
                                   'size'       :      self.size,                                   
                                   'width':            self.width,
                                   'height':           self.height,
                                   'background_color': self.background_color,
                                   'background_shape': jsonpickle.encode(self.background_shape),
                                   'stim_mask':        jsonpickle.encode(self.stim_mask),
                                   'stim_orientation': self.stim_orientation,
                                   'stim_mirrorvalue':self.stim_mirrorvalue,
                                   'stim_link'       : self.stim_link,
                                   'stim_classlabel': self.stim_classlabel,
                                   'stim_idlabel':    self.stim_idlabel
                                   },
                     'positions': {'positiontype':          self.positions._position_type,
                                   'positionparameters':    jsonpickle.encode(self.positions._position_parameters),
                                   'jitter':         self.positions._jitter,
                                   'jitterparameters': jsonpickle.encode(self.positions._jitter_parameters),                                   
                                   'deviation':             self.positions._deviation,
                                   'deviationparameters':   jsonpickle.encode(self.positions._deviation_parameters)                                   
                                   },
                     'elements': { 'element_id'   :    jsonpickle.encode(list(range(len(self.dwg_elements)))),
                                   'positions'    :    jsonpickle.encode(self.positions),
                                   'shapes'       :    jsonpickle.encode(self._shapes) if hasattr(self, '_shapes') else jsonpickle.encode(self.shapes),
                                   'boundingboxes' :  jsonpickle.encode(self._boundingboxes) if hasattr(self, '_boundingboxes') else jsonpickle.encode(self.boundingboxes),
                                   'fillcolors'     :  jsonpickle.encode(self._fillcolors) if hasattr(self, '_fillcolors') else jsonpickle.encode(self.fillcolors),
                                   'orientations'  :   jsonpickle.encode(self._orientations) if hasattr(self, '_orientations') else jsonpickle.encode(self.orientations),
                                   'borderwidths'   :  jsonpickle.encode(self._borderwidths) if hasattr(self, '_borderwidths') else jsonpickle.encode(self.borderwidths),
                                   'bordercolors'   :  jsonpickle.encode(self._bordercolors) if hasattr(self, '_bordercolors') else jsonpickle.encode(self.bordercolors),
                                   'opacities'      :  jsonpickle.encode(self._opacities) if hasattr(self, '_opacities') else jsonpickle.encode(self.opacities),
                                   'mirrorvalues'       :    jsonpickle.encode(self._mirrorvalues) if hasattr(self, '_mirrorvalues') else jsonpickle.encode(self.mirrorvalues),
                                   'links'       :      jsonpickle.encode(self._links) if hasattr(self, '_links') else jsonpickle.encode(self.links),
                                   'idlabels'           :    jsonpickle.encode(self._idlabels) if hasattr(self, '_idlabels') else jsonpickle.encode(self.idlabels),
                                   'classlabels'        :    jsonpickle.encode(self._classlabels) if hasattr(self, '_classlabels') else jsonpickle.encode(self.classlabels),
                                   'data'         :    jsonpickle.encode(self._data) if hasattr(self, '_data') else jsonpickle.encode(self.data),
                                   'overrides'    :    jsonpickle.encode(self._attribute_overrides),
                                   'element_order':    jsonpickle.encode(self._element_presentation_order)
                                   }}        
        return json_data            
        
    def LoadFromJSON(filename, folder = None):
        """
        Creates a stimulus object from a JSON file.

        Parameters
        ----------
        filename : string
            JSON file that needs to be loaded.
        folder : string, optional
            Name of the folder in which the csv file needs to be saved.

        Returns
        -------
        Stimulus
            A stimulus object with parameters extracted from the JSON file.

        """
        stimulus = None
        
        if folder is not None:
            json_filename  = os.path.join(folder, filename + '.json')
        else:
            json_filename = os.path.join(filename + '.json')
        
        with open(json_filename, 'r') as input_file:
            data = json.load(input_file)
            
            
            # Define stimulus characteristics
            
            if data['stimulus']['size'] == 'auto':
                stimulus_size = None
            else:
                stimulus_size = (data['stimulus']['width'], data['stimulus']['height'])

    
            if data['stimulus']['stimulustype'] == "Grid":
            
                stimulus = Grid(data['stimulus']['n_rows'], 
                                data['stimulus']['n_cols'], 
                                data['stimulus']['row_spacing'],
                                data['stimulus']['col_spacing'], 
                                data['stimulus']['x_margin'], 
                                data['stimulus']['y_margin'],
                                stimulus_size,
                                data['stimulus']['background_color'],
                                jsonpickle.decode(data['stimulus']['background_shape']),
                                jsonpickle.decode(data['stimulus']['stim_mask']),
                                data['stimulus']['stim_orientation'],
                                data['stimulus']['stim_mirrorvalue'],
                                data['stimulus']['stim_link'],
                                data['stimulus']['stim_classlabel'],
                                data['stimulus']['stim_idlabel'])
            
            elif data['stimulus']['stimulustype'] == "Outline":
               stimulus = Outline(data['stimulus']['n_elements'], 
                                data['stimulus']['shape'],
                                data['stimulus']['shape_boundingbox'],
                                data['stimulus']['x_margin'], 
                                data['stimulus']['y_margin'],
                                stimulus_size,
                                data['stimulus']['background_color'],
                                jsonpickle.decode(data['stimulus']['background_shape']),
                                jsonpickle.decode(data['stimulus']['stim_mask']),
                                data['stimulus']['stim_orientation'],
                                data['stimulus']['stim_mirrorvalue'],
                                data['stimulus']['stim_link'],
                                data['stimulus']['stim_classlabel'],
                                data['stimulus']['stim_idlabel'])
                
            elif data['stimulus']['stimulustype'] == "Concentric":
               stimulus = Concentric(data['stimulus']['n_elements'], 
                                data['stimulus']['x_margin'], 
                                data['stimulus']['y_margin'],
                                stimulus_size,
                                data['stimulus']['background_color'],
                                jsonpickle.decode(data['stimulus']['background_shape']),
                                jsonpickle.decode(data['stimulus']['stim_mask']),
                                data['stimulus']['stim_orientation'],
                                data['stimulus']['stim_mirrorvalue'],
                                data['stimulus']['stim_link'],
                                data['stimulus']['stim_classlabel'],
                                data['stimulus']['stim_idlabel'])
               
            else:
               stimulus = Stimulus(                                
                                data['stimulus']['x_margin'], 
                                data['stimulus']['y_margin'],
                                stimulus_size,
                                data['stimulus']['background_color'],
                                jsonpickle.decode(data['stimulus']['background_shape']),
                                jsonpickle.decode(data['stimulus']['stim_mask']),
                                data['stimulus']['stim_orientation'],
                                data['stimulus']['stim_mirrorvalue'],
                                data['stimulus']['stim_link'],
                                data['stimulus']['stim_classlabel'],
                                data['stimulus']['stim_idlabel'])
            
            stimulus._autosize_method = data['stimulus']['autosize_method']
            
            # Define position characteristics                                
            stimulus.positions._position_type       = data['positions']['positiontype']
            stimulus.positions._position_parameters = jsonpickle.decode(data['positions']['positionparameters'])
            stimulus.positions._jitter       = data['positions']['jitter']
            stimulus.positions._jitter_parameters = jsonpickle.decode(data['positions']['jitterparameters'])
            stimulus.positions._deviation           = data['positions']['deviation']
            stimulus.positions._deviation_parameters = jsonpickle.decode(data['positions']['deviationparameters'])

            if stimulus.positions._position_type == "RectGrid":
                stimulus.positions = Positions.CreateRectGrid(n_rows = stimulus.positions._position_parameters['n_rows'], 
                                                            n_cols = stimulus.positions._position_parameters['n_cols'], 
                                                            row_spacing = stimulus.positions._position_parameters['row_spacing'], 
                                                            col_spacing= stimulus.positions._position_parameters['col_spacing'])
            elif stimulus.positions._position_type == "SineGrid":
                stimulus.positions = Positions.CreateSineGrid(n_rows = stimulus.positions._position_parameters['n_rows'], 
                                                              n_cols = stimulus.positions._position_parameters['n_cols'], 
                                                              row_spacing = stimulus.positions._position_parameters['row_spacing'], 
                                                              col_spacing= stimulus.positions._position_parameters['col_spacing'],
                                                              A = stimulus.positions._position_parameters['A'],  
                                                              f = stimulus.positions._position_parameters['f'], 
                                                              axis = stimulus.positions._position_parameters['axis'])
            elif stimulus.positions._position_type == "CustomPositions":
                stimulus.positions = Positions.CreateCustomPositions(x = stimulus.positions._position_parameters['x'].pattern, 
                                                                     y = stimulus.positions._position_parameters['y'].pattern)
            elif stimulus.positions._position_type == "Circle":
                stimulus.positions = Positions.CreateCircle(radius = stimulus.positions._position_parameters['radius'], 
                                                            n_elements = stimulus.positions._position_parameters['n_elements'], 
                                                            starting_point = stimulus.positions._position_parameters['starting_point'])
            elif stimulus.positions._position_type == "Shape":
                stimulus.positions = Positions.CreateShape(n_elements = stimulus.positions._position_parameters['n_elements'], 
                                                           src = stimulus.positions._position_parameters['src'], 
                                                           path = stimulus.positions._position_parameters['path'],  
                                                           width = stimulus.positions._position_parameters['width'], 
                                                           height = stimulus.positions._position_parameters['height'])
            elif stimulus.positions._position_type == "RandomPositions":
                stimulus.positions = Positions.CreateRandomPositions(n_elements = stimulus.positions._position_parameters['n_elements'],  
                                                                     width = stimulus.positions._position_parameters['width'], 
                                                                     height = stimulus.positions._position_parameters['height'],
                                                                     min_distance = stimulus.positions._position_parameters['min_distance'], 
                                                                     max_iterations = stimulus.positions._position_parameters['max_iterations'])
                
           
            # Define element characteristics
            stimulus.positions                   = jsonpickle.decode(data['elements']['positions'])
            stimulus._boundingboxes             = jsonpickle.decode(data['elements']['boundingboxes'])
            stimulus._shapes                     = jsonpickle.decode(data['elements']['shapes'])
            stimulus._fillcolors                 = jsonpickle.decode(data['elements']['fillcolors'])
            stimulus._opacities                  = jsonpickle.decode(data['elements']['opacities'])
            stimulus._bordercolors               = jsonpickle.decode(data['elements']['bordercolors'])
            stimulus._borderwidths               = jsonpickle.decode(data['elements']['borderwidths'])
            stimulus._orientations               = jsonpickle.decode(data['elements']['orientations'])
            stimulus._data                       = jsonpickle.decode(data['elements']['data'])
            stimulus._attribute_overrides        = jsonpickle.decode(data['elements']['overrides'])
            stimulus._element_presentation_order = jsonpickle.decode(data['elements']['element_order'])
            stimulus._idlabels                  = jsonpickle.decode(data['elements']['idlabels'])
            stimulus._classlabels               = jsonpickle.decode(data['elements']['classlabels'])
            stimulus._mirrorvalues              = jsonpickle.decode(data['elements']['mirrorvalues'])
            stimulus._links                      = jsonpickle.decode(data['elements']['links'])
                          
        return stimulus
    
                           
    def Render(self):
        """
        Prepares the SVG stimulus. The stimulus parameters are first parsed, then
        a new drawing is instantiated to which all the individual elements are added.

        """
        self.__CalculateStimulusValues()
        self.__AutoCalculateSize()
        self.__ParseDrawingParameters()
        self.__StartNewDrawing()
        self.__AddDrawingElements()
        
            
    def Show(self):
        """
        Displays the current SVG stimulus in the IPython console window.

        """
        
        self.Render()             
        display(SVG(self.dwg.tostring()))
            
        
    def __CalculateStimulusValues(self):
        """
        Gets the actual element positions and adds them to the stimulus properties.

        """
        self._calculated_positions = self.positions.GetPositions()
        
    def __ParseDrawingParameters(self):
        """
        Uses the stimulus parameter properties to create a dictionary with
        parameters for each individual shape.

        """
        self.dwg_elements = []
        
        boundingboxes = self.boundingboxes
        fillcolors     = self.fillcolors
        opacities      = self.opacities
        bordercolors   = self.bordercolors
        borderwidths   = self.borderwidths
        orientations   = self.orientations
        datas          = self.data
        shapes         = self.shapes
        idlabels      = self.idlabels
        classlabels   = self.classlabels
        mirrorvalues  = self.mirrorvalues
        links          = self.links
        x, y           = self._calculated_positions
        
        for i in range(len(self._element_presentation_order)):
            idx = self._element_presentation_order[i]
                   
            x_i           = x[i] + self._x_offset
            y_i           = y[i] + self._y_offset
            
            if 'boundingbox' in self._attribute_overrides[idx]:
                boundingbox = self._attribute_overrides[idx]['boundingbox']
            else:
                boundingbox = boundingboxes[idx]
                
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
                
            if 'mirrorvalues' in self._attribute_overrides[idx]:
                mirrorvalue = self._attribute_overrides[idx]['mirrorvalues']
            else:
                mirrorvalue = mirrorvalues[idx]
                
            if 'links' in self._attribute_overrides[idx]:
                link = self._attribute_overrides[idx]['links']
            else:
                link = links[idx]
                
            if 'classlabels' in self._attribute_overrides[idx]:
                classlabel = self._attribute_overrides[idx]['classlabels']
            else:
                classlabel = classlabels[idx]
                
            if 'idlabels' in self._attribute_overrides[idx]:
                idlabel = self._attribute_overrides[idx]['idlabels']
            else:
                idlabel = idlabels[idx]
                
            element_parameters = {'element_id'   : i,
                                  'position'     : (x_i, y_i), 
                                  'shape'        : shape, 
                                  'boundingbox' : boundingbox, 
                                  'fillcolor'    : fillcolor,
                                  'orientation'  : orientation,
                                  'borderwidth'  : borderwidth,
                                  'bordercolor'  : bordercolor,
                                  'opacity'      : opacity, 
                                  'mirrorvalue' : mirrorvalue,
                                  'link'         : link,
                                  'classlabel'  : classlabel,
                                  'idlabel'     : idlabel,
                                  'data'         : data}
            
            self.dwg_elements.append(element_parameters)
                        
            
    def __StartNewDrawing(self):        
        """
        Instantiates a new drawing canvas to which elements can be added. Executing
        this function will result in a blank canvas with the provided size and
        stimulus characteristics.

        """           
        self.dwg = svgwrite.Drawing(size = (self.width, self.height)) 

        # ADD CLIP PATH
        if(self.background_shape != "auto"):
            self.clip_path = self.dwg.defs.add(self.dwg.clipPath(id='custom_clip_path'))
            if type(self.background_shape) == str:
                if self.background_shape == "Ellipse":
                    self.background_shape = Ellipse(position = (self.width/2,self.height/2), boundingbox = (self.width,self.height))
                elif self.background_shape == "Rectangle":
                    self.background_shape = Rectangle(position = (self.width/2,self.height/2), boundingbox = (self.width,self.height))
                elif self.background_shape == "Triangle":
                    self.background_shape = Triangle(position = (self.width/2,self.height/2), boundingbox = (self.width,self.height))
                elif "FitImage" in self.background_shape:
                    self.background_shape = self.background_shape.replace(" ", "")
                    src = self.background_shape[:self.background_shape.find(")")-1]
                    self.background_shape = FitImage_(position = (self.width/2,self.height/2), boundingbox = (self.width,self.height), data = src)
                elif "Image" in self.background_shape:
                    self.background_shape = self.background_shape.replace(" ", "")
                    src = self.background_shape[self.background_shape.find("(")+2:self.background_shape.find(")")-1]
                    self.background_shape = Image_(position = (self.width/2,self.height/2), boundingbox = (self.width,self.height), data = src)
                elif "Text" in self.background_shape:
                    self.background_shape = self.background_shape.replace(" ", "")
                    text = self.background_shape[self.background_shape.find("(")+2:self.background_shape.find(")")-1]
                    self.background_shape = Text_(position = (self.width/2,self.height/2), boundingbox = (self.width,self.height), data = text)
                elif "RegularPolygon" in self.background_shape:
                    n_sides = self.background_shape[self.background_shape.find("(")+1:self.background_shape.find(")")]
                    self.background_shape = RegularPolygon_(position = (self.width/2,self.height/2), boundingbox = (self.width,self.height), data = n_sides)
                elif "Polygon" in self.background_shape:
                    n_sides = self.background_shape[self.background_shape.find("(")+1:self.background_shape.find(")")]
                    self.background_shape = Polygon_(position = (self.width/2,self.height/2), boundingbox = (self.width,self.height), data = n_sides)
                elif "PathSvg" in self.background_shape:
                    self.background_shape = self.background_shape.replace(" ", "")
                    src = self.background_shape[self.background_shape.find("(")+2:self.background_shape.find(")")-1]
                    self.background_shape = PathSvg_(position = (self.width/2,self.height/2), boundingbox = (self.width,self.height), data = src)
                elif "Path" in self.background_shape:
                    self.background_shape = self.background_shape.replace(" ", "")
                    data = self.background_shape[self.background_shape.find("(")+1:self.background_shape.find(")")]
                    path = [ '"{}"'.format(x) for x in list(csv.reader([data], delimiter=',', quotechar='"'))[0]][0].replace(" ", "")
                    xsize = int([ '"{}"'.format(x) for x in list(csv.reader([data], delimiter=',', quotechar='"'))[0]][1].replace(" ", "").replace('"','').replace("'",''))
                    ysize = int([ '"{}"'.format(x) for x in list(csv.reader([data], delimiter=',', quotechar='"'))[0]][2].replace(" ", "").replace('"','').replace("'",''))
                    data = [path, xsize, ysize]
                    self.background_shape = Path_(position = (self.width/2,self.height/2), boundingbox = (self.width,self.height), data = data)
                else:
                    self.background_shape.position = (self.width/2,self.height/2)
            else:
                self.background_shape.position = (self.width/2,self.height/2)
            self.clip_path.add(self.background_shape.generate(self.dwg)) #things inside this shape will be drawn
            clippath = "url(#custom_clip_path)"
        else:
            clippath = None
            
        # ADD stim_mask
        if(self.stim_mask != "none"):
            self.stim_mask_object = self.dwg.defs.add(self.dwg.mask(id='custom_stim_mask'))
            self.stim_mask.position = (self.width/2,self.height/2)
            self.stim_mask_object.add(self.stim_mask.generate(self.dwg))
            maskpath = "url(#custom_stim_mask)"
            
            if clippath != None:
                self.stim = self.dwg.g(clip_path = clippath, mask = maskpath)
            else:
                self.stim = self.dwg.g(mask = maskpath)
                
        else:
            maskpath = None
            
            if clippath != None:            
                self.stim = self.dwg.g(clip_path = clippath)
            else:            
                self.stim = self.dwg.g()
                
            
        # ADD MIRROR VALUE  
        mirror_transform = ""
        if self.stim_mirrorvalue == "vertical":
            mirror_transform = "scale(-1, 1) translate(%f, 0)"%(-2*(self.width/2))
        elif self.stim_mirrorvalue == "horizontal":
            mirror_transform = "scale(1, -1), translate(0, %f)"%(-2*(self.height/2))
        elif self.stim_mirrorvalue == "horizontalvertical":
            mirror_transform = "scale(-1, -1) translate(%f, %f)"%(-2*(self.width/2), -2*(self.height/2))

        # ADD ROTATION
        rotation_transform = ""
        self.rotation_animation = ""
        if (type(self.stim_orientation) == int) or (type(self.stim_orientation) == float):
            rotation_transform = "rotate(%d, %d, %d)"%(self.stim_orientation, self.width/2, self.height/2)
        elif type(self.stim_orientation) == list:
            self.rotation_animation = "svgwrite.animate.AnimateTransform('rotate','transform', from_= '" + str(self.stim_orientation[1]) + " " + str(self.width/2) + " " + str(self.height/2) + "', to = '" + str(self.stim_orientation[2]) + " " + str(self.width/2) + " " + str(self.height/2) + "', " + self.stim_orientation[3] + ")"
            rotation_transform = "rotate(%d, %d, %d)"%(int(self.stim_orientation[1]), self.width/2, self.height/2)
            
        if (mirror_transform != "") | (rotation_transform != ""):
            self.stim['transform'] = " ".join([mirror_transform, rotation_transform])
                        
        # ADD GROUP OF ELEMENTS TO DRAWING
        self.dwg.add(self.stim)
          
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
            
        if self.stim_classlabel != None:
            self.stim['class']         = self.stim_classlabel
        if self.stim_idlabel != None:
            self.stim['id']        = self.stim_idlabel
        
        if self.rotation_animation != "":
            self.stim.add(eval(self.rotation_animation))  
           
        if self.stim_link != None:       
            link = 'self.dwg.add(self.dwg.a(href = "' + str(self.stim_link) + '", target="_blank"' + '))'
            self.stim = eval(link).add(self.stim)
            
    @property
    def x_margin(self):
        """
        The horizontal margin in the stimulus
        
        """
        return self._x_margin
    
    @x_margin.setter
    def x_margin(self, x_margin):
        """
        Sets the horizontal margin in the stimulus
        
        Parameters
        ----------
        x_margin: int, float, or tuple
            Amount of extra space added to both sides of the stimulus in the x-direction.

        """
        if type(x_margin) == int or type(x_margin) == float:
            self._x_margin = (x_margin, x_margin)
        elif type(x_margin) == list or type(x_margin) == tuple:
            if len(x_margin) == 2:
                self._x_margin = x_margin
        elif type(x_margin) == str:
            self._x_margin = x_margin
                
    @property
    def y_margin(self):
        """
        The vertical margin in the stimulus
        
        """
        return self._y_margin
    
    @y_margin.setter
    def y_margin(self, y_margin):
        """
        Sets the vertical margin in the stimulus
        
        Parameters
        ----------
        y_margin: int, float, or tuple
            Amount of extra space added to both sides of the stimulus in the y-direction. 
        
        """
        if type(y_margin) == int or type(y_margin) == float:
            self._y_margin = (y_margin, y_margin)
        elif type(y_margin) == list or type(y_margin) == tuple:
            if len(y_margin) == 2:
                self._y_margin = y_margin
        elif type(y_margin) == str:
            self._y_margin = y_margin
        
    def __AutoCalculateSize(self):
        """
        Calculates the automatic size of the svg drawing.

        """  
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
        
        boundingboxes = self.boundingboxes
        
        if self._autosize_method == "maximum_boundingbox":
            min_position_x = min(x)
            max_position_x = max(x)
            min_position_y = min(y)
            max_position_y = max(y)
            
            max_boundingbox_x = max(list(list(zip(*boundingboxes))[0]))
            max_boundingbox_y = max(list(list(zip(*boundingboxes))[1]))
            
            min_x = min_position_x - max_boundingbox_x//2
            max_x = max_position_x + max_boundingbox_x//2
            
            min_y = min_position_y - max_boundingbox_y//2
            max_y = max_position_y + max_boundingbox_y//2
            
        elif self._autosize_method == "tight_fit":
            for i in range(len(x)):
                if (x[i] - boundingboxes[i][0]//2) < min_x:
                    min_x = x[i] -  boundingboxes[i][0]//2
                if (x[i] +  boundingboxes[i][0]//2) > max_x:
                    max_x = x[i] +  boundingboxes[i][0]//2 
                    
                if (y[i] -  boundingboxes[i][1]//2) < min_y: 
                    min_y = y[i] -  boundingboxes[i][1]//2
                if (y[i] +  boundingboxes[i][1]//2) > max_y: 
                    max_y = y[i] +  boundingboxes[i][1]//2
                
        self.width = abs(max_x - min_x) + sum(self.x_margin)
        self.height = abs(max_y - min_y) + sum(self.y_margin)
        
        self._x_offset = -min_x + self.x_margin[0]
        self._y_offset = -min_y + self.y_margin[0]
        

    def __AddDrawingElements(self):
        """
        Adds the provided stimulus elements to the svg drawing.

        """                
        for i in range(len(self.dwg_elements)):
            if not self.dwg_elements[i]['shape'] == None:
                el = self.dwg_elements[i]['shape'](**self.dwg_elements[i])
                self.stim.add(el.generate(self.dwg))
                
    def CalculateCenter(self):
        """
        Calculates the center position based on the position of the elements
        """       
        x, y = self._calculated_positions
        
        self._x_center = sum(x)/len(x)
        self._y_center  = sum(y)/len(y)
        
        return (self._x_center, self._y_center)
        
        
    
    
class Grid(Stimulus):
    """ Class for creating a Grid stimulus.
    
    """
    _element_attributes = ["_boundingboxes", "_orientations", "_bordercolors", "_borderwidths", "_fillcolors", "_opacities", "_shapes",
                          "_classlabels", "_idlabels", "_mirrorvalues", "_links" ,"_data"]
    
    def __init__(self, n_rows, n_cols, row_spacing = 50, col_spacing= 50, 
                 x_margin = 20, y_margin = 20, size = None, 
                 background_color = "white", background_shape = None, 
                 stim_mask = None, stim_orientation = 0, stim_mirrorvalue = None, 
                 stim_link = None, stim_classlabel = None, stim_idlabel = None):
        """
        Instantiates a Grid stimulus object.

        Parameters
        ----------
        n_rows: int
            Number of rows in the stimulus. 
        n_cols: int
            Number of columns in the stimulus. 
        row_spacing: int or float, optional
            Amount of space between two rows (element positions in the y-direction). The default is 50.
        col_spacing: int or float, optional
            Amount of space between two columns (element positions in the x-direction). The default is 50.
        x_margin: int, float, or tuple, optional
            Amount of extra space added to both sides of the stimulus in the x-direction. The default is 20.
        y_margin: int, float, or tuple, optional
            Amount of extra space added to both sides of the stimulus in the y-direction. The default is 20.
        size: tuple, optional
            If specified, fixes the size of the stimulus to the dimension
            given in the tuple. The center of the stimulus will be calculated
            to correspond to the center of all element positions in the
            stimulus.
        background_color: string or list, optional
            Background color of the stimulus. The default is "white".
        background_shape: string or octa.shapes object, optional
            If specified, clips the stimulus to the specified shape (only the part of the stimulus that falls within the 
            background shape will be visible). The center of the background shape 
            will correspond to the center of all element positions in the stimulus.
            If a shape name is provided as string, the boundingbox of the shape will be equal to the stimulus size.
        stim_mask: string or octa.shapes object, optional
            If specified, clips the stimulus to the specified shape. The center of the background shape 
            will correspond to the center of all element positions in the stimulus.
            If a shape name is provided as string, the boundingbox of the shape will be equal to the stimulus size.   
        stim_orientation: int, float, or list, optional
            If not equal to 0, the stimulus will be rotated around its center according to the specified degree value. The default is 0.
        stim_mirrorvalue: string, optional
            If specified, defines the way the stimulus will be mirrored (none, horizontal, vertical, or horizontalvertical).   
        stim_link: string, optional
            If specified, defines the hyperlink that will be activated when the stimulus is clicked.   
        stim_classlabel: string, optional
            If specified, defines the class label that can be used to add javascript or css changes to the stimulus. 
        stim_idlabel: string, optional
            If specified, defines the id label that can be used to add javascript or css changes to the stimulus.        

        """

        super().__init__(x_margin = x_margin, y_margin = y_margin, size = size, 
                         background_color = background_color, background_shape = background_shape, 
                         stim_mask = stim_mask, stim_orientation = stim_orientation, stim_mirrorvalue = stim_mirrorvalue, 
                         stim_link = stim_link, stim_classlabel = stim_classlabel, stim_idlabel = stim_idlabel)
        
        # Initialize the positions of each element
        self._n_rows = n_rows
        self._n_cols = n_cols
        self._n_elements = n_rows * n_cols
        self.row_spacing = row_spacing
        self.col_spacing = col_spacing
        
        self.positions = Positions.CreateRectGrid(n_rows = self._n_rows, n_cols = self._n_cols, row_spacing = self.row_spacing, col_spacing = self.col_spacing)
        
        # Initialize the element attributes to their default values
        self._boundingboxes = GridPattern.RepeatAcrossElements([(45, 45)], self._n_rows, self._n_cols)
        self._orientations   = GridPattern.RepeatAcrossElements([0], self._n_rows, self._n_cols)
        self._bordercolors   = GridPattern.RepeatAcrossElements([""], self._n_rows, self._n_cols)
        self._borderwidths   = GridPattern.RepeatAcrossElements([0], self.n_rows, self.n_cols)
        self._fillcolors     = GridPattern.RepeatAcrossElements(["dodgerblue"], self.n_rows, self.n_cols)
        self._opacities      = GridPattern.RepeatAcrossElements([1], self.n_rows, self.n_cols)
        self._shapes         = GridPattern.RepeatAcrossElements([Polygon(8)], self._n_rows, self._n_cols)
        self._classlabels   = GridPattern.RepeatAcrossElements([""], self._n_rows, self._n_cols)
        self._idlabels      = GridPattern.RepeatAcrossElements([""], self._n_rows, self._n_cols)
        self._mirrorvalues  = GridPattern.RepeatAcrossElements([""], self._n_rows, self._n_cols)
        self._links          = GridPattern.RepeatAcrossElements([""], self._n_rows, self._n_cols)
        self._data           = GridPattern.RepeatAcrossElements(["8"], self._n_rows, self._n_cols)
        
        # Initialize a list with element attribute overrides
        self._attribute_overrides = [dict() for _ in range(self._n_cols * self._n_rows)]
        self._element_presentation_order = list(range(self._n_cols * self._n_rows))
        
    @property
    def n_elements(self):
        """
        The number of elements in the Grid
        
        """
        return self._n_elements
        
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
        
        This only works if none of the element attributes has a fixed grid
        structure.
        
        Parameters
        ----------
        n_rows: int
            Number of rows in the stimulus.
        """
        if not self._is_modifiable():
            print("WARNING: At least one element attribute has a fixed structure. n_rows remains unchanged.")
            return
        
        self._n_rows = n_rows
        self.positions = Positions.CreateRectGrid(n_rows = self._n_rows, n_cols = self._n_cols, row_spacing = self.row_spacing, col_spacing = self.col_spacing)
        
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
        Sets the number of columns in the Grid.
        
        This only works if none of the element attributes has a fixed grid
        structure.
        
        Parameters
        ----------
        n_cols: int
            Number of columns in the stimulus. 
            
        """
        if not self._is_modifiable():
            print("WARNING: At least one element attribute has a fixed structure. n_rows remains unchanged.")
            return
        
        self._n_cols = n_cols
        
        self.positions = Positions.CreateRectGrid(n_rows = self._n_rows, n_cols = self._n_cols, row_spacing = self.row_spacing, col_spacing = self.col_spacing)
        
        self._attribute_overrides = [dict() for _ in range(self._n_cols * self._n_rows)]
        self._element_presentation_order = list(range(self._n_cols * self._n_rows))
        
        for attr in Grid._element_attributes:
            setattr(getattr(self, attr), 'n_cols', self._n_cols)
        
        
    @property
    def boundingboxes(self):
        """
        The size for each element in the grid.
        
        The size is defined in terms of a rectangular boundingbox that
        contains the element.
        
        """
        return self._boundingboxes.generate().pattern
    
    
    @boundingboxes.setter
    def boundingboxes(self, boundingboxes):
        """
        Sets the boundingbox size for each grid element.
        
        If the provided pattern has a fixed grid structure, that structure
        must match the number of rows and columns of the Grid stimulus   
                
        Parameters
        ----------
        boundingboxes: list
            A list of boundingbox values equal in length to the number of elements in the position pattern of the stimulus.
                   
        """
        if not self._check_attribute_dimensions(boundingboxes):
            return
            
        self._boundingboxes = boundingboxes
        self._boundingboxes.n_rows = self._n_rows
        self._boundingboxes.n_cols = self._n_cols
        
    
    def set_element_boundingbox(self, element_id, boundingbox_value):
        """
        Sets the boundingbox value for an individual element
        
        Parameters
        ----------
        element_id : int, tuple, or list
            A single integer referring to the element's index value (element number),
            or a tuple or list with the row and column index of the element. 
        boundingbox_value: int, float, or tuple
            The new boundingbox value to apply to the element.
            
        """
        element_id = self._parse_element_id(element_id)
        boundingbox_value = Grid._check_boundingbox_value(boundingbox_value)                
        self._attribute_overrides[element_id]['boundingbox'] = boundingbox_value
        
    def set_element_boundingboxes(self, boundingbox_value, element_id = None, n_changes = None):
        """
        Sets the boundingbox value for a series of individual elements
        
        Parameters
        ----------
        boundingbox_value: int, float, tuple, or list
            The new boundingbox value(s) to apply to the specified elements.        
        element_id : int, tuple, or list, optional
            A single integer referring to the element's index value (element number),
            or a tuple or list with the row and column index of the element,
            or a list of several element ids 
        n_changes: int, optional  
            The number of randomly chosen elements to change in the stimulus.
            
        """  
        if element_id is not None:
            if type(element_id) == int:
                element_id = [element_id]
            n_changes = len(element_id)
            boundingbox_value = Pattern(boundingbox_value).RepeatPatternToSize(n_changes).pattern
        elif n_changes is not None:
            n_changes = n_changes
            boundingbox_value = Pattern(boundingbox_value).RepeatPatternToSize(n_changes).pattern
        else:
            if type(boundingbox_value) is not list:
                boundingbox_value = [boundingbox_value]
            n_changes = len(boundingbox_value)
        
        n_elements = self._n_rows * self._n_cols
        assert n_elements >= n_changes, "Maximum number of boundingbox changes reached, try again with a lower number of elements"
               
        # 1. Sample n element ids to change
        if element_id is None:
            changes = random.sample(range(n_elements), n_changes)
        else:
            changes = element_id
            
        # 2. Change elements
        for i in range(len(changes)):
            self.set_element_boundingbox(element_id = changes[i], boundingbox_value = boundingbox_value[i])
        
    def _check_boundingbox_value(boundingbox_value):
        """
        Inspects the boundingbox_value and raises an error when the format
        of this value is not correct
        
        Returns
        -------
        boundingbox_value: tuple
            A valid boundingbox_value
        """
        assert type(boundingbox_value) == list or type(boundingbox_value) == tuple or type(boundingbox_value) == int, "Bounding box value must be int, list or tuple"
        
        if type(boundingbox_value) == list or type(boundingbox_value) == tuple:
            assert len(boundingbox_value) == 2, "Bounding box collection can only contain two values"
        else:
            boundingbox_value = (boundingbox_value, boundingbox_value)
            
        return boundingbox_value
          
        
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
        must match the number of rows and columns of the Grid stimulus
                 
        Parameters
        ----------
        shapes: list
            A list of shape values equal in length to the number of elements in the position pattern of the stimulus.
                   
        """
        if not self._check_attribute_dimensions(shapes):
            return
            
        self._shapes = shapes
        self._shapes.n_rows = self._n_rows
        self._shapes.n_cols = self._n_cols


        if (self._shapes.generate().patterndirection == "Grid") & (self._shapes.generate().patterntype in ["Tiled", "TiledElement"]):
            
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

            self.data = eval(str(self._shapes.generate().patternclass + self._shapes.generate().patterntype) + str(self._shapes.generate().patterndirection) + "(" + str("GridPattern." + self._shapes.source_grid.patterntype) + str(self._shapes.source_grid.patterndirection) + "(" + str(datalist) + ", " + str(self._shapes.source_grid.n_rows) + ", " + str(self._shapes.source_grid.n_cols) + "), (" + str(int(self._shapes.generate().n_rows/self._shapes.source_grid.n_rows)) + ", " + str(int(self._shapes.generate().n_cols/self._shapes.source_grid.n_cols)) + "))")
        
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

            self.data = eval(str(self._shapes.generate().patternclass + self._shapes.generate().patterntype) + str(self._shapes.generate().patterndirection) + "(" + str(datalist) + ")")
 
       
    def set_element_shape(self, element_id, shape_value):
        """
        Sets the shape of an individual element

        Parameters
        ----------
        element_id : int, tuple, or list
            A single integer referring to the element's index value (element number),
            or a tuple or list with the row and column index of the element. 
        shape_value : Shape or None
            An element shape, or None if no shape needs to be displayed.

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
            
    def set_element_shapes(self, shape_value, element_id = None, n_changes = None):
        """
        Sets the shapes of a series of individual elements
        
        Parameters
        ----------
        shape_value: Shape, None, or list
            The new shape value(s) to apply to the specified elements.        
        element_id : int, tuple, or list, optional
            A single integer referring to the element's index value (element number),
            or a tuple or list with the row and column index of the element,
            or a list of several element ids 
        n_changes: int, optional  
            The number of randomly chosen elements to change in the stimulus.
            
        """  
        if element_id is not None:
            if type(element_id) == int:
                element_id = [element_id]
            n_changes = len(element_id)
            shape_value = Pattern(shape_value).RepeatPatternToSize(n_changes).pattern
        elif n_changes is not None:
            n_changes = n_changes
            shape_value = Pattern(shape_value).RepeatPatternToSize(n_changes).pattern
        else:
            if type(shape_value) is not list:
                shape_value = [shape_value]
            n_changes = len(shape_value)
        
        n_elements = self._n_rows * self._n_cols
        assert n_elements >= n_changes, "Maximum number of shape changes reached, try again with a lower number of elements"
               
        # 1. Sample n element ids to change
        if element_id is None:
            changes = random.sample(range(n_elements), n_changes)
        else:
            changes = element_id
            
        # 2. Change elements
        for i in range(len(changes)):
            self.set_element_shape(element_id = changes[i], shape_value = shape_value[i])
        
    def remove_element(self, element_id):
        """
        Removes the shape at position element_id from the display
        
        Parameters
        ----------       
        element_id : int, tuple, or list, optional
            A single integer referring to the element's index value (element number),
            or a tuple or list with the row and column index of the element. 
        
        """
        self.set_element_shape(element_id, None)
        
    def remove_elements(self, n_removals = 0, element_id = None):
        """
        Removes the shape of a series of individual elements
        
        Parameters
        ----------
        n_removals: int, optional  
            The number of randomly chosen elements to remove in the stimulus. Default value is 0.      
        element_id : int, tuple, or list, optional
            A single integer referring to the element's index value (element number),
            or a tuple or list with the row and column index of the element,
            or a list of several element ids
            
        """
        if element_id is not None:
            if type(element_id) == int:
                element_id = [element_id]
            n_removals = len(element_id)
        
        n_elements = self._n_rows * self._n_cols
        assert n_elements >= n_removals, "Maximum number of removals reached, try again with a lower number of removals"
               
        # 1. Sample n element ids to remove
        if element_id is None:
            removals = random.sample(range(n_elements), n_removals)
        else:
            removals = element_id
            
        # 2. Remove elements
        for element in removals:
            self.remove_element(element_id = element)
        
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
        must match the number of rows and columns of the Grid stimulus
        
        Parameters
        ----------
        bordercolors: list
            A list of bordercolor values equal in length to the number of elements in the position pattern of the stimulus.

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
            A single integer referring to the element's index value (element number),
            or a tuple or list with the row and column index of the element. 
        bordercolor_value : string or list
            Color string, or a list for animated colors.

        """
        element_id = self._parse_element_id(element_id)
        
        self._attribute_overrides[element_id]['bordercolor'] = bordercolor_value
        
    def set_element_bordercolors(self, bordercolor_value, element_id = None, n_changes = None):
        """
        Sets the bordercolors of a series of individual elements
        
        Parameters
        ----------
        bordercolor_value: string or list
            The new bordercolor value(s) to apply to the specified elements.        
        element_id : int, tuple, or list, optional
            A single integer referring to the element's index value (element number),
            or a tuple or list with the row and column index of the element,
            or a list of several element ids 
        n_changes: int, optional  
            The number of randomly chosen elements to change in the stimulus.
            
        """  
 
        if element_id is not None:
            if type(element_id) == int:
                element_id = [element_id]
            n_changes = len(element_id)
            bordercolor_value = Pattern(bordercolor_value).RepeatPatternToSize(n_changes).pattern
        elif n_changes is not None:
            n_changes = n_changes
            bordercolor_value = Pattern(bordercolor_value).RepeatPatternToSize(n_changes).pattern
        else:
            if type(bordercolor_value) is not list:
                bordercolor_value = [bordercolor_value]
            n_changes = len(bordercolor_value)
        
        n_elements = self._n_rows * self._n_cols
        assert n_elements >= n_changes, "Maximum number of bordercolor changes reached, try again with a lower number of elements"
               
        # 1. Sample n element ids to change
        if element_id is None:
            changes = random.sample(range(n_elements), n_changes)
        else:
            changes = element_id
            
        # 2. Change elements
        for i in range(len(changes)):
            self.set_element_bordercolor(element_id = changes[i], bordercolor_value = bordercolor_value[i])
            
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
        must match the number of rows and columns of the Grid stimulus
        
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
        element_id : int, tuple, or list
            A single integer referring to the element's index value (element number),
            or a tuple or list with the row and column index of the element. 
        fillcolor_value : string or list
            Color string, or a list for animated colors.

        """
        element_id = self._parse_element_id(element_id)
        
        self._attribute_overrides[element_id]['fillcolor'] = fillcolor_value
        
    def set_element_fillcolors(self, fillcolor_value, element_id = None, n_changes = None):
        """
        Sets the fillcolors of a series of individual elements
        
        Parameters
        ----------
        fillcolor_value: string or list
            The new fillcolor value(s) to apply to the specified elements.        
        element_id : int, tuple, or list, optional
            A single integer referring to the element's index value (element number),
            or a tuple or list with the row and column index of the element,
            or a list of several element ids 
        n_changes: int, optional  
            The number of randomly chosen elements to change in the stimulus.

        """  
 
        if element_id is not None:
            if type(element_id) == int:
                element_id = [element_id]
            n_changes = len(element_id)
            fillcolor_value = Pattern(fillcolor_value).RepeatPatternToSize(n_changes).pattern
        elif n_changes is not None:
            n_changes = n_changes
            fillcolor_value = Pattern(fillcolor_value).RepeatPatternToSize(n_changes).pattern
        else:
            if type(fillcolor_value) is not list:
                fillcolor_value = [fillcolor_value]
            n_changes = len(fillcolor_value)
        
        n_elements = self._n_rows * self._n_cols
        assert n_elements >= n_changes, "Maximum number of fillcolor changes reached, try again with a lower number of elements"
               
        # 1. Sample n element ids to change
        if element_id is None:
            changes = random.sample(range(n_elements), n_changes)
        else:
            changes = element_id
            
        # 2. Change elements
        for i in range(len(changes)):
            self.set_element_fillcolor(element_id = changes[i], fillcolor_value = fillcolor_value[i])
              
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
        must match the number of rows and columns of the Grid stimulus
        
        Parameters
        ----------
        opacities: list
            A list of opacity values equal in length to the number of elements in the position pattern of the stimulus.

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
        element_id : int, tuple, or list
            A single integer referring to the element's index value (element number),
            or a tuple or list with the row and column index of the element. 
        opacity_value : int, float, or list
            A numeric value between 0 and 1, or a list for animated opacities.

        """
        element_id = self._parse_element_id(element_id)
        
        self._attribute_overrides[element_id]['opacity'] = opacity_value
                    
    def set_element_opacities(self, opacity_value, element_id = None, n_changes = None):
        """
        Sets the opacities of a series of individual elements
        
        Parameters
        ----------
        opacity_value: int, float, or list
            The new opacity value(s) to apply to the specified elements.        
        element_id : int, tuple, or list, optional
            A single integer referring to the element's index value (element number),
            or a tuple or list with the row and column index of the element,
            or a list of several element ids 
        n_changes: int, optional  
            The number of randomly chosen elements to change in the stimulus.
        """  
 
        if element_id is not None:
            if type(element_id) == int:
                element_id = [element_id]
            n_changes = len(element_id)
            opacity_value = Pattern(opacity_value).RepeatPatternToSize(n_changes).pattern
        elif n_changes is not None:
            n_changes = n_changes
            opacity_value = Pattern(opacity_value).RepeatPatternToSize(n_changes).pattern
        else:
            if type(opacity_value) is not list:
                opacity_value = [opacity_value]
            n_changes = len(opacity_value)
        
        n_elements = self._n_rows * self._n_cols
        assert n_elements >= n_changes, "Maximum number of opacity changes reached, try again with a lower number of elements"
               
        # 1. Sample n element ids to change
        if element_id is None:
            changes = random.sample(range(n_elements), n_changes)
        else:
            changes = element_id
            
        # 2. Change elements
        for i in range(len(changes)):
            self.set_element_opacity(element_id = changes[i], opacity_value = opacity_value[i])

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
        must match the number of rows and columns of the Grid stimulus
        
        Parameters
        ----------
        borderwidths: list
            A list of borderwidth values equal in length to the number of elements in the position pattern of the stimulus.

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
        element_id : int, tuple, or list
            A single integer referring to the element's index value (element number),
            or a tuple or list with the row and column index of the element. 
        borderwidth_value : int, float, or list
            Size of the border.

        """
        element_id = self._parse_element_id(element_id)
        
        self._attribute_overrides[element_id]['borderwidth'] = borderwidth_value
                       
    def set_element_borderwidths(self, borderwidth_value, element_id = None, n_changes = None):
        """
        Sets the borderwidths of a series of individual elements
        
        Parameters
        ----------
        borderwidth_value: int, float, or list
            The new borderwidth value(s) to apply to the specified elements.        
        element_id : int, tuple, or list, optional
            A single integer referring to the element's index value (element number),
            or a tuple or list with the row and column index of the element,
            or a list of several element ids 
        n_changes: int, optional  
            The number of randomly chosen elements to change in the stimulus.
        """  

        if element_id is not None:
            if type(element_id) == int:
                element_id = [element_id]
            n_changes = len(element_id)
            borderwidth_value = Pattern(borderwidth_value).RepeatPatternToSize(n_changes).pattern
        elif n_changes is not None:
            n_changes = n_changes
            borderwidth_value = Pattern(borderwidth_value).RepeatPatternToSize(n_changes).pattern
        else:
            if type(borderwidth_value) is not list:
                borderwidth_value = [borderwidth_value]
            n_changes = len(borderwidth_value)
        
        n_elements = self._n_rows * self._n_cols
        assert n_elements >= n_changes, "Maximum number of borderwidth changes reached, try again with a lower number of elements"
               
        # 1. Sample n element ids to change
        if element_id is None:
            changes = random.sample(range(n_elements), n_changes)
        else:
            changes = element_id
            
        # 2. Change elements
        for i in range(len(changes)):
            self.set_element_borderwidth(element_id = changes[i], borderwidth_value = borderwidth_value[i])
            
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
        must match the number of rows and columns of the Grid stimulus
        
        Parameters
        ----------
        orientations: list
            A list of orientation values equal in length to the number of elements in the position pattern of the stimulus.

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
        element_id : int, tuple, or list
            A single integer referring to the element's index value (element number),
            or a tuple or list with the row and column index of the element. 
        orientation_value : int or list
            Orientation of the element.
        """
        element_id = self._parse_element_id(element_id)
        
        self._attribute_overrides[element_id]['orientation'] = orientation_value
            
    def set_element_orientations(self, orientation_value, element_id = None, n_changes = None):
        """
        Sets the orientations of a series of individual elements
        
        Parameters
        ----------
        orientation_value: int or list
            The new orientation value(s) to apply to the specified elements.        
        element_id : int, tuple, or list, optional
            A single integer referring to the element's index value (element number),
            or a tuple or list with the row and column index of the element,
            or a list of several element ids 
        n_changes: int, optional  
            The number of randomly chosen elements to change in the stimulus.
        """  
 
        if element_id is not None:
            if type(element_id) == int:
                element_id = [element_id]
            n_changes = len(element_id)
            orientation_value = Pattern(orientation_value).RepeatPatternToSize(n_changes).pattern
        elif n_changes is not None:
            n_changes = n_changes
            orientation_value = Pattern(orientation_value).RepeatPatternToSize(n_changes).pattern
        else:
            if type(orientation_value) is not list:
                orientation_value = [orientation_value]
            n_changes = len(orientation_value)
        
        n_elements = self._n_rows * self._n_cols
        assert n_elements >= n_changes, "Maximum number of orientation changes reached, try again with a lower number of elements"
               
        # 1. Sample n element ids to change
        if element_id is None:
            changes = random.sample(range(n_elements), n_changes)
        else:
            changes = element_id
            
        # 2. Change elements
        for i in range(len(changes)):
            self.set_element_orientation(element_id = changes[i], orientation_value = orientation_value[i])
            
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
        must match the number of rows and columns of the Grid stimulus
        
        Parameters
        ----------
        data: list
            A list of data values equal in length to the number of elements in the position pattern of the stimulus.

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
        element_id : int, tuple, or list
            A single integer referring to the element's index value (element number),
            or a tuple or list with the row and column index of the element. 
        data_value : string
            Data string for the element.
        """
        element_id = self._parse_element_id(element_id)
        
        self._attribute_overrides[element_id]['data'] = data_value

    def set_element_datas(self, data_value, element_id = None, n_changes = None):
        """
        Sets the data of a series of individual elements
        
        Parameters
        ----------
        data_value: string or list
            The new data value(s) to apply to the specified elements.        
        element_id : int, tuple, or list, optional
            A single integer referring to the element's index value (element number),
            or a tuple or list with the row and column index of the element,
            or a list of several element ids 
        n_changes: int, optional  
            The number of randomly chosen elements to change in the stimulus.
        """  
 
        if element_id is not None:
            if type(element_id) == int:
                element_id = [element_id]
            n_changes = len(element_id)
            data_value = Pattern(data_value).RepeatPatternToSize(n_changes).pattern
        elif n_changes is not None:
            n_changes = n_changes
            data_value = Pattern(data_value).RepeatPatternToSize(n_changes).pattern
        else:
            if type(data_value) is not list:
                data_value = [data_value]
            n_changes = len(data_value)
        
        n_elements = self._n_rows * self._n_cols
        assert n_elements >= n_changes, "Maximum number of data changes reached, try again with a lower number of elements"
               
        # 1. Sample n element ids to change
        if element_id is None:
            changes = random.sample(range(n_elements), n_changes)
        else:
            changes = element_id
            
        # 2. Change elements
        for i in range(len(changes)):
            self.set_element_data(element_id = changes[i], data_value = data_value[i])
            
    @property
    def classlabels(self):
        """
        The class labels for each grid element

        """
        return self._classlabels.generate().pattern
    
    @classlabels.setter
    def classlabels(self, classlabels):
        """
        Sets the classlabel for each grid element.
        
        If the provided pattern has a fixed grid structure, that structure
        must match the number of rows and columns of the Grid stimulus
                 
        Parameters
        ----------
        classlabels: list
            A list of classlabel values equal in length to the number of elements in the position pattern of the stimulus.
        """

        if not self._check_attribute_dimensions(classlabels):
            return
        
        self._classlabels = classlabels
        self._classlabels.n_rows = self._n_rows
        self._classlabels.n_cols = self._n_cols
        
    def set_element_classlabel(self, element_id, classlabel_value):
        """
        Sets the classlabel of an individual element

        Parameters
        ----------
        element_id : int, tuple, or list
            A single integer referring to the element's index value (element number),
            or a tuple or list with the row and column index of the element. 
        classlabel_value : string
            A classlabel string.
        """

        element_id = self._parse_element_id(element_id)
        
        self._attribute_overrides[element_id]['classlabels'] = classlabel_value
        
    def set_element_classlabels(self, classlabel_value, element_id = None, n_changes = None):
        """
        Sets the classlabels of a series of individual elements
        
        Parameters
        ----------
        classlabel_value: string or list
            The new classlabel value(s) to apply to the specified elements.        
        element_id : int, tuple, or list, optional
            A single integer referring to the element's index value (element number),
            or a tuple or list with the row and column index of the element,
            or a list of several element ids 
        n_changes: int, optional  
            The number of randomly chosen elements to change in the stimulus.
        """  
        if element_id is not None:
            if type(element_id) == int:
                element_id = [element_id]
            n_changes = len(element_id)
            classlabel_value = Pattern(classlabel_value).RepeatPatternToSize(n_changes).pattern
        elif n_changes is not None:
            n_changes = n_changes
            classlabel_value = Pattern(classlabel_value).RepeatPatternToSize(n_changes).pattern
        else:
            if type(classlabel_value) is not list:
                classlabel_value = [classlabel_value]
            n_changes = len(classlabel_value)
        
        n_elements = self._n_rows * self._n_cols
        assert n_elements >= n_changes, "Maximum number of classlabel changes reached, try again with a lower number of elements"
               
        # 1. Sample n element ids to change
        if element_id is None:
            changes = random.sample(range(n_elements), n_changes)
        else:
            changes = element_id
            
        # 2. Change elements
        for i in range(len(changes)):
            self.set_element_classlabel(element_id = changes[i], classlabel_value = classlabel_value[i])    
            
    @property
    def idlabels(self):
        """
        The ids for each grid element

        """
        return self._idlabels.generate().pattern
    
    @idlabels.setter
    def idlabels(self, idlabels):
        """
        Sets the idlabel for each grid element.
        
        If the provided pattern has a fixed grid structure, that structure
        must match the number of rows and columns of the Grid stimulus
                 
        Parameters
        ----------
        idlabels: list
            A list of idlabel values equal in length to the number of elements in the position pattern of the stimulus.
        """
        if not self._check_attribute_dimensions(idlabels):
            return
        
        self._idlabels = idlabels
        self._idlabels.n_rows = self._n_rows
        self._idlabels.n_cols = self._n_cols
        
    def set_element_idlabel(self, element_id, idlabel_value):
        """
        Sets the idlabel of an individual element

        Parameters
        ----------
        element_id : int, tuple, or list
            A single integer referring to the element's index value (element number),
            or a tuple or list with the row and column index of the element. 
        idlabel_value : string
            An idlabel string.
        """
        element_id = self._parse_element_id(element_id)
        
        self._attribute_overrides[element_id]['idlabels'] = idlabel_value
        
    def set_element_idlabels(self, idlabel_value, element_id = None, n_changes = None):
        """
        Sets the idlabels of a series of individual elements
        
        Parameters
        ----------
        idlabel_value: string or list
            The new idlabel value(s) to apply to the specified elements.        
        element_id : int, tuple, or list, optional
            A single integer referring to the element's index value (element number),
            or a tuple or list with the row and column index of the element,
            or a list of several element ids 
        n_changes: int, optional  
            The number of randomly chosen elements to change in the stimulus.
        """  
        if element_id is not None:
            if type(element_id) == int:
                element_id = [element_id]
            n_changes = len(element_id)
            idlabel_value = Pattern(idlabel_value).RepeatPatternToSize(n_changes).pattern
        elif n_changes is not None:
            n_changes = n_changes
            idlabel_value = Pattern(idlabel_value).RepeatPatternToSize(n_changes).pattern
        else:
            if type(idlabel_value) is not list:
                idlabel_value = [idlabel_value]
            n_changes = len(idlabel_value)
        
        n_elements = self._n_rows * self._n_cols
        assert n_elements >= n_changes, "Maximum number of idlabel changes reached, try again with a lower number of elements"
               
        # 1. Sample n element ids to change
        if element_id is None:
            changes = random.sample(range(n_elements), n_changes)
        else:
            changes = element_id
            
        # 2. Change elements
        for i in range(len(changes)):
            self.set_element_idlabel(element_id = changes[i], idlabel_value = idlabel_value[i])
            
    @property
    def mirrorvalues(self):
        """
        The mirror value for each grid element

        """
        return self._mirrorvalues.generate().pattern
    
    @mirrorvalues.setter
    def mirrorvalues(self, mirrorvalues):
        """
        Sets the mirrorvalue for each grid element.
        
        If the provided pattern has a fixed grid structure, that structure
        must match the number of rows and columns of the Grid stimulus
                 
        Parameters
        ----------
        mirrorvalues: list
            A list of mirrorvalue values equal in length to the number of elements in the position pattern of the stimulus.
        """

        if not self._check_attribute_dimensions(mirrorvalues):
            return
        
        self._mirrorvalues = mirrorvalues
        self._mirrorvalues.n_rows = self._n_rows
        self._mirrorvalues.n_cols = self._n_cols
        
    def set_element_mirrorvalue(self, element_id, mirror_value):
        """
        Sets the mirrorvalue of an individual element

        Parameters
        ----------
        element_id : int, tuple, or list
            A single integer referring to the element's index value (element number),
            or a tuple or list with the row and column index of the element. 
        mirrorvalue_value : string
            A mirrorvalue string ('none', 'horizontal', 'vertical', or 'horizontalvertical')
        """

        element_id = self._parse_element_id(element_id)
        
        self._attribute_overrides[element_id]['mirrorvalues'] = mirror_value
    
    def set_element_mirrorvalues(self, mirror_value, element_id = None, n_changes = None):
        """
        Sets the mirrorvalues of a series of individual elements
        
        Parameters
        ----------
        mirror_value: string or list
            The new mirrorvalue value(s) to apply to the specified elements.        
        element_id : int, tuple, or list, optional
            A single integer referring to the element's index value (element number),
            or a tuple or list with the row and column index of the element,
            or a list of several element ids 
        n_changes: int, optional  
            The number of randomly chosen elements to change in the stimulus.
        """  
  
        if element_id is not None:
            if type(element_id) == int:
                element_id = [element_id]
            n_changes = len(element_id)
            mirror_value = Pattern(mirror_value).RepeatPatternToSize(n_changes).pattern
        elif n_changes is not None:
            n_changes = n_changes
            mirror_value = Pattern(mirror_value).RepeatPatternToSize(n_changes).pattern
        else:
            if type(mirror_value) is not list:
                mirror_value = [mirror_value]
            n_changes = len(mirror_value)
        
        n_elements = self._n_rows * self._n_cols
        assert n_elements >= n_changes, "Maximum number of mirrorvalue changes reached, try again with a lower number of elements"
               
        # 1. Sample n element ids to change
        if element_id is None:
            changes = random.sample(range(n_elements), n_changes)
        else:
            changes = element_id
            
        # 2. Change elements
        for i in range(len(changes)):
            self.set_element_mirrorvalue(element_id = changes[i], mirror_value = mirror_value[i])
            
    @property
    def links(self):
        """
        The link for each grid element

        """
        return self._links.generate().pattern
    
    @links.setter
    def links(self, links):
        """
        Sets the link for each grid element.
        
        If the provided pattern has a fixed grid structure, that structure
        must match the number of rows and columns of the Grid stimulus
                 
        Parameters
        ----------
        links: list
            A list of link values equal in length to the number of elements in the position pattern of the stimulus.
        """

        if not self._check_attribute_dimensions(links):
            return
        
        self._links = links
        self._links.n_rows = self._n_rows
        self._links.n_cols = self._n_cols
        
    def set_element_link(self, element_id, link):
        """
        Sets the link of an individual element

        Parameters
        ----------
        element_id : int, tuple, or list
            A single integer referring to the element's index value (element number),
            or a tuple or list with the row and column index of the element. 
        link_value : string
            A hyperlink string.
        """

        element_id = self._parse_element_id(element_id)
        
        self._attribute_overrides[element_id]['links'] = link
    
    def set_element_links(self, link_value, element_id = None, n_changes = None):
        """
        Sets the links of a series of individual elements
        
        Parameters
        ----------
        link_value: string or list
            The new link value(s) to apply to the specified elements.        
        element_id : int, tuple, or list, optional
            A single integer referring to the element's index value (element number),
            or a tuple or list with the row and column index of the element,
            or a list of several element ids 
        n_changes: int, optional  
            The number of randomly chosen elements to change in the stimulus.
        """  

        if element_id is not None:
            if type(element_id) == int:
                element_id = [element_id]
            n_changes = len(element_id)
            link_value = Pattern(link_value).RepeatPatternToSize(n_changes).pattern
        elif n_changes is not None:
            n_changes = n_changes
            link_value = Pattern(link_value).RepeatPatternToSize(n_changes).pattern
        else:
            if type(link_value) is not list:
                link_value = [link_value]
            n_changes = len(link_value)
        
        n_elements = self._n_rows * self._n_cols
        assert n_elements >= n_changes, "Maximum number of link changes reached, try again with a lower number of elements"
               
        # 1. Sample n element ids to change
        if element_id is None:
            changes = random.sample(range(n_elements), n_changes)
        else:
            changes = element_id
            
        # 2. Change elements
        for i in range(len(changes)):
            self.set_element_link(element_id = changes[i], link_value = link_value[i])
            
    def randomize_elements(self, direction = "AcrossElements"):
        """
        Randomizes the order of the elements in the Grid stimulus across a specified direction.
        
        Parameters
        ----------
        direction: string
            A pattern direction ("AcrossElements", "AcrossRows", "AcrossColumns",
            "AcrossLeftDiagonal","AcrossRightDiagonal"). 
            Default is "AcrossElements".
        """
        # if self.dwg_elements is None:
        self.Render() 
            
        if direction == "AcrossElements":
               
            new_order = Pattern(self._element_presentation_order)._SetRandomizeAcrossElements()
            self._element_presentation_order = new_order.pattern
            
        elif direction == "AcrossRows":
               
            new_order = Pattern(self._element_presentation_order)._SetRandomizeAcrossRows(n_rows = self.n_rows, n_cols = self.n_cols)
            self._element_presentation_order = new_order.pattern
                
        elif direction == "AcrossColumns":
               
            new_order = Pattern(self._element_presentation_order)._SetRandomizeAcrossColumns(n_rows = self.n_rows, n_cols = self.n_cols)
            self._element_presentation_order = new_order.pattern        
        
        elif direction == "AcrossLeftDiagonal":
               
            new_order = Pattern(self._element_presentation_order)._SetRandomizeAcrossLeftDiagonal(n_rows = self.n_rows, n_cols = self.n_cols)
            self._element_presentation_order = new_order.pattern

        elif direction == "AcrossRightDiagonal":
               
            new_order = Pattern(self._element_presentation_order)._SetRandomizeAcrossRightDiagonal(n_rows = self.n_rows, n_cols = self.n_cols)
            self._element_presentation_order = new_order.pattern
            
    def swap_elements(self, n_swap_pairs = 1, swap_pairs = None):
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
        n_swap_pairs: int, optional 
            Number of element pairs that will be swapped. Maximum value
            is half the total number of elements. Default is 1.
        swap_pairs: tuple or list, optional
            Element indices of specific pairs of elements to be swapped.

        """
        if swap_pairs is not None:
            assert type(swap_pairs) == tuple or type(swap_pairs) == list, 'Swap_pairs needs to be tuple or list'
            if type(swap_pairs) is not list:
                swap_pairs = [swap_pairs]
            n_swap_pairs = len(swap_pairs)     
        
        n_elements = self._n_rows * self._n_cols
        assert n_elements >= n_swap_pairs * 2, 'Maximal number of swaps possible is %d, but %d were requested'%(n_elements//2, n_swap_pairs)
              
        if swap_pairs is None:
            # 1. Generate all available swap positions
            candidate_swap_positions = set()
            for i in range(n_elements):
                for j in range(i+1, n_elements):
                    candidate_swap_positions.add((i,j))
                
            # 2. Select the required number of swap positions
            selected_swap_pairs = []
            for i in range(n_swap_pairs):
                selected_pair = random.sample(sorted(candidate_swap_positions), 1)[0]
                selected_swap_pairs.append(selected_pair)
                
                removable_positions = set()
                for p in candidate_swap_positions:
                    if selected_pair[0] in p or selected_pair[1] in p:
                        removable_positions.add(p)
                        
                candidate_swap_positions.difference_update(removable_positions)
        else:
            selected_swap_pairs = swap_pairs
            
        # 3. Perform the swap
        for swap_pair in selected_swap_pairs:
            self._element_presentation_order[swap_pair[0]], self._element_presentation_order[swap_pair[1]] = self._element_presentation_order[swap_pair[1]], self._element_presentation_order[swap_pair[0]]
            
            
    def swap_distinct_elements(self, n_swap_pairs = 1, distinction_features = ['shapes', 'boundingboxes', 'fillcolors', 'orientations', 'opacities', 'mirrorvalues', 'links', 'classlabels', 'idlabels']):
        """
        Swaps the position of two elements in the pattern. The elements that
        wil be swapped need to be distinct on at least one element feature
        dimension specified in the distinction_features argument. Once 
        an element is used in a swap, it will not be used in subsequent swaps.
        
        
        Parameters
        ----------
        n_swap_pairs: int, optional
            Number of element pairs that will be swapped. Default is 1.
        distinction_features: list
            Feature dimensions that will be inspected to decide if two elements
            are the same. Default is ['shapes', 'boundingboxes', 'fillcolors', 'orientations', 'opacities', 'mirrorvalues', 'links', 'classlabels', 'idlabels']

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
            selected_pair = random.sample(sorted(candidate_swap_positions), 1)[0]
            selected_swap_pairs.append(selected_pair)
            
            removable_positions = set()
            for p in candidate_swap_positions:
                if selected_pair[0] in p or selected_pair[1] in p:
                    removable_positions.add(p)
                    
            candidate_swap_positions.difference_update(removable_positions)
            
        # 3. Perform the swap
        for swap_pair in selected_swap_pairs:
            self._element_presentation_order[swap_pair[0]], self._element_presentation_order[swap_pair[1]] = self._element_presentation_order[swap_pair[1]], self._element_presentation_order[swap_pair[0]]

    def swap_features(self, n_swap_pairs = 1, feature_dimensions = ['fillcolors'], swap_pairs = None):
        """
        Swaps the position of two element features in the pattern. Once 
        an element is used in a swap, it will not be used in subsequent swaps.
        
        
        Parameters
        ----------
        n_swap_pairs: int , optional
            Number of element pairs that will be swapped. Default is 1.
        feature_dimensions: list, optional
            Feature dimensions that will be swapped between the elements.
            Default is ['fillcolors'].
        swap_pairs: tuple or list, optional
            Element indices of specific pairs of elements to be swapped.
        """
        if swap_pairs is not None:
            assert type(swap_pairs) == tuple or type(swap_pairs) == list, 'Swap_pairs needs to be tuple or list'
            if type(swap_pairs) is not list:
                swap_pairs = [swap_pairs]
            n_swap_pairs = len(swap_pairs)  
            
        if swap_pairs is None:
            # 1. Generate all available swap positions
            n_elements = self.n_rows * self.n_cols
            
            candidate_swap_positions = set()
            for i in range(n_elements):
                for j in range(i+1, n_elements):
                    candidate_swap_positions.add((i,j))
            
            # 2. Select the required number of swap positions
            selected_swap_pairs = []
            for i in range(n_swap_pairs):
                assert len(candidate_swap_positions) > 0, "Distinct swaps exhausted, try again with a lower number of pairs"
                selected_pair = random.sample(sorted(candidate_swap_positions), 1)[0]
                selected_swap_pairs.append(selected_pair)
                
                removable_positions = set()
                for p in candidate_swap_positions:
                    if selected_pair[0] in p or selected_pair[1] in p:
                        removable_positions.add(p)
                        
                candidate_swap_positions.difference_update(removable_positions)
        else:
            selected_swap_pairs = swap_pairs
            
        # 3. Perform the swap
        for swap_pair in selected_swap_pairs:
            
            swap_element_0 = self._parse_element_id(swap_pair[0])
            swap_element_1 = self._parse_element_id(swap_pair[1])
            
            if 'shapes' in feature_dimensions:
                self._attribute_overrides[swap_element_0]['shape'] , self._attribute_overrides[swap_element_1]['shape'] = self.shapes[swap_pair[1]], self.shapes[swap_pair[0]]
            if 'boundingboxes' in feature_dimensions:
                self._attribute_overrides[swap_element_0]['boundingbox'] , self._attribute_overrides[swap_element_1]['boundingbox'] = self.boundingboxes[swap_pair[1]], self.boundingboxes[swap_pair[0]]
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
            if 'classlabels' in feature_dimensions:
                self._attribute_overrides[swap_element_0]['classlabel'] , self._attribute_overrides[swap_element_1]['classlabel']  = self.classlabels[swap_pair[1]], self.classlabels[swap_pair[0]]
            if 'idlabels' in feature_dimensions:
                self._attribute_overrides[swap_element_0]['idlabel'] , self._attribute_overrides[swap_element_1]['idlabel']  = self.idlabels[swap_pair[1]], self.idlabels[swap_pair[0]]
            if 'mirrorvalues' in feature_dimensions:
                self._attribute_overrides[swap_element_0]['mirrorvalue'] , self._attribute_overrides[swap_element_1]['mirrorvalue']  = self.mirrorvalues[swap_pair[1]], self.mirrorvalues[swap_pair[0]]
            if 'links' in feature_dimensions:
                self._attribute_overrides[swap_element_0]['link'] , self._attribute_overrides[swap_element_1]['link']  = self.links[swap_pair[1]], self.links[swap_pair[0]]
 
  
    def swap_distinct_features(self, n_swap_pairs = 1, feature_dimensions = ['fillcolors']):
        """
        Swaps the position of two element features in the pattern. The element features that
        wil be swapped need to be distinct on the element feature
        dimension specified in the feature_dimensions argument. Once 
        an element is used in a swap, it will not be used in subsequent swaps.
        
        
        Parameters
        ----------
        n_swap_pairs: int, optional 
            Number of element pairs that will be swapped. Default is 1.
        feature_dimensions: list
            Feature dimensions that will be swapped between the elements.
            Default is ['fillcolors'].

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
            selected_pair = random.sample(sorted(candidate_swap_positions), 1)[0]
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
            if 'boundingboxes' in feature_dimensions:
                self._attribute_overrides[swap_element_0]['boundingbox'] , self._attribute_overrides[swap_element_1]['boundingbox'] = self.boundingboxes[swap_pair[1]], self.boundingboxes[swap_pair[0]]
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
            if 'classlabels' in feature_dimensions:
                self._attribute_overrides[swap_element_0]['classlabel'] , self._attribute_overrides[swap_element_1]['classlabel']  = self.classlabels[swap_pair[1]], self.classlabels[swap_pair[0]]
            if 'idlabels' in feature_dimensions:
                self._attribute_overrides[swap_element_0]['idlabel'] , self._attribute_overrides[swap_element_1]['idlabel']  = self.idlabels[swap_pair[1]], self.idlabels[swap_pair[0]]
            if 'mirrorvalues' in feature_dimensions:
                self._attribute_overrides[swap_element_0]['mirrorvalue'] , self._attribute_overrides[swap_element_1]['mirrorvalue']  = self.mirrorvalues[swap_pair[1]], self.mirrorvalues[swap_pair[0]]
            if 'links' in feature_dimensions:
                self._attribute_overrides[swap_element_0]['link'] , self._attribute_overrides[swap_element_1]['link']  = self.links[swap_pair[1]], self.links[swap_pair[0]]
 
           
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

class Concentric(Grid):
    _element_attributes = ["_boundingboxes", "_orientations", "_bordercolors", "_borderwidths", "_fillcolors", "_opacities", "_shapes",
                          "_classlabels", "_idlabels", "_mirrorvalues", "_links", "_data"]
    
    def __init__(self, n_elements, x_margin = 20, y_margin = 20, size = None, 
                 background_color = "white", background_shape = None, 
                 stim_mask = None, stim_orientation = 0, stim_mirrorvalue = None, 
                 stim_link = None, stim_classlabel = None, stim_idlabel = None):
        """
        Instantiates a Concentric (Grid) stimulus.

        Parameters
        ----------
        n_elements: int
            Number of elements in the stimulus.
        x_margin: int, float, or tuple, optional
            Amount of extra space added to both sides of the stimulus in the x-direction. The default is 20.
        y_margin: int, float, or tuple, optional
            Amount of extra space added to both sides of the stimulus in the y-direction. The default is 20.
        size: tuple, optional
            If specified, fixes the size of the stimulus to the dimension
            given in the tuple. The center of the stimulus will be calculated
            to correspond to the center of all element positions in the
            stimulus.
        background_color: string or list, optional
            Background color of the stimulus. The default is "white".
        background_shape: string or octa.shapes object, optional
            If specified, clips the stimulus to the specified shape (only the part of the stimulus that falls within the 
            background shape will be visible). The center of the background shape 
            will correspond to the center of all element positions in the stimulus.
            If a shape name is provided as string, the boundingbox of the shape will be equal to the stimulus size.
        stim_mask: string or octa.shapes object, optional
            If specified, clips the stimulus to the specified shape. The center of the background shape 
            will correspond to the center of all element positions in the stimulus.
            If a shape name is provided as string, the boundingbox of the shape will be equal to the stimulus size.   
        stim_orientation: int, float, or list, optional
            If not equal to 0, the stimulus will be rotated around its center according to the specified degree value. The default is 0.
        stim_mirrorvalue: string, optional
            If specified, defines the way the stimulus will be mirrored (none, horizontal, vertical, or horizontalvertical).   
        stim_link: string, optional
            If specified, defines the hyperlink that will be activated when the stimulus is clicked.   
        stim_classlabel: string, optional
            If specified, defines the class label that can be used to add javascript or css changes to the stimulus. 
        stim_idlabel: string, optional
            If specified, defines the id label that can be used to add javascript or css changes to the stimulus.        

        """
        
        super().__init__(n_rows = 1, n_cols = n_elements, x_margin = x_margin, y_margin = y_margin, size = size, 
                         background_color = background_color, background_shape = background_shape, 
                         stim_mask = stim_mask, stim_orientation = stim_orientation, stim_mirrorvalue = stim_mirrorvalue, 
                         stim_link = stim_link, stim_classlabel = stim_classlabel, stim_idlabel = stim_idlabel)
        
        # Initialize the positions of each element
        self._n_elements = n_elements
        self._n_rows = 1
        self._n_cols = n_elements
        
        self.positions = Positions.CreateCustomPositions(x = [0]*n_elements, y = [0]*n_elements)
        
        self.boundingboxes = GridPattern.GradientAcrossElements((200,200), (20,20))
        self.fillcolors = GridPattern.RepeatAcrossElements(["dodgerblue", "lightgrey"])

class Outline(Grid):
    _element_attributes = ["_boundingboxes", "_orientations", "_bordercolors", "_borderwidths", "_fillcolors", "_opacities", "_shapes",
                          "_classlabels", "_idlabels", "_mirrorvalues", "_links", "_data"]
    
    def __init__(self, n_elements, shape = 'Ellipse', shape_boundingbox = (150,150), 
                 x_margin = 20, y_margin = 20, size = None, 
                 background_color = "white", background_shape = None, 
                 stim_mask = None, stim_orientation = 0, stim_mirrorvalue = None, 
                 stim_link = None, stim_classlabel = None, stim_idlabel = None):
        """
        Instantiates an Outline (Grid) stimulus.

        Parameters
        ----------
        n_elements: int
            Number of elements in the stimulus
        shape: string
            'Ellipse' or source string to svg file. Default is 'Ellipse'.
        shape_boundingbox: int or tuple
            Boundingbox value for shape outline. Default is (150,150).
        x_margin: int, float, or tuple, optional
            Amount of extra space added to both sides of the stimulus in the x-direction. The default is 20.
        y_margin: int, float, or tuple, optional
            Amount of extra space added to both sides of the stimulus in the y-direction. The default is 20.
        size: tuple, optional
            If specified, fixes the size of the stimulus to the dimension
            given in the tuple. The center of the stimulus will be calculated
            to correspond to the center of all element positions in the
            stimulus.
        background_color: string or list, optional
            Background color of the stimulus. The default is "white".
        background_shape: string or octa.shapes object, optional
            If specified, clips the stimulus to the specified shape (only the part of the stimulus that falls within the 
            background shape will be visible). The center of the background shape 
            will correspond to the center of all element positions in the stimulus.
            If a shape name is provided as string, the boundingbox of the shape will be equal to the stimulus size.
        stim_mask: string or octa.shapes object, optional
            If specified, clips the stimulus to the specified shape. The center of the background shape 
            will correspond to the center of all element positions in the stimulus.
            If a shape name is provided as string, the boundingbox of the shape will be equal to the stimulus size.   
        stim_orientation: int, float, or list, optional
            If not equal to 0, the stimulus will be rotated around its center according to the specified degree value. The default is 0.
        stim_mirrorvalue: string, optional
            If specified, defines the way the stimulus will be mirrored (none, horizontal, vertical, or horizontalvertical).   
        stim_link: string, optional
            If specified, defines the hyperlink that will be activated when the stimulus is clicked.   
        stim_classlabel: string, optional
            If specified, defines the class label that can be used to add javascript or css changes to the stimulus. 
        stim_idlabel: string, optional
            If specified, defines the id label that can be used to add javascript or css changes to the stimulus.        

        """
        
        super().__init__(n_rows = 1, n_cols = n_elements, x_margin = x_margin, y_margin = y_margin, size = size,
                         background_color = background_color, background_shape = background_shape, 
                         stim_mask = stim_mask, stim_orientation = stim_orientation, stim_mirrorvalue = stim_mirrorvalue, 
                         stim_link = stim_link, stim_classlabel = stim_classlabel, stim_idlabel = stim_idlabel)
        
        # Initialize the positions of each element
        self._n_elements = n_elements
        self._n_rows = 1
        self._n_cols = n_elements
        
        self._shape = shape
        self._shape_boundingbox = shape_boundingbox
        
        if shape == 'Ellipse':
            self.positions = Positions.CreateCircle(n_elements = n_elements, radius = shape_boundingbox[0])
        else:
            self.positions = Positions.CreateShape(n_elements = n_elements, src = shape, width = shape_boundingbox[0], height = shape_boundingbox[1])
        
