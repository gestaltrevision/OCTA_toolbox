# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 12:31:15 2020

@author: Christophe
"""
from octa.Stimulus import Grid, Stimulus
from octa.patterns import GridPattern, Pattern
from octa.shapes import Ellipse, Rectangle, Triangle, Image, Text, Polygon
from octa.measurements import LOCE

#%% Default grid
stimulus = Grid(6,6)
stimulus.x_margin = 0
stimulus.y_margin = 0
stimulus.bounding_boxes = GridPattern.RepeatAcrossRows([(50,50), (10, 10)])
stimulus.Show()

#%%
stimulus = Grid(2,2)
stimulus.fillcolors = GridPattern.MirrorAcrossElements(["red", "green"])
stimulus.Show()

print("LOCE: ", LOCE.CalculateElementsLOCE(stimulus))

#%% Adjusting grid structure dynamically

stimulus = Grid(5, 5,  row_spacing = 50, col_spacing = 50)

stimulus.background_color = "lightgrey"
stimulus.shapes = GridPattern.MirrorAcrossRows([Ellipse, Rectangle, Polygon])
stimulus.data   = GridPattern.MirrorAcrossRows(["", "", "5"])
# stimulus.fillcolors = GridPattern.RandomPattern(["red", "green","blue","orange"], proportions = [0,0.5,.25,.25])
stimulus.Show()

#%% 
stimulus = Grid(6,5)
stimulus.fillcolors = GridPattern.MirrorAcrossRightDiagonal(["red", "green"])
stimulus.Show()

#%% New grid structure: layered grid
center_grid = GridPattern.RepeatAcrossElements(["red"], 2, 2)
outer_layers= Pattern(["green", "blue", "yellow"])
fillcolors = GridPattern.LayeredGrid(center_grid, outer_layers)

stimulus = Grid(fillcolors.n_rows, fillcolors.n_cols)
stimulus.fillcolors = fillcolors
stimulus.Show()

#%% If one attribute has a layered grid structure, attribute dimensions
# can not be changed freely
center_grid = GridPattern.RepeatAcrossElements(["red"], 2, 2)
outer_layers= Pattern(["green", "blue", "yellow"])
fillcolors = GridPattern.LayeredGrid(center_grid, outer_layers)

stimulus = Grid(fillcolors.n_rows, fillcolors.n_cols)
stimulus.fillcolors = fillcolors
stimulus.n_rows = 10
stimulus.Show()

#%% Tiled element grid
source_grid = GridPattern.RepeatAcrossColumns(["red", "green", "blue"], 3, 3)
fillcolors = GridPattern.TiledElementGrid(source_grid, 2)

stimulus = Grid(fillcolors.n_rows, fillcolors.n_cols)
stimulus.fillcolors = fillcolors
stimulus.Show()

#%% Tiled grid
source_grid = GridPattern.RepeatAcrossColumns(["red", "green", "blue"], 3, 3)
fillcolors = GridPattern.TiledGrid(source_grid, (3, 2))

stimulus = Grid(fillcolors.n_rows, fillcolors.n_cols)
stimulus.fillcolors = fillcolors
stimulus.Show()

#%% Swapping elements
center_grid = GridPattern.RepeatAcrossElements([Rectangle], 2, 2)
outer_layers= Pattern([Triangle, Ellipse]).RepeatElements(2)
shapes = GridPattern.LayeredGrid(center_grid, outer_layers)

stimulus = Grid(shapes.n_rows, shapes.n_cols)
stimulus.shapes = shapes
stimulus.fillcolors = GridPattern.RepeatAcrossLeftDiagonal(["red", "green", "blue"])
stimulus.Show()

stimulus.swap_elements(10)
stimulus.Show()

#%% Sizes are always defined using the bounding box parameter
source_grid_1 = GridPattern.RepeatAcrossElements([Rectangle, Triangle, Ellipse],3,3)
source_grid_2 = GridPattern.RepeatAcrossElements([(20, 20), (30, 30), (40, 40)],3,3)

stimulus = Grid(9,9)
stimulus.bounding_boxes = GridPattern.TiledElementGrid(source_grid_2, 3)
stimulus.shapes = GridPattern.TiledGrid(source_grid_1, 3)
stimulus.Show()