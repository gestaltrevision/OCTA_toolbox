# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 12:31:15 2020

@author: Christophe
"""
from octa.Stimulus import Stimulus
from octa.Positions import Positions
from octa import shapes, patterns
from octa.patterns import GridPattern, Pattern

### SUBGROUP PATTERN ###

n_rows = 12
n_cols = 6

row_spacing = 40
col_spacing = 40

x_offset = 50
y_offset = 50

stimulus = Stimulus(background_color = "white")

# stimulus.positions   = Positions.Create2DGrid(n_rows, n_cols, row_spacing, col_spacing, x_offset, y_offset)
# stimulus.shapes      = patterns.Pattern([shapes.Triangle, shapes.Rectangle]).RepeatPatternToSize(n_rows * n_cols)
# stimulus.size        = patterns.BasicPattern([20, (10, 20)]).DuplicatePatternToSize(n_rows * n_cols)
# stimulus.colour      = patterns.GridRepeater(["red", "green", "blue"], n_rows, n_cols).RepeatElementsInSubgroups()
# stimulus.orientation = patterns.SymmetryPattern([0,12,45], n_rows, n_cols).MirrorAcrossColumns()
# stimulus.data        = patterns.BasicPattern(["none"]).DuplicatePatternToSize(n_rows * n_cols)
# stimulus.Render()
# stimulus.Show()

# g = print(GridPattern.RepeatElements([10, 20, 30]))

# g = print(GridPattern.RepeatAcrossRows([10, 20, 30]))

# g = print(GridPattern.RepeatAcrossColumns([10, 20, 30]))

# g = print(GridPattern.RepeatAcrossRightDiagonal([10, 20, 30]))

# g = print(GridPattern.RepeatAcrossLeftDiagonal([10, 20, 30]))

# g = print(GridPattern.MirrorElements([10, 20, 30]))

# g = print(GridPattern.MirrorAcrossRows([10, 20, 30]))

# g = print(GridPattern.MirrorAcrossColumns([10, 20, 30]))

# g = print(GridPattern.MirrorAcrossLeftDiagonal([10, 20, 30]))

# g = print(GridPattern.MirrorAcrossRightDiagonal([10, 20, 30]))

center_grid = GridPattern.RepeatElements([1], 2, 2)
outer_layers= Pattern([7, 8, 9])
g = GridPattern.LayeredGrid(center_grid, outer_layers)
print(g.generate())