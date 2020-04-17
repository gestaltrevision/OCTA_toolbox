# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 16:02:30 2020

@author: Christophe
"""

class Circle:
    
    def __init__(self, **kwargs):
        self.center = (kwargs['x'], kwargs['y'])
        self.radius = kwargs['radius']
        
        if 'colour' in kwargs.keys():
            self.fill   = kwargs['colour']
        else:
            self.fill   = 'black'
            
    def __str__(self):
        result = "Circle object with params:\n"
        result+= "center: (%.2f, %.2f)\n"%self.center
        result+= "radius: %.2f\n"%self.radius
        result+= "fill  : %s\n"%self.fill
        return result
        
    def generate(self, dwg):
        circle = dwg.circle(
                center = self.center,
                r      = self.radius,
                fill   = self.fill)
        
        return circle
    
    
if __name__ == '__main__':
    c = Circle(x = 3, y = 4, radius = 10)
    print(c)