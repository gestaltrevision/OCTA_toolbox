# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 12:31:15 2020

@author: Christophe
"""
from octa.Stimulus import Grid, Circles
from octa.Positions import Positions
from octa.patterns import GridPattern, Pattern
from octa.shapes import Ellipse, Rectangle

colours = GridPattern.LayeredGrid(GridPattern.RepeatElements(["blue"], 2, 2), Pattern(["red", "green", "blue"]))
shapes  = GridPattern.LayeredGrid(GridPattern.RepeatElements([Ellipse], 2, 2), Pattern([Rectangle, Ellipse, Rectangle]))
n_rows, n_cols = colours.get_dimensions()

stimulus = Grid(n_rows, n_cols, x_offset = 20, y_offset = 20)
stimulus.size = GridPattern.RepeatElements([30])
stimulus.shapes = shapes
stimulus.colours = colours
stimulus.Show()

