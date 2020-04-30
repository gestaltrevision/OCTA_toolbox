# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 16:02:30 2020

@author: Christophe
"""
import math

class Triangle:
    
    def __init__(self, **kwargs):
        self.pos = (kwargs['x'], kwargs['y'])
        
        if type(kwargs['size']) == list or type(kwargs['size']) == tuple:
            self.diameter = kwargs['size']
        elif type(kwargs['size']) == int or type(kwargs['size']) == float:
            self.diameter = (kwargs['size'], kwargs['size'])
      
        self.points = [(self.pos[0], self.pos[1] - (self.diameter[1]/2)), 
                       (self.pos[0] - (self.diameter[0]/2), self.pos[1] + (self.diameter[1]/2)), 
                       (self.pos[0] + (self.diameter[0]/2), self.pos[1] + (self.diameter[1]/2))]
#        for deg in [90, 210, 330]:
#            rad = math.radians(deg + 180)
#            self.points.append((self.pos[0] + self.diameter * math.cos(rad), self.pos[1] + self.diameter * math.sin(rad)))
        
        if 'colour' in kwargs.keys():
            self.fill   = kwargs['colour']
        else:
            self.fill   = 'black'
            
        if 'orientation' in kwargs.keys():
            self.orientation = kwargs['orientation']
        else:
            self.orientation = 0
            
        if 'mirror' in kwargs.keys():
            self.mirror = kwargs['mirror']
        else:
            self.mirror = 'none'
            
        self.transform = "rotate(%d, %d, %d)"%(self.orientation, self.pos[0], self.pos[1])
            
    def __str__(self):
        result = "Triangle object with params:\n"
        result+= "points: %s\n"%str(self.points)
        result+= "diameter: %.2f\n"%self.diameter
        result+= "fill  : %s\n"%self.fill
        return result
        
    def generate(self, dwg):
        svg = dwg.polygon(
                points = self.points,
                fill   = self.fill,
                transform = self.transform)
        
        return svg
    
    
if __name__ == '__main__':
    c = Triangle(x = 3, y = 4, size = 10)
    print(c)