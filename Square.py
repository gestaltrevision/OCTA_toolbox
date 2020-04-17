# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 16:02:30 2020

@author: Christophe
"""

class Square:
    
    def __init__(self, **kwargs):
        self.center = (kwargs['x'], kwargs['y'])
        self.size = (kwargs['radius'], kwargs['radius'])
        
        self.topleft= (self.center[0] - self.size[0]/2, self.center[1] - self.size[0]/2)
        
        if 'colour' in kwargs.keys():
            self.fill   = kwargs['colour']
        else:
            self.fill   = 'black'
            
    def __str__(self):
        result = "Square object with params:\n"
        result+= "center: (%.2f, %.2f)\n"%self.center
        result+= "size: (%.2f, %.2f)\n"%self.size
        result+= "fill  : %s\n"%self.fill
        return result
        
    def generate(self, dwg):
        svg = dwg.rect(
                insert = self.topleft,
                size   = self.size,
                fill   = self.fill)
        
        return svg
    
    
if __name__ == '__main__':
    c = Square(x = 3, y = 4, radius = 10)
    print(c)