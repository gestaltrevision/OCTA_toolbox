# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 16:02:30 2020

@author: Christophe
"""

class Rectangle:
    
    def __init__(self, **kwargs):
        self.pos = (kwargs['x'], kwargs['y'])
        
        if type(kwargs['size']) == list or type(kwargs['size']) == tuple:
            self.size = kwargs['size']
        elif type(kwargs['size']) == int or type(kwargs['size']) == float:
            self.size = (kwargs['size'], kwargs['size'])
            
        self.topleft= (self.pos[0] - self.size[0]/2, self.pos[1] - self.size[1]/2)
        
        if 'colour' in kwargs.keys():
            self.fill   = kwargs['colour']
        else:
            self.fill   = 'black'
            
        if 'orientation' in kwargs.keys():
            self.orientation = kwargs['orientation']
        else:
            self.orientation = 0
            
        self.transform = "rotate(%d, %d, %d)"%(self.orientation, self.pos[0], self.pos[1])
            
    def __str__(self):
        result = "Rectangle object with params:\n"
        result+= "center: (%.2f, %.2f)\n"%self.pos
        result+= "size: (%.2f, %.2f)\n"%self.size
        result+= "fill  : %s\n"%self.fill
        return result
        
    def generate(self, dwg):
        svg = dwg.rect(
                insert    = self.topleft,
                size      = self.size,
                fill      = self.fill,
                transform = self.transform)
        
        return svg
    
    
if __name__ == '__main__':
    c = Rectangle(x = 3, y = 4, size = 10,  colour = "blue", orientation = 30)
    print(c)