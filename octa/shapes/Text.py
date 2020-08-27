# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 16:02:30 2020

@author: Christophe
"""

class Text:
    parameters = ['position', 'bounding_box', 'orientation' ,'bordercolor', 'borderwidth', 'fillcolor', 'class_label', 'id_label', 'mirror_value', 'data']
    
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
    
    
    def set_bordercolor(self, bordercolor):
        if bordercolor == None:
            bordercolor = "green"
            
        self.bordercolor = bordercolor
    
    
    def set_borderwidth(self, borderwidth):
        if borderwidth == None:
            borderwidth = 4
            
        self.borderwidth = borderwidth
        
        
    def set_fillcolor(self, fillcolor):
        if fillcolor == None:
            fillcolor = "gray"
            
        self.fillcolor = fillcolor
    
    
    def set_class_label(self, class_label):
        if class_label == None:
            class_label = ""
            
        self.class_label = class_label
    
    def set_id_label(self, id_label):
        if id_label == None:
            id_label = ""
            
        self.id_label = id_label
    
    def set_mirror_value(self, mirror):
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
    
    def create_mirror_transform(self):
        mirror_transform = ""
        if self.mirror == "horizontal":
            mirror_transform = "scale(-1, 1) translate(%f, 0)"%(-2*self.position[0])
        elif self.mirror == "vertical":
            mirror_transform = "scale(1, -1), translate(0, %f)"%(-2*self.position[1])
        elif self.mirror == "horizontalvertical":
            mirror_transform = "scale(-1, -1) translate(%f, %f)"%(-2*self.position[0], -2*self.position[1])
                
        return mirror_transform
        
    def generate(self, dwg):
        mirror_transform = self.create_mirror_transform()

        rotation_transform = "rotate(%d, %d, %d)"%(self.orientation, self.position[0], self.position[1])
        
#        topleft = (self.position[0] - self.bounding_box[0]/2 , self.position[1] - self.bounding_box[1]/2)

        textlength = max([(len(i) - i.count(" ")) for i in self.data.split("\n")])

        svg = dwg.textArea(
                text        = self.data,
                fill        = self.fillcolor,
                stroke= self.bordercolor,
                stroke_width = self.borderwidth,
                text_align = 'center',
#                display_align = 'center',
                insert      = (self.position[0]- (4* textlength ), self.position[1]- (4* textlength)),
                font_size   = "10pt",#min(self.bounding_box),
                font_family = 'Roboto Mono',
                size        = self.bounding_box,
                transform   = " ".join([mirror_transform, rotation_transform]))
        
#        svg = dwg.text(
#                text        = self.data, 
#                insert      = self.position,
#                fill        = self.fillcolor,
#                stroke      = self.bordercolor,
#                stroke_width = self.borderwidth,
##                style       = 'text-align = "middle";',
#                textlength  = self.bounding_box[0],
#                font_size   = min(self.bounding_box), 
##                font_weight = str(700), 
#                transform   = " ".join([mirror_transform, rotation_transform]))
#        
        return svg
    
