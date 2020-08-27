# -*- coding: utf-8 -*-
"""

"""
import svgwrite
import svgpathtools

class Path:
    parameters = ['position', 'bounding_box', 'orientation' ,'bordercolor', 'borderwidth', 'fillcolor', 'class_label', 'id_label', 'mirror_value', 'data']
    
    def __init__(self, **kwargs):
        for p in Path.parameters:
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
    

    def create_mirror_transform(self):
        mirror_transform = ""
        if self.mirror == "horizontal":
            mirror_transform = "scale(-1, 1) translate(%f, 0)"%(-2*self.position[0])
        elif self.mirror == "vertical":
            mirror_transform = "scale(1, -1), translate(0, %f)"%(-2*self.position[1])
        elif self.mirror == "horizontalvertical":
            mirror_transform = "scale(-1, -1) translate(%f, %f)"%(-2*self.position[0], -2*self.position[1])
                
        return mirror_transform
    
    def __str__(self):
        result = "Path object with params:\n"
        for p in Path.parameters:
            result += "%s: %s\n"%(p, getattr(self,p))
            
        return result
        
    def generate(self, dwg):
        topleft = (self.position[0] - self.bounding_box[0]/2 , self.position[1] - self.bounding_box[1]/2)
                          
        xsize = self.data[1]
        ysize = self.data[2]
        scale_x_parameter = self.bounding_box[0] / xsize
        scale_y_parameter = self.bounding_box[0] / ysize
        
        sizeposition_transform = "scale(%f, %f) translate(%f, %f)"%(scale_x_parameter, scale_y_parameter, (topleft[0]/scale_x_parameter), (topleft[1]/scale_y_parameter))

        mirror_transform = self.create_mirror_transform()  
        
        rotation_transform = "rotate(%d, %d, %d)"%(self.orientation, xsize/2, ysize/2)
               
        svg = dwg.path(
                d            = self.data[0],              
                fill         = self.fillcolor,
                stroke       = self.bordercolor,
                stroke_width = self.borderwidth,
                transform    = " ".join([mirror_transform, sizeposition_transform,  rotation_transform]))#,
#                insert      = topleft,
#                size        = self.bounding_box)
                
#                extra = 
                
#                transform   = " ".join([mirror_transform, rotation_transform]))
        
        return svg
    
    
if __name__ == '__main__':
    c = Path(x = 3, y = 4, size = 10,  color = "blue", orientation = 30, data = 'hello')
    print(c)