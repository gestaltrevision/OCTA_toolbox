# -*- coding: utf-8 -*-
"""
Created on Wed May  6 11:21:53 2020

@author: Christophe

"""


class Droplet:
    
    def __init__(self, **kwargs):
        self.pos = (kwargs['x'], kwargs['y'])
        
        if type(kwargs['size']) == list or type(kwargs['size']) == tuple:
            self.size = kwargs['size']
        elif type(kwargs['size']) == int or type(kwargs['size']) == float:
            self.size = (kwargs['size'], kwargs['size'])
            
        
        if 'colour' in kwargs.keys():
            self.stroke   = kwargs['colour']
        else:
            self.stroke   = 'black'
            
        self.fill   = 'none'
        self.stroke_width = 3
            
        if 'orientation' in kwargs.keys():
            self.orientation = kwargs['orientation']
        else:
            self.orientation = 0
            
        self.transform = "rotate(%d, %d, %d)"%(self.orientation, self.pos[0], self.pos[1])
        
        self._generate_curve()
    
    def _generate_curve(self):
        # move to 
        x = self.pos[0] - self.size[0] / 4
        y = self.pos[1]
        
        move_to = "M %d, %d"%(x, y)
        
        # bezier curve
        x_1 = self.pos[0] - (2/3)*self.size[0]
        y_1 = self.pos[1] + (10/12)*self.size[0]
        x_2 = self.pos[0] + (2/3)*self.size[0] 
        y_2 = self.pos[1] + (10/12)*self.size[0]
        x_t = self.pos[0] + self.size[0] / 4
        y_t = self.pos[1] + self.size[0]
        
        bezier = "C %d, %d, %d, %d, %d, %d"%(x_1, y_1, x_2, y_2, x_t, y_t)
        
        # line 1
        x = self.pos[0]
        y = self.pos[1] - self.size[0] / 2
        
        line_1 = "L %d, %d"%(x, y)
        
        # line 2
        x = self.pos[0] - self.size[0] / 4
        y = self.pos[1]
        
        line_2 = "L %d, %d"%(x, y)
        
        self.d = " ".join([move_to, bezier, line_1, line_2])
        
        
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
    c = FlowerLeave(x = 3, y = 4, size = 10,  colour = "blue", orientation = 30)
    print(c)