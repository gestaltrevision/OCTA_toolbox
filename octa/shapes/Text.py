# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 16:02:30 2020

@author: Christophe
"""

class Text:
    parameters = ['position', 'bounding_box', 'orientation' ,'bordercolour', 'borderwidth', 'fillcolour', 'class_label', 'id_label', 'mirror', 'data']
    
    def __init__(self, **kwargs):
        for p in Text.parameters:
            set_method = getattr(self, 'set_%s'%p)
            if p in kwargs:
                set_method(kwargs[p])
            else:
                set_method(None)


    def set_position(self, position):
        if position == None:
            position = (0, 0)
        
        self.position = position
    
    
    def set_bounding_box(self, bounding_box):
        if bounding_box == None:
            bounding_box = (10, 10)
        
        self.bounding_box = bounding_box
    
    
    def set_orientation(self, orientation):
        if orientation == None:
            orientation = 0
            
        self.orientation = orientation
    
    
    def set_bordercolour(self, bordercolour):
        if bordercolour == None:
            bordercolour = "green"
            
        self.bordercolour = bordercolour
    
    
    def set_borderwidth(self, borderwidth):
        if borderwidth == None:
            borderwidth = 4
            
        self.borderwidth = borderwidth
        
        
    def set_fillcolour(self, fillcolour):
        if fillcolour == None:
            fillcolour = "gray"
            
        self.fillcolour = fillcolour
    
    
    def set_class_label(self, class_label):
        if class_label == None:
            class_label = ""
            
        self.class_label = class_label
    
    def set_id_label(self, id_label):
        if id_label == None:
            id_label = ""
            
        self.id_label = id_label
    
    def set_mirror(self, mirror):
        if mirror == None:
            mirror = ""
            
        self.mirror = mirror
        
    def set_data(self, data):
        if data == None:
            data = ""
            
        self.data = data
    

    def __str__(self):
        result = "Text object with params:\n"
        for p in Text.parameters:
            result += "%s: %s\n"%(p, getattr(self,p))
            
        return result
        
    def generate(self, dwg):
        topleft = (self.position[0] - self.bounding_box[0]/2 , self.position[1] - self.bounding_box[1]/2)
        svg = dwg.textArea(
                text        = self.data,
                insert      = topleft,
                font_size   = 10,
                size        = self.bounding_box)
        
        return svg
    
