# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 16:02:30 2020

@author: Christophe
"""

class Text:
    
    def __init__(self, **kwargs):
        self.pos         = (kwargs['x'], kwargs['y'])
        
        if type(kwargs['size']) == list or type(kwargs['size']) == tuple:
            self.size = kwargs['size']
        elif type(kwargs['size']) == int or type(kwargs['size']) == float:
            self.size = (kwargs['size'], kwargs['size'])
        
        self.fill        = kwargs['colour']
        self.style       = "text-align = middle;"
        self.text        = kwargs['data']
        self.textLength  = len(self.text)
        self.font_weight = '700'
        self.font_family = 'Trebuchet MS'
        
        x = self.pos[0] - self.size[0] / 2
        y = self.pos[1] + self.size[1] / 16
        self.insert = (x,y)
        self.orientation = kwargs['orientation']
        
        self.transform = "rotate(%d, %d, %d)"%(self.orientation, self.pos[0], self.pos[1])
            
    def __str__(self):
        result = "Rectangle object with params:\n"
        result+= "center: (%.2f, %.2f)\n"%self.pos
        result+= "size: (%.2f, %.2f)\n"%self.size
        result+= "fill  : %s\n"%self.fill
        return result
        
    def generate(self, dwg):
        svg = dwg.text(
                text        = self.text,
                insert      = self.insert,
                fill        = self.fill,
                textLength  = self.textLength,
                font_size   = self.size[0]/4,
                font_weight = self.font_weight,
                transform   = self.transform)
        
        return svg
    
    
if __name__ == '__main__':
    c = Text(x = 3, y = 4, size = 10,  colour = "blue", orientation = 30, data = 'hello')
    print(c)