# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 16:02:30 2020

@author: Christophe
"""

from math import sin, cos, pi, radians

def RegularPolygon(n_sides, name = None):
    if name == None:
        name = "RegularPolygon_" + str(n_sides)
    return type(str(name), (RegularPolygon_,), {'n_sides': n_sides, 'name': name})


class RegularPolygon_:
    parameters = ['position', 'bounding_box', 'orientation' ,'bordercolor', 'borderwidth', 'fillcolor', 'class_label', 'id_label', 'mirror_value', 'data']
    
    def __init__(self, **kwargs):
        for p in RegularPolygon_.parameters:
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
    
    def set_mirror_value(self, mirror_value):
        if mirror_value == None:
            mirror_value = ""
            
        self.mirror_value = mirror_value
        
    def set_data(self, data):
        if data == None:
            data = "3"
            
        self.data = data
    

    def __str__(self):
        result = "RegularPolygon object with params:\n"
        for p in RegularPolygon_.parameters:
            result += "%s: %s\n"%(p, getattr(self,p))
            
        return result
    
    def create_mirror_transform(self):
        mirror_transform = ""
        if self.mirror_value == "vertical":
            mirror_transform = "scale(-1, 1) translate(%f, 0)"%(-2*self.position[0])
        elif self.mirror_value == "horizontal":
            mirror_transform = "scale(1, -1), translate(0, %f)"%(-2*self.position[1])
        elif self.mirror_value == "horizontalvertical":
            mirror_transform = "scale(-1, -1) translate(%f, %f)"%(-2*self.position[0], -2*self.position[1])
                
        return mirror_transform
        
    def create_fillcolor(self, dwg):
        gradient = ""
        if len(self.fillcolor) < 2:
            return self.fillcolor
        elif self.fillcolor[0] == "radial":
            gradient = dwg.radialGradient()
        elif self.fillcolor[0] == "horizontal":
            gradient = dwg.linearGradient((0, 0), (1, 0))
        elif self.fillcolor[0] == "vertical":
            gradient = dwg.linearGradient((0, 0), (0, 1))
        elif self.fillcolor[0] == "diagonal":
            gradient = dwg.linearGradient((0, 0), (1, 1))
        else:
            return self.fillcolor
            
        dwg.defs.add(gradient)
        # define the gradient colors
        n_colors = len(self.fillcolor)-1
        stepsize = 1 / (n_colors - 1)
        for i in range(n_colors):
            gradient.add_stop_color(i*stepsize, self.fillcolor[i+1])
            
        return gradient.get_paint_server()  

    def create_bordercolor(self, dwg):
        gradient = ""
        if len(self.bordercolor) < 2:
            return self.bordercolor
        elif self.bordercolor[0] == "radial":
            gradient = dwg.radialGradient()
        elif self.bordercolor[0] == "horizontal":
            gradient = dwg.linearGradient((0, 0), (1, 0))
        elif self.bordercolor[0] == "vertical":
            gradient = dwg.linearGradient((0, 0), (0, 1))
        elif self.bordercolor[0] == "diagonal":
            gradient = dwg.linearGradient((0, 0), (1, 1))
        else:
            return self.bordercolor
            
        dwg.defs.add(gradient)
        # define the gradient colors
        n_colors = len(self.bordercolor)-1
        stepsize = 1 / (n_colors - 1)
        for i in range(n_colors):
            gradient.add_stop_color(i*stepsize, self.bordercolor[i+1])
            
        return gradient.get_paint_server() 

    def generate(self, dwg):
        mirror_transform = self.create_mirror_transform()

        rotation_transform = "rotate(%d, %d, %d)"%(self.orientation, self.position[0], self.position[1])
        
#        bb = dwg.rect(
#                insert       = (self.position[0] - self.bounding_box[0]/2, self.position[1] - self.bounding_box[1]/2),
#                size         = self.bounding_box,
#                fill         = "none",
#                stroke       = "red",
#                stroke_width = 1)
#        dwg.add(bb)
            
        
        n_sides = int(self.n_sides) #int(self.data)
        
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
        
        scaling = min([x_scaling, y_scaling])
        
        # Second pass centering
        points = []
        for i in range(n_sides):
            x = self.position[0] + scaling * (sin((i*2*pi/n_sides) + pi) + x_offset)
            y = self.position[1] + scaling * (cos((i*2*pi/n_sides) + pi) + y_offset)
            points.append((x, y))
        
        svg = dwg.polygon(
                points       = points,
                fill         = self.create_fillcolor(dwg),
                stroke       = self.create_bordercolor(dwg),
                stroke_width = self.borderwidth,
                transform    = " ".join([mirror_transform, rotation_transform]))
        
        if self.class_label != "":
            svg['class']         = self.class_label
        if self.id_label != "":
            svg['id']        = self.id_label
            
        return svg
    

    
if __name__ == '__main__':
    c = RegularPolygon_(x = 3, y = 4, size = 10,  color = "blue", orientation = 30)
    print(c)