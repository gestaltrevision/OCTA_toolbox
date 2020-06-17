# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 12:31:15 2020

@author: Christophe
"""
from octa.Stimulus import Grid, Stimulus
from octa.patterns import GridPattern, Pattern
from octa.shapes import Ellipse, Rectangle, Triangle, Image, Text, Polygon

#%% Default grid
stimulus = Grid(5,5, x_offset = 40, y_offset = 40)
stimulus.Show()

#%% Adjusting grid structure dynamically
stimulus = Grid(9, 9, x_offset = 40, y_offset = 40, row_spacing = 50, col_spacing = 50)
stimulus.shapes = GridPattern.MirrorAcrossRows([Ellipse, Rectangle, Triangle])
stimulus.fillcolours = GridPattern.MirrorAcrossColumns(["red", "green","blue","orange"])
stimulus.Show()

stimulus.n_rows = 5
stimulus.Show()

#%% New grid structure: layered grid
center_grid = GridPattern.RepeatElements(["red"], 2, 2)
outer_layers= Pattern(["green", "blue", "yellow"])
fillcolours = GridPattern.LayeredGrid(center_grid, outer_layers)

stimulus = Grid(fillcolours.n_rows, fillcolours.n_cols, x_offset = 40, y_offset = 40)
stimulus.fillcolours = fillcolours
stimulus.Show()

#%% If one attribute has a layered grid structure, attribute dimensions
# can not be changed freely
center_grid = GridPattern.RepeatElements(["red"], 2, 2)
outer_layers= Pattern(["green", "blue", "yellow"])
fillcolours = GridPattern.LayeredGrid(center_grid, outer_layers)

stimulus = Grid(fillcolours.n_rows, fillcolours.n_cols, x_offset = 40, y_offset = 40)
stimulus.fillcolours = fillcolours
stimulus.n_rows = 10
stimulus.Show()

#%% Tiled element grid
source_grid = GridPattern.RepeatAcrossColumns(["red", "green", "blue"], 3, 3)
fillcolours = GridPattern.TiledElementGrid(source_grid, 2)

stimulus = Grid(fillcolours.n_rows, fillcolours.n_cols, x_offset = 40, y_offset = 40)
stimulus.fillcolours = fillcolours
stimulus.Show()

#%% Tiled grid
source_grid = GridPattern.RepeatAcrossColumns(["red", "green", "blue"], 3, 3)
fillcolours = GridPattern.TiledGrid(source_grid, (3, 2))

stimulus = Grid(fillcolours.n_rows, fillcolours.n_cols, x_offset = 40, y_offset = 40)
stimulus.fillcolours = fillcolours
stimulus.Show()

#%% Swapping elements
center_grid = GridPattern.RepeatElements([Rectangle], 2, 2)
outer_layers= Pattern([Triangle, Ellipse]).RepeatElements(2)
shapes = GridPattern.LayeredGrid(center_grid, outer_layers)

stimulus = Grid(shapes.n_rows, shapes.n_cols, x_offset = 20, y_offset = 20)
stimulus.shapes = shapes
stimulus.fillcolours = GridPattern.RepeatAcrossLeftDiagonal(["red", "green", "blue"])
stimulus.Show()

stimulus.swap_elements(10)
stimulus.Show()

#%% Sizes are always defined using the bounding box parameter
source_grid_1 = GridPattern.RepeatElements([Rectangle, Triangle, Ellipse],3,3)
source_grid_2 = GridPattern.RepeatElements([(20, 20), (30, 30), (40, 40)],3,3)

stimulus = Grid(9,9, x_offset = 40, y_offset = 40)
stimulus.bounding_boxes = GridPattern.TiledElementGrid(source_grid_2, 3)
stimulus.shapes = GridPattern.TiledGrid(source_grid_1, 3)
stimulus.Show()