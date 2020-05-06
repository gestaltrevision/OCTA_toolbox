# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 12:31:15 2020

@author: Christophe
"""


from octa.Stimulus import Stimulus
from octa.Positions import Positions
from octa import shapes, patterns

n_rows = 2
n_cols = 4

row_spacing = 50
col_spacing = 50

x_offset = 50
y_offset = 50

stimulus = Stimulus(background_color = "white")

#stimulus.positions   = Positions.Create2DGrid(n_rows, n_cols, row_spacing, col_spacing, x_offset, y_offset)
#stimulus.positions   = Positions.CreateSineGrid(n_rows, n_cols, row_spacing, col_spacing, x_offset, y_offset, A = 30, f = 1/5)
stimulus.positions   = Positions.CreateCircle(radius = 100, n_elements = 8, x_offset = 150, y_offset = 150)
stimulus.shapes      = BasicPattern([Rectangle]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.size        = BasicPattern([25]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.colour      = GridGradient("red", "green", n_rows, n_cols).GradientAcrossRightDiagonal()
stimulus.orientation = SymmetryPattern([0], n_rows, n_cols).MirrorAcrossColumns()
stimulus.Render()
stimulus.Show()
#stimulus.SaveJSON('test_stimulus')
#stimulus.SaveSVG('test_stimulus')

#%%
#stim_2 = Stimulus.LoadFromJSON("test_stimulus.json")
#stim_2.Render()
#stim_2.Show()
