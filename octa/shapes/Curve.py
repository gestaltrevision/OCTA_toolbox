# -*- coding: utf-8 -*-
"""
Created on Wed May  6 11:21:53 2020

@author: Christophe

TODO: 
    - Decide what the center coordinates for the curve should be
    - Discuss the name of the class (e.g. Semicircle better represents the shape?)
"""


class Curve:
    
    def __init__(self, **kwargs):
        self.pos = (kwargs['x'], kwargs['y'])
        
        if type(kwargs['size']) == list or type(kwargs['size']) == tuple:
            self.size = kwargs['size']
        elif type(kwargs['size']) == int or type(kwargs['size']) == float:
            self.size = (kwargs['size'], kwargs['size'])
            
        # Moveto parameters
        x = self.pos[0] - self.size[0]/2
        y = self.pos[1] - self.size[0]/4
        
        # Bezier curve parameters
        x_1 = self.pos[0] - self.size[0]/2 + self.size[0] / 5
        y_1 = self.pos[1] + self.size[0] / 4
        x_2 = self.pos[0] + self.size[0] / 2 - self.size[0] /5
        y_2 = self.pos[1] + self.size[0] / 4
        x_t = self.pos[0] + self.size[0] / 2
        y_t = self.pos[1] - self.size[0] / 4
        
        moveto = 'M %d, %d'%(x, y)
        bezier = 'C %d, %d, %d, %d, %d, %d'%(x_1, y_1, x_2, y_2, x_t, y_t)
        
        self.d = moveto + " " + bezier
        
        if 'colour' in kwargs.keys():
            self.fill   = kwargs['colour']
        else:
            self.fill   = 'black'
            
        self.stroke = 'black'
        self.stroke_width = 3
            
        if 'orientation' in kwargs.keys():
            self.orientation = kwargs['orientation']
        else:
            self.orientation = 0
            
        self.transform = "rotate(%d, %d, %d)"%(self.orientation, self.pos[0], self.pos[1])
            
    def __str__(self):
        result = "Curve object with params:\n"
        result+= "center: (%.2f, %.2f)\n"%self.pos
        result+= "size: (%.2f, %.2f)\n"%self.size
        result+= "fill  : %s\n"%self.fill
        result+= "d     :%s"%self.d
        return result
        
    def generate(self, dwg):
        svg = dwg.path(
                d            = self.d,
                stroke       = self.stroke,
                fill         = self.fill,
                stroke_width = self.stroke_width,
                transform    = self.transform)
        
        return svg
    
    
if __name__ == '__main__':
    c = Curve(x = 3, y = 4, size = 10,  colour = "blue", orientation = 30)
    print(c)