# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 12:59:09 2020

@author: u0072088
"""
import svgwrite
from IPython.display import SVG, display

class Stimulus:
    """ Container class for creating a stimulus.
    
    Size and background color is set when creating the object.
    
    Position, radii and shape properties need to be assigned. When this is done,
    the render method can be called. This will generate the JSON format, and 
    create an svg image.
    """
    
    def __init__(self, width = 512, height = 512, background_color = "white"):
        self.width = width
        self.height = height
        self.background_color = background_color
        
        self.positions = None
        self.radii     = None
        self.shapes    = None
        self.colour    = None
        
        self.json_parameters = None
        
    def CreateEmptyBackground(self):        
        """ Creates an empty background in which elements can be drawn. """
        self.dwg = svgwrite.Drawing(size = (self.width, self.height))
        self.background = self.dwg.rect(insert = (0, 0), size = (self.width, self.height), fill = self.background_color)
        self.dwg.add(self.background)              
                
    def Save(self, filename):
        self.dwg.saveas('%s.svg'%filename , pretty = True)
                
    def Render(self):
        if self.json_parameters is None:
            self.CreateJSON()
            
        self.CreateEmptyBackground()
            
        for i in range(len(self.shapes.pattern)):
            el = self.shapes.pattern[i](**self.json_parameters[i])
            self.dwg.add(el.generate(self.dwg))
            
    def Show(self):
        display(SVG(self.dwg.tostring()))
            
        
    def CreateJSON(self):
        self.json_parameters = []
        
        for i in range(len(self.shapes.pattern)):
            x      = self.positions[0].pattern[i]
            y      = self.positions[1].pattern[i]
            radius = self.radii.pattern[i]
            colour = self.colour.pattern[i]
            
            dict_parameters = {'x' : x, 'y' : y, 'radius' : radius, 'colour' : colour}
            
            self.json_parameters.append(dict_parameters)
            
    