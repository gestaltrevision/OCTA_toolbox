# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 16:02:30 2020

@author: Christophe
"""

import base64
from urllib.request import urlopen

class Image:
    parameters = ['position', 'bounding_box', 'orientation' ,'bordercolor', 'borderwidth', 'fillcolor', 'class_label', 'id_label', 'mirror_value', 'data']
    
    def __init__(self, **kwargs):
        for p in Image.parameters:
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
        
    def set_data(self, data):
        if data == None:
            data = ""
            
        ext = [".svg", ".png", ".jpg", ".jpeg", ".bmp", ".gif", \
               ".ico", ".tif", ".tiff", ".webp"]
        
        try:
            image_data = urlopen(data).read()
            encoded = base64.b64encode(image_data).decode()
        except ValueError:  # invalid URL
            if data.endswith(tuple(ext)):
                image_data = open(data, "rb").read() # read file in binary format
                encoded = base64.b64encode(image_data).decode() # read image in base64 encoding
     
        if data.endswith(".svg"):
            data = 'data:image/svg+xml;base64,{}'.format(encoded)
            
        elif data.endswith(".png"):
            data = 'data:image/png;base64,{}'.format(encoded)
            
        elif data.endswith(".jpg") | data.endswith(".jpeg"):
            data = 'data:image/jpeg;base64,{}'.format(encoded)
            
        elif data.endswith(".bmp"):
            data = 'data:image/bmp;base64,{}'.format(encoded)
            
        elif data.endswith(".gif"):
            data = 'data:image/gif;base64,{}'.format(encoded)
            
        elif data.endswith(".ico"):
            data = 'data:image/vnd.microsoft.icon;base64,{}'.format(encoded)
                            
        elif data.endswith(".tif") | data.endswith(".tiff"):
            data = 'data:image/tiff;base64,{}'.format(encoded)
            
        elif data.endswith(".webp"):
            data = 'data:image/webp;base64,{}'.format(encoded)
        
        else:
            data = data

        self.data = data
    

    def create_mirror_transform(self):
        mirror_transform = ""
        if self.mirror_value == "vertical":
            mirror_transform = "scale(-1, 1) translate(%f, 0)"%(-2*self.position[0])
        elif self.mirror_value == "horizontal":
            mirror_transform = "scale(1, -1), translate(0, %f)"%(-2*self.position[1])
        elif self.mirror_value == "horizontalvertical":
            mirror_transform = "scale(-1, -1) translate(%f, %f)"%(-2*self.position[0], -2*self.position[1])
                
        return mirror_transform
    
    def __str__(self):
        result = "Image object with params:\n"
        for p in Image.parameters:
            result += "%s: %s\n"%(p, getattr(self,p))
            
        return result
        
    def generate(self, dwg):
        topleft = (self.position[0] - self.bounding_box[0]/2 , self.position[1] - self.bounding_box[1]/2)
        mirror_transform = self.create_mirror_transform()

        rotation_transform = "rotate(%d, %d, %d)"%(self.orientation, self.position[0], self.position[1])
        
        svg = dwg.image(
                href        = self.data,
                insert      = topleft,
                size        = self.bounding_box,
                
                transform   = " ".join([mirror_transform, rotation_transform]))
        
        if self.class_label != "":
            svg['class']         = self.class_label
        if self.id_label != "":
            svg['id']        = self.id_label
        
#        svg.fit(scale="slice")
        svg.fit(scale="meet")
#        svg.stretch()
        
        return svg
    
    
if __name__ == '__main__':
    c = Image(x = 3, y = 4, size = 10,  color = "blue", orientation = 30, data = 'hello')
    print(c)