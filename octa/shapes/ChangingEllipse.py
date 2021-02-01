# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 16:02:30 2020

@author: Christophe
"""
import svgwrite

class Ellipse:
    parameters = ['position', 'bounding_box', 'orientation' ,'bordercolor', 'borderwidth', 'fillcolor', 'class_label', 'id_label', 'mirror_value']
    
    def __init__(self, **kwargs):
        for p in Ellipse.parameters:
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
    
    def set_mirror_value(self, mirror_value):
        if mirror_value == None:
            mirror_value = ""
            
        self.mirror_value = mirror_value
    

    def __str__(self):
        result = "Ellipse object with params:\n"
        for p in Ellipse.parameters:
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
        
    def generate(self, dwg):
        mirror_transform = self.create_mirror_transform()

        rotation_transform = "rotate(%d, %d, %d)"%(self.orientation, self.position[0], self.position[1])
        
        svg = dwg.ellipse(
                center       = self.position,
                r            = (self.bounding_box[0]/2, self.bounding_box[1]/2),
                fill         = self.fillcolor,
                stroke       = self.bordercolor,
                stroke_width = self.borderwidth,
                transform    = " ".join([mirror_transform, rotation_transform]))
        
        if self.class_label != "":
            svg['class']         = self.class_label
        if self.id_label != "":
            svg['id']        = self.id_label
            
        svg.add(svgwrite.animate.Set(attributeName = "fill", to = "purple", begin = "click", dur = "2s" )) 
        svg.add(svgwrite.animate.Animate(attributeName = "fill", values = "red;orange;green;blue;indigo;violet;red", dur="10s", repeatCount="indefinite")) #to = "red"
        svg.add(svgwrite.animate.Animate(attributeName = "cx", values = "-20;-20;20;20;-20", additive = "sum", dur="5s", repeatCount="indefinite")) #from_ = "0", to = "20"
        svg.add(svgwrite.animate.Animate(attributeName = "cy", values = "20;-20;-20;20;20", additive = "sum", dur="5s", repeatCount="indefinite"))
        
        return svg
    
    
if __name__ == '__main__':
    c = Ellipse(x = 3, y = 4, radius = 10)
    print(c)