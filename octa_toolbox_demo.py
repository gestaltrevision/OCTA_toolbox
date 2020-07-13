# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 12:31:15 2020

@author: Christophe
"""
from octa.Stimulus import Grid, Stimulus
from octa.patterns import GridPattern, Pattern
from octa.shapes import Ellipse, Rectangle, Triangle, Image, Text, Polygon, RegularPolygon
from octa.measurements import LOCE

#%%
def rgb2hex(r,g,b):
    return "#{:02x}{:02x}{:02x}".format(round(r*255),round(g*255),round(b*255))

#%% Default grid
stimulus = Grid(6,6, background_color = "lightgrey")
stimulus.bounding_boxes = GridPattern.RandomPattern([(50,50)])

stimulus = Grid(6,6, background_color = "lightgrey", x_margin = 0, y_margin = 0)
stimulus._autosize_method = "maximum_bounding_box"
stimulus.bounding_boxes = GridPattern.RandomPattern([(50,50), (10,10)], counts = [18,18])
stimulus.Show()

#%% RGB colors
stimulus = Grid(6,6, background_color = "white", x_margin = 0, y_margin = 0, row_spacing = 80, col_spacing = 50)
stimulus._autosize_method = "maximum_bounding_box"
#stimulus._autosize_method = "tight_fit"
stimulus.shapes = GridPattern.RepeatAcrossElements([Polygon, RegularPolygon])
stimulus.bounding_boxes = GridPattern.RepeatAcrossRows([(50,80)])
stimulus.data = GridPattern.RepeatAcrossRows([3,3,5,5,6,6])
stimulus.orientations = GridPattern.RepeatAcrossRows([0,180])
stimulus.borderwidths = GridPattern.RepeatAcrossElements([1])
stimulus.bordercolors = GridPattern.RepeatAcrossElements(["black"])

#stimulus.fillcolors = GridPattern.MirrorAcrossRows([rgb2hex(0.30294,0.78057,0.90983)])
#stimulus.fillcolors = GridPattern.RepeatAcrossRows(['#7FE5FF', '#38AEE8', '#0079B0'])
stimulus.fillcolors = GridPattern.RepeatAcrossColumns(['#6dd6ff', '#1b9fd8', '#006ca1'])
## OR LESS RISKY:
#stimulus.fillcolors = GridPattern.RepeatAcrossColumns(['#5cc8ff', '#1b9fd8', '#0078af'])
# OR EVEN CLOSER:
#stimulus.fillcolors = GridPattern.RepeatAcrossRows(['#4bbaf5', '#1b9fd8', '#0085bc'])
                                                    
#stimulus.swap_distinct_elements(1, distinction_features = ['shapes', 'bounding_boxes', 'fillcolors', 'orientations', 'data'])
stimulus.Show()

#%% RGB colors
stimulus = Grid(6,6, background_color = "white", x_margin = 0, y_margin = 0, row_spacing = 50, col_spacing = 50)
stimulus._autosize_method = "maximum_bounding_box"
#stimulus._autosize_method = "tight_fit"
stimulus.shapes = GridPattern.RepeatAcrossElements([RegularPolygon])
stimulus.bounding_boxes = GridPattern.RepeatAcrossRows([(45,45)])
stimulus.data = GridPattern.RepeatAcrossRows([6,8,10])
stimulus.orientations = GridPattern.RepeatAcrossRows([0])
#stimulus.borderwidths = GridPattern.RepeatAcrossElements([1])
#stimulus.bordercolors = GridPattern.RepeatAcrossElements(["black"])

#stimulus.fillcolors = GridPattern.MirrorAcrossRows([rgb2hex(0.30294,0.78057,0.90983)])
#stimulus.fillcolors = GridPattern.RepeatAcrossRows(['#7FE5FF', '#38AEE8', '#0079B0'])
stimulus.fillcolors = GridPattern.RepeatAcrossColumns(['#6dd6ff', '#1b9fd8', '#006ca1'])
## OR LESS RISKY:
#stimulus.fillcolors = GridPattern.RepeatAcrossColumns(['#5cc8ff', '#1b9fd8', '#0078af'])
# OR EVEN CLOSER:
#stimulus.fillcolors = GridPattern.RepeatAcrossRows(['#4bbaf5', '#1b9fd8', '#0085bc'])
                                                    
#stimulus.swap_distinct_elements(1, distinction_features = ['shapes', 'bounding_boxes', 'fillcolors', 'orientations', 'data'])
stimulus.Show()

#%%
stimulus = Grid(5,2)
stimulus.fillcolors = GridPattern.MirrorAcrossElements(["red", "green", "blue"])
stimulus.Show()

print("LOCE: ", LOCE.CalculateElementsLOCE(stimulus))

#%% Size parameter
stimulus = Grid(7,6, background_color = "gray", size = (350, 350), x_margin = 23, y_margin = 10)
stimulus.shapes = GridPattern.MirrorAcrossColumns([Rectangle, Triangle])
stimulus.bounding_boxes = GridPattern.RepeatAcrossRows([ (24, 24), (46, 30)])
stimulus.Show()

#%% MirrorAcrossElements
stimulus = Grid(5,2)
stimulus.fillcolors = GridPattern.MirrorAcrossElements(["red", "green"])
stimulus.Show()

#%% Request list of pattern values
#stimulus.shapes.generate().pattern


#%% Adjusting grid structure dynamically

stimulus = Grid(5, 5,  row_spacing = 50, col_spacing = 50)

stimulus.background_color = "lightgrey"
stimulus.shapes = GridPattern.MirrorAcrossRows([Ellipse, Rectangle, Polygon])
stimulus.data   = GridPattern.MirrorAcrossRows(["", "", "5"])
stimulus.fillcolors = GridPattern.RandomPattern(["red", "green","blue","orange"], counts = [5,5,10,5])
stimulus.Show()

#%% 
stimulus = Grid(6,5)
stimulus.fillcolors = GridPattern.MirrorAcrossRightDiagonal(["red", "green"])
stimulus.Show()

stimulus.shapes = GridPattern.RepeatAcrossRows([Triangle, Polygon])
stimulus.data   = GridPattern.RepeatAcrossRows(["", "3"])
stimulus.orientations = GridPattern.RepeatAcrossRows([0,0])

stimulus.Show()
