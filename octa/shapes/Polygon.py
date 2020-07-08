# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 16:02:30 2020

@author: Christophe
"""

from math import sin, cos, pi, radians

class Polygon:
    parameters = ['position', 'bounding_box', 'orientation' ,'bordercolor', 'borderwidth', 'fillcolor', 'class_label', 'id_label', 'mirror', 'data']
    
    def __init__(self, **kwargs):
        for p in Polygon.parameters:
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
        
#        assert bounding_box[0] == bounding_box[1], 'Polygon bounding box needs to be square'
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
    
    def set_mirror(self, mirror):
        if mirror == None:
            mirror = ""
            
        self.mirror = mirror
        
    def set_data(self, data):
        if data == None:
            data = "3"
            
        self.data = data
    

    def __str__(self):
        result = "Rectangle object with params:\n"
        for p in Polygon.parameters:
            result += "%s: %s\n"%(p, getattr(self,p))
            
        return result
        
    def generate(self, dwg):    
        transform_string = "rotate(%d, %d, %d)"%(self.orientation, self.position[0], self.position[1])
        
        
        n_sides = int(self.data)
        
        r = 1
        
        # Initial pass for calculating offset parameters
        points = []
        for i in range(n_sides):
            x = self.position[0] + r * sin((i*2*pi/n_sides) + pi)
            y = self.position[1] + r * cos((i*2*pi/n_sides) + pi) 
            points.append((x, y))
        
        min_x = min([p[0] for p in points])
        max_x = max([p[0] for p in points])
        min_y = min([p[1] for p in points])
        max_y = max([p[1] for p in points])
        
        x_center = (min_x + max_x) / 2
        y_center = (min_y + max_y) / 2
        
        x_height = max_x - min_x
        y_height = max_y - min_y
        
        x_offset = self.position[0] - x_center
        y_offset = self.position[1] - y_center
        
        x_scaling = (1/(x_height/2))*(self.bounding_box[0]/2)
        y_scaling = (1/(y_height/2))*(self.bounding_box[1]/2)
        
        # Second pass centering
        points = []
        for i in range(n_sides):
            x = self.position[0] + x_scaling * (sin((i*2*pi/n_sides) + pi) + x_offset)
            y = self.position[1] + y_scaling * (cos((i*2*pi/n_sides) + pi) + y_offset)
            points.append((x, y))
        
        svg = dwg.polygon(
                points       = points,
                fill         = self.fillcolor,
                stroke       = self.bordercolor,
                stroke_width = self.borderwidth,
                transform    = transform_string)
        
        return svg
    
if __name__ == '__main__':
    c = Polygon(x = 3, y = 4, size = 10,  color = "blue", orientation = 30)
    print(c)