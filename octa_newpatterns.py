# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 12:31:15 2020

@author: Christophe
"""
from octa.Stimulus import Grid
from octa.Positions import Positions
from octa.patterns import GridPattern, Pattern
from octa.shapes import Ellipse, Rectangle, Triangle, Image, Text, Polygon

center_grid  = GridPattern.RepeatElements([(20, 20)], 3, 3)
outer_layers = Pattern([(30, 30), (40, 40), (50 ,50)])
orientations = GridPattern.LayeredGrid(center_grid, outer_layers)


stimulus = Grid(9, 9, x_offset = 40, y_offset = 40, row_spacing = 50, col_spacing = 50)
stimulus.bounding_boxes = orientations 
stimulus.shapes         = GridPattern.RepeatElements([Triangle])
stimulus.orientations   = GridPattern.RepeatElements([0])
stimulus.borderwidths   = GridPattern.RepeatElements([1])
stimulus.bordercolours  = GridPattern.RepeatElements(["red", "green", "blue"])
stimulus.fillcolours    = GridPattern.RepeatElements(["green", "blue", "red"])
stimulus.data           = GridPattern.RepeatElements(["hello everybody in the houses tonight how","","5"])

stimulus.Show()

#%%
src = GridPattern.RepeatElements(["red", "green", "blue"], 4, 4)
p = GridPattern.TiledElementGrid(src, 2)

stimulus = Grid(8, 8, x_offset = 40, y_offset = 40, row_spacing = 20, col_spacing = 20)
stimulus.fillcolours = p
stimulus.Show()
