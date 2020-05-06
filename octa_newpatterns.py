# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 12:31:15 2020

@author: Christophe
"""
from octa.Stimulus import Stimulus
from octa.Positions import Positions
from octa import shapes, patterns

### SUBGROUP PATTERN ###

n_rows = 12
n_cols = 6

row_spacing = 40
col_spacing = 40

x_offset = 50
y_offset = 50

stimulus = Stimulus(background_color = "white")

stimulus.positions   = Positions.Create2DGrid(n_rows, n_cols, row_spacing, col_spacing, x_offset, y_offset)
stimulus.shapes      = patterns.BasicPattern([shapes.Triangle, shapes.Rectangle]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.size        = patterns.BasicPattern([20, (10, 20)]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.colour      = patterns.GridRepeater(["red", "green", "blue"], n_rows, n_cols).RepeatElementsInSubgroups()
stimulus.orientation = patterns.SymmetryPattern([0,12,45], n_rows, n_cols).MirrorAcrossColumns()
stimulus.data        = patterns.BasicPattern(["none"]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.Render()
stimulus.Show()
#stimulus.SaveJSON(r'output/test_stimulus')
#stimulus.SaveSVG(r'output/test_stimulus')

#%%

### CHECKERBOARD PATTERN - 2 VALUES ###
n_rows = 8
n_cols = 6

row_spacing = 50
col_spacing = 50

x_offset = 50
y_offset = 50

stimulus = Stimulus(background_color = "white")

stimulus.positions   = Positions.Create2DGrid(n_rows, n_cols, row_spacing, col_spacing, x_offset, y_offset)
stimulus.shapes      = patterns.BasicPattern([shapes.Rectangle]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.size        = patterns.BasicPattern([20]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.colour      = patterns.GridRepeater(["red", "green"], n_rows, n_cols).RepeatPatternInCheckerboard()
stimulus.orientation = patterns.SymmetryPattern([0], n_rows, n_cols).MirrorAcrossColumns()
stimulus.data        = patterns.BasicPattern(["none"]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.Render()
stimulus.Show()
#stimulus.SaveJSON(r'output/test_stimulus')
#stimulus.SaveSVG(r'output/test_stimulus')

#%%

### CHECKERBOARD PATTERN - 3 VALUES ###
n_rows = 8
n_cols = 6

row_spacing = 50
col_spacing = 50

x_offset = 50
y_offset = 50

stimulus = Stimulus(background_color = "white")

stimulus.positions   = Positions.Create2DGrid(n_rows, n_cols, row_spacing, col_spacing, x_offset, y_offset)
stimulus.shapes      = patterns.BasicPattern([shapes.Rectangle]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.size        = patterns.BasicPattern([20]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.colour      = patterns.GridRepeater(["red", "green", "blue"], n_rows, n_cols).RepeatPatternInCheckerboard()
stimulus.orientation = patterns.SymmetryPattern([0], n_rows, n_cols).MirrorAcrossColumns()
stimulus.data        = patterns.BasicPattern(["none"]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.Render()
stimulus.Show()
#stimulus.SaveJSON(r'output/test_stimulus')
#stimulus.SaveSVG(r'output/test_stimulus')


#%%

### OUTWARD-INWARD PATTERN - EVEN NUMBER OF ROWS AND COLUMNS ###
n_rows = 6
n_cols = 6

row_spacing = 50
col_spacing = 50

x_offset = 50
y_offset = 50

stimulus = Stimulus(background_color = "white")

stimulus.positions   = Positions.Create2DGrid(n_rows, n_cols, row_spacing, col_spacing, x_offset, y_offset)
stimulus.shapes      = patterns.BasicPattern([shapes.Rectangle]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.size        = patterns.BasicPattern([20]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.colour      = patterns.GridRepeater(["red", "green", "blue"], n_rows, n_cols).RepeatAcrossOutIn()
stimulus.orientation = patterns.SymmetryPattern([0], n_rows, n_cols).MirrorAcrossColumns()
stimulus.data        = patterns.BasicPattern(["none"]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.Render()
stimulus.Show()
#stimulus.SaveJSON(r'output/test_stimulus')
#stimulus.SaveSVG(r'output/test_stimulus')

#%%

### OUTWARD-INWARD PATTERN - ODD NUMBER OF ROWS AND COLUMNS ###
n_rows = 7
n_cols = 7

row_spacing = 50
col_spacing = 50

x_offset = 50
y_offset = 50

stimulus = Stimulus(background_color = "white")

stimulus.positions   = Positions.Create2DGrid(n_rows, n_cols, row_spacing, col_spacing, x_offset, y_offset)
stimulus.shapes      = patterns.BasicPattern([shapes.Rectangle]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.size        = patterns.BasicPattern([20]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.colour      = patterns.GridRepeater(["red", "green", "blue"], n_rows, n_cols).RepeatAcrossOutIn()
stimulus.orientation = patterns.SymmetryPattern([0], n_rows, n_cols).MirrorAcrossColumns()
stimulus.data        = patterns.BasicPattern(["none"]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.Render()
stimulus.Show()
#stimulus.SaveJSON(r'output/test_stimulus')
#stimulus.SaveSVG(r'output/test_stimulus')