# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 12:31:15 2020

@author: Christophe
"""
from octa.Stimulus import Stimulus
from octa.Positions import Positions
from octa import shapes, patterns

### CURVE ###

n_rows = 6
n_cols = 6

row_spacing = 40
col_spacing = 40

x_offset = 50
y_offset = 50

stimulus = Stimulus(background_color = "white")

stimulus.positions   = Positions.Create2DGrid(n_rows, n_cols, row_spacing, col_spacing, x_offset, y_offset)
stimulus.shapes      = patterns.BasicPattern([shapes.Curve, shapes.Ellipse]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.size        = patterns.BasicPattern([20, 20]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.colour      = patterns.GridRepeater(["red", "green", "blue"], n_rows, n_cols).RepeatAcrossColumns()
stimulus.orientation = patterns.SymmetryPattern([0,12,45], n_rows, n_cols).MirrorAcrossColumns()
stimulus.data        = patterns.BasicPattern(["none"]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.Render()
stimulus.Show()
#stimulus.SaveJSON(r'output/test_stimulus')
#stimulus.SaveSVG(r'output/test_stimulus')

#%%

### DROPLET ###
n_rows = 6
n_cols = 6

row_spacing = 40
col_spacing = 40

x_offset = 50
y_offset = 50

stimulus = Stimulus(background_color = "white")

stimulus.positions   = Positions.Create2DGrid(n_rows, n_cols, row_spacing, col_spacing, x_offset, y_offset)
stimulus.shapes      = patterns.BasicPattern([shapes.Droplet]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.size        = patterns.BasicPattern([20]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.colour      = patterns.GridRepeater(["red", "green", "blue"], n_rows, n_cols).RepeatAcrossColumns()
stimulus.orientation = patterns.SymmetryPattern([0], n_rows, n_cols).MirrorAcrossColumns()
stimulus.data        = patterns.BasicPattern(["none"]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.Render()
stimulus.Show()
#stimulus.SaveJSON(r'output/test_stimulus')
#stimulus.SaveSVG(r'output/test_stimulus')

#%%

### FLOWERLEAVE ###
n_rows = 6
n_cols = 6

row_spacing = 40
col_spacing = 40

x_offset = 50
y_offset = 50

stimulus = Stimulus(background_color = "white")

stimulus.positions   = Positions.Create2DGrid(n_rows, n_cols, row_spacing, col_spacing, x_offset, y_offset)
stimulus.shapes      = patterns.BasicPattern([shapes.FlowerLeave, shapes.Ellipse]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.size        = patterns.BasicPattern([20, 20]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.colour      = patterns.GridRepeater(["red", "green", "blue"], n_rows, n_cols).RepeatAcrossColumns()
stimulus.orientation = patterns.SymmetryPattern([0,12,45], n_rows, n_cols).MirrorAcrossColumns()
stimulus.data        = patterns.BasicPattern(["none"]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.Render()
stimulus.Show()
#stimulus.SaveJSON(r'output/test_stimulus')
#stimulus.SaveSVG(r'output/test_stimulus')


#%%

### INFINITY ###
n_rows = 6
n_cols = 6

row_spacing = 40
col_spacing = 40

x_offset = 50
y_offset = 50

stimulus = Stimulus(background_color = "white")

stimulus.positions   = Positions.Create2DGrid(n_rows, n_cols, row_spacing, col_spacing, x_offset, y_offset)
stimulus.shapes      = patterns.BasicPattern([shapes.Infinity, shapes.Ellipse]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.size        = patterns.BasicPattern([20, 20]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.colour      = patterns.GridRepeater(["red", "green", "blue"], n_rows, n_cols).RepeatAcrossColumns()
stimulus.orientation = patterns.SymmetryPattern([0,12,45], n_rows, n_cols).MirrorAcrossColumns()
stimulus.data        = patterns.BasicPattern(["none"]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.Render()
stimulus.Show()
#stimulus.SaveJSON(r'output/test_stimulus')
#stimulus.SaveSVG(r'output/test_stimulus')

#%%

### TEXT ###
n_rows = 6
n_cols = 6

row_spacing = 40
col_spacing = 40

x_offset = 50
y_offset = 50

stimulus = Stimulus(background_color = "white")

stimulus.positions   = Positions.Create2DGrid(n_rows, n_cols, row_spacing, col_spacing, x_offset, y_offset)
stimulus.shapes      = patterns.BasicPattern([shapes.Text, shapes.Ellipse]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.size        = patterns.BasicPattern([50, 20]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.colour      = patterns.GridRepeater(["red", "green", "blue"], n_rows, n_cols).RepeatAcrossColumns()
stimulus.orientation = patterns.SymmetryPattern([0], n_rows, n_cols).MirrorAcrossColumns()
stimulus.data        = patterns.BasicPattern(["octa"]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.Render()
stimulus.Show()
#stimulus.SaveJSON(r'output/test_stimulus')
#stimulus.SaveSVG(r'output/test_stimulus')

#%%

### IMAGE ###
n_rows = 6
n_cols = 6

row_spacing = 40
col_spacing = 40

x_offset = 50
y_offset = 50

stimulus = Stimulus(background_color = "white")
#image_loc = r"C:\Users\u0090621\Downloads\kisspng-bird-cartoon-clip-art-birds-5ab38ad5633e37.2425937115217159254065.png"
#image_loc = r"C:\Users\u0090621\Downloads\bird.svg"
#image_loc = r"C:\Users\u0090621\Downloads\animated-bird.jpg"

stimulus.positions   = Positions.Create2DGrid(n_rows, n_cols, row_spacing, col_spacing, x_offset, y_offset)
stimulus.shapes      = patterns.BasicPattern([shapes.Image, shapes.Ellipse]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.size        = patterns.BasicPattern([50, 20]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.colour      = patterns.GridRepeater(["red", "green", "blue"], n_rows, n_cols).RepeatAcrossColumns()
stimulus.orientation = patterns.SymmetryPattern([0,12,45], n_rows, n_cols).MirrorAcrossColumns()
stimulus.data        = patterns.BasicPattern([image_loc]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.Render()
stimulus.Show()
#stimulus.SaveJSON(r'output/test_stimulus')
#stimulus.SaveSVG(r'output/test_stimulus')