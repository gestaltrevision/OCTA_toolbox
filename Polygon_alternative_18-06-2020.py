# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 16:02:30 2020

@author: Christophe
"""

from math import sin, cos, pi, sqrt

class Polygon:
    parameters = ['position', 'bounding_box', 'orientation' ,'bordercolour', 'borderwidth', 'fillcolour', 'class_label', 'id_label', 'mirror', 'data']
    
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
        
        assert bounding_box[0] == bounding_box[1], 'Polygon bounding box needs to be square'
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
            data = "3"
            
        self.data = data
    

    def __str__(self):
        result = "Rectangle object with params:\n"
        for p in Polygon.parameters:
            result += "%s: %s\n"%(p, getattr(self,p))
            
        return result
        
    def generate(self, dwg):
        transform_string = "rotate(%d, %d, %d)"%(self.orientation, self.position[0], self.position[1])
        
        points = []
        n_sides = int(self.data)
        
#        # using inner circle radius
#        r_inner = self.bounding_box[0] / 2
#        # using outer circle radius
#        r_outer = sqrt((self.bounding_box[0]*self.bounding_box[0]) + (self.bounding_box[1]*self.bounding_box[1]))/2
#        # using something in between inner and outer circle radius
#        r = (r_inner*4 + r_outer)/5
        
        r = self.bounding_box[0] / 2
        for i in range(n_sides):
            x = self.position[0] + r * sin(i*2*pi/n_sides)
            y = self.position[1] + r * cos(i*2*pi/n_sides)
            points.append((x, y))
            
        # calculate used y distance and margin left compared to specified radius    
        y_dist = max(list(list(zip(*points))[1])) - min(list(list(zip(*points))[1]))
        y_margin = ((2*r) - y_dist)/2

        # recalculate points to recenter using y_margin
        points = []
        for i in range(n_sides):
            x = self.position[0] + r * sin((i*2*pi/n_sides)+pi) 
            y = self.position[1] + r * cos((i*2*pi/n_sides)+pi) + y_margin 
            points.append((x, y))
            
        svg = dwg.polygon(
                points       = points,
                fill         = self.fillcolour,
                stroke       = self.bordercolour,
                stroke_width = self.borderwidth,
                transform    = transform_string)
        
        return svg
    
    
if __name__ == '__main__':
    c = Polygon(x = 3, y = 4, size = 10,  colour = "blue", orientation = 30)
    print(c)