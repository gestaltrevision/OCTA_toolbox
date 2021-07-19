#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 15:56:47 2020
"""

from octa.Stimulus import Grid, Stimulus
from octa.patterns import GridPattern, Pattern

#%% Default pattern
stimulus = Grid(12, 12)
stimulus.fillcolors = GridPattern.RepeatAcrossRows(["red", "green","blue"])
stimulus.swap_distinct_elements(10)
stimulus.Show()

#%% Mirror across columns
stimulus = Grid(12, 12)
stimulus.fillcolors = GridPattern.MirrorAcrossColumns(["purple", "blue"])
stimulus.Show()

stimulus.fillcolors = GridPattern.MirrorAcrossColumns(["purple", "blue", "green"])
stimulus.Show()

#%% Mirror across rows
stimulus = Grid(12, 12)
stimulus.fillcolors = GridPattern.MirrorAcrossRows(["purple", "blue"])
stimulus.Show()

stimulus.fillcolors = GridPattern.MirrorAcrossRows(["purple", "blue", "green"])
stimulus.Show()

#%% Mirror across leftdiagonal
stimulus = Grid(3, 6)
stimulus.fillcolors = GridPattern.MirrorAcrossLeftDiagonal(["purple", "blue"])
stimulus.Show()

stimulus.fillcolors = GridPattern.MirrorAcrossLeftDiagonal(["purple", "blue", "green"])
stimulus.Show()
#%% Mirror across rightdiagonal
stimulus = Grid(3, 6)
stimulus.fillcolors = GridPattern.MirrorAcrossRightDiagonal(["purple", "blue"])
stimulus.Show()

stimulus.fillcolors = GridPattern.MirrorAcrossRightDiagonal(["purple", "blue", "green"])
stimulus.Show()

#%% Alternate rows
stimulus = Grid(12, 12)
stimulus.fillcolors = GridPattern.RepeatAcrossRows(["purple", "blue"])
stimulus.Show()

stimulus.fillcolors = GridPattern.RepeatAcrossRows(["purple", "blue", "green"])
stimulus.Show()

#%% Alternate columns
stimulus = Grid(12, 12)
stimulus.fillcolors = GridPattern.RepeatAcrossColumns(["purple", "blue"])
stimulus.Show()

stimulus.fillcolors = GridPattern.RepeatAcrossColumns(["purple", "blue", "green"])
stimulus.Show()

#%% Alternate across leftdiagonal
stimulus = Grid(3, 6)
stimulus.fillcolors = GridPattern.RepeatAcrossLeftDiagonal(["purple", "blue"])
stimulus.Show()

stimulus.fillcolors = GridPattern.RepeatAcrossLeftDiagonal(["purple", "blue", "green"])
stimulus.Show()

#%% Alternate across rightdiagonal
stimulus = Grid(3, 6)
stimulus.fillcolors = GridPattern.RepeatAcrossRightDiagonal(["purple", "blue"])
stimulus.Show()

stimulus.fillcolors = GridPattern.RepeatAcrossRightDiagonal(["purple", "blue", "green"])
stimulus.Show()

#%% Repeat across rows
stimulus = Grid(12, 12)
stimulus.fillcolors = GridPattern.RepeatAcrossRows(Pattern(["purple", "blue"]).RepeatElements(3))
stimulus.Show()

stimulus = Grid(12, 12)
stimulus.fillcolors = GridPattern.RepeatAcrossRows(Pattern(["purple", "blue", "green"]).RepeatElements(2))
stimulus.Show()

#%% Repeat across columns
stimulus = Grid(12, 12)
stimulus.fillcolors = GridPattern.RepeatAcrossColumns(Pattern(["purple", "blue"]).RepeatElements(3))
stimulus.Show()

stimulus = Grid(12, 12)
stimulus.fillcolors = GridPattern.RepeatAcrossColumns(Pattern(["purple", "blue", "green"]).RepeatElements(2))
stimulus.Show()

#%% Repeat across leftdiagonal
stimulus = Grid(12, 12)
stimulus.fillcolors = GridPattern.RepeatAcrossLeftDiagonal(Pattern(["purple", "blue"]).RepeatElements(3))
stimulus.Show()

stimulus = Grid(12, 12)
stimulus.fillcolors = GridPattern.RepeatAcrossLeftDiagonal(Pattern(["purple", "blue", "green"]).RepeatElements(2))
stimulus.Show()

#%% Repeat across rightdiagonal
stimulus = Grid(12, 12)
stimulus.fillcolors = GridPattern.RepeatAcrossRightDiagonal(Pattern(["purple", "blue"]).RepeatElements(3))
stimulus.Show()

stimulus = Grid(12, 12)
stimulus.fillcolors = GridPattern.RepeatAcrossRightDiagonal(Pattern(["purple", "blue", "green"]).RepeatElements(2))
stimulus.Show()

#%% Subgroups
tiled_grid_1 = GridPattern.TiledElementGrid(GridPattern.MirrorAcrossRightDiagonal(["purple", "blue"], 2 , 2),6)

stimulus = Grid(tiled_grid_1.n_rows, tiled_grid_1.n_cols)
stimulus.fillcolors = tiled_grid_1
stimulus.Show()


tiled_grid_2 = GridPattern.TiledElementGrid(GridPattern.MirrorAcrossRightDiagonal(["purple", "blue", "green"], 3, 3), 4)
stimulus.fillcolors = tiled_grid_2
stimulus.Show()

#%% Outin
stimulus = Grid(12,12)

colors_1 = Pattern(["green","blue"]).RepeatPatternToSize(count = 6)
center_grid = GridPattern.RepeatAcrossElements(Pattern(colors_1.pattern[0]), 2, 2)
outer_layers= Pattern(colors_1.pattern[1:])
stimulus.fillcolors  = GridPattern.LayeredGrid(center_grid, outer_layers)

stimulus.Show()


stimulus = Grid(12,12)

colors_1 = Pattern(["green","blue", "purple"]).RepeatPatternToSize(count = 6)
center_grid = GridPattern.RepeatAcrossElements(Pattern(colors_1.pattern[0]), 2, 2)
outer_layers= Pattern(colors_1.pattern[1:])
stimulus.fillcolors  = GridPattern.LayeredGrid(center_grid, outer_layers)

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
fillcolors = GridPattern.TiledGrid(source_grid, 6)

stimulus = Grid(fillcolors.n_rows, fillcolors.n_cols)
stimulus.fillcolors = fillcolors
stimulus.Show()

source_grid = GridPattern.RepeatAcrossElements(["purple", "blue", "green", "purple"], 2, 2)
fillcolors = GridPattern.TiledGrid(source_grid, 6)

stimulus = Grid(fillcolors.n_rows, fillcolors.n_cols)
stimulus.fillcolors = fillcolors
stimulus.Show()
