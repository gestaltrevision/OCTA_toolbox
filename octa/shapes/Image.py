# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 16:02:30 2020

@author: Christophe
"""

class Image:
    
    def __init__(self, **kwargs):
        self.pos         = (kwargs['x'], kwargs['y'])
        
        if type(kwargs['size']) == list or type(kwargs['size']) == tuple:
            self.size = kwargs['size']
        elif type(kwargs['size']) == int or type(kwargs['size']) == float:
            self.size = (kwargs['size'], kwargs['size'])
        
        self.href = kwargs['data']
        x = self.pos[0] - self.size[0] / 2
        y = self.pos[1] - self.size[1] / 2
        self.insert = (x,y)
        
        self.orientation = kwargs['orientation']
        
        self.transform = "rotate(%d, %d, %d)"%(self.orientation, self.pos[0], self.pos[1])
            
    def __str__(self):
        return ""
        
    def generate(self, dwg):
        svg = dwg.image(
                href        = self.href,
                insert      = self.insert,
                size        = self.size,
                
                transform   = self.transform)
        
        return svg
    
    
if __name__ == '__main__':
    c = Image(x = 3, y = 4, size = 10,  colour = "blue", orientation = 30, data = 'hello')
    print(c)