#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 15:56:47 2020

@author: rudy
"""

from octa.Stimulus import Grid, Stimulus
from octa.patterns import GridPattern, Pattern

#%% Default pattern
stimulus = Grid(6, 6)
stimulus.positions.JitterLocations(axis="xy", distribution = "normal", mu = 10, std = 10)
stimulus.x_margin = 40
stimulus.y_margin = 40
stimulus.Show()

#%% Mirror across columns
stimulus = Grid(6, 6)
stimulus.fillcolors = GridPattern.MirrorAcrossColumns(["purple", "blue"])
stimulus.Show()

stimulus.fillcolors = GridPattern.MirrorAcrossColumns(["purple", "blue", "green"])
stimulus.Show()

#%% Mirror across rows
stimulus = Grid(6, 6)
stimulus.fillcolors = GridPattern.MirrorAcrossRows(["purple", "blue"])
stimulus.Show()

stimulus.fillcolors = GridPattern.MirrorAcrossRows(["purple", "blue", "green"])
stimulus.Show()

#%% Alternate rows
stimulus = Grid(6, 6)
stimulus.fillcolors = GridPattern.RepeatAcrossRows(["purple", "blue"])
stimulus.Show()

stimulus.fillcolors = GridPattern.RepeatAcrossRows(["purple", "blue", "green"])
stimulus.Show()

#%% Alternate columns
stimulus = Grid(6, 6)
stimulus.fillcolors = GridPattern.RepeatAcrossColumns(["purple", "blue"])
stimulus.Show()

stimulus.fillcolors = GridPattern.RepeatAcrossColumns(["purple", "blue", "green"])
stimulus.Show()

#%% Repeat across rows
stimulus = Grid(6, 6)
stimulus.fillcolors = GridPattern.RepeatAcrossColumns(Pattern(["purple", "blue"]).RepeatElements(3))
stimulus.Show()

stimulus = Grid(6, 6)
stimulus.fillcolors = GridPattern.RepeatAcrossColumns(Pattern(["purple", "blue", "green"]).RepeatElements(2))
stimulus.Show()

#%% Repeat across columns
stimulus = Grid(6, 6)
stimulus.fillcolors = GridPattern.RepeatAcrossRows(Pattern(["purple", "blue"]).RepeatElements(3))
stimulus.Show()

stimulus = Grid(6, 6)
stimulus.fillcolors = GridPattern.RepeatAcrossRows(Pattern(["purple", "blue", "green"]).RepeatElements(2))
stimulus.Show()

#%% Subgroups
tiled_grid_1 = GridPattern.TiledElementGrid(GridPattern.MirrorAcrossRightDiagonal(["purple", "blue"], 2 , 2),3)

stimulus = Grid(tiled_grid_1.n_rows, tiled_grid_1.n_cols)
stimulus.fillcolors = tiled_grid_1
stimulus.Show()


tiled_grid_2 = GridPattern.TiledElementGrid(GridPattern.MirrorAcrossRightDiagonal(["purple", "blue", "green"], 3, 3), 2)
stimulus.fillcolors = tiled_grid_2
stimulus.Show()

#%% Outin
center_grid = GridPattern.RepeatAcrossElements(["purple"], 2, 2)
outer_layers= Pattern(["blue", "purple"])
fillcolors  = GridPattern.LayeredGrid(center_grid, outer_layers)

stimulus = Grid(fillcolors.n_rows, fillcolors.n_cols)
stimulus.fillcolors = fillcolors
stimulus.Show()

center_grid = GridPattern.RepeatAcrossElements(["green"], 2, 2)
outer_layers= Pattern(["blue", "purple"])
fillcolors  = GridPattern.LayeredGrid(center_grid, outer_layers)
stimulus.fillcolors = fillcolors
stimulus.Show()

#%% Outin with different center grid dimensions
center_grid = GridPattern.RepeatAcrossElements(["green"], 2, 4)
outer_layers= Pattern(["blue", "purple"])
fillcolors  = GridPattern.LayeredGrid(center_grid, outer_layers)

stimulus = Grid(fillcolors.n_rows, fillcolors.n_cols)
stimulus.fillcolors = fillcolors
stimulus.Show()

#%% Checkerboard
source_grid = GridPattern.RepeatAcrossElements(["purple", "blue", "blue", "purple"], 2, 2)
fillcolors = GridPattern.TiledGrid(source_grid, 3)

stimulus = Grid(fillcolors.n_rows, fillcolors.n_cols)
stimulus.fillcolors = fillcolors
stimulus.Show()

source_grid = GridPattern.RepeatAcrossElements(["purple", "blue", "green", "purple"], 2, 2)
fillcolors = GridPattern.TiledGrid(source_grid, 3)

stimulus = Grid(fillcolors.n_rows, fillcolors.n_cols)
stimulus.fillcolors = fillcolors
stimulus.Show()