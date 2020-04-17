# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 16:02:30 2020

@author: Christophe
"""

class Ellipse:
    
    def __init__(self, **kwargs):
        self.pos = (kwargs['x'], kwargs['y'])
        
        
        if type(kwargs['size']) == list or type(kwargs['size']) == tuple:
            self.radius = kwargs['size']
        elif type(kwargs['radius']) == int or type(kwargs['size']) == float:
            self.radius = (kwargs['size'], kwargs['size'])
        
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
        result = "Ellipse object with params:\n"
        result+= "center: (%.2f, %.2f)\n"%self.pos
        result+= "radius: %s\n"%str(self.radius)
        result+= "fill  : %s\n"%self.fill
        return result
        
    def generate(self, dwg):
        ellipse = dwg.ellipse(
                center    = self.pos,
                r         = (self.radius[0], self.radius[1]),
                fill      = self.fill,
                transform = self.transform)
        
        return ellipse
    
    
if __name__ == '__main__':
    c = Ellipse(x = 3, y = 4, size = (10,10))
    print(c)