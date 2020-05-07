# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 12:31:15 2020

@author: Christophe
"""


from octa.Stimulus import Stimulus
from octa.Positions import Positions
from octa import shapes, patterns


n_rows = 6
n_cols = 6


row_spacing = 60
col_spacing = 60

x_offset = 50
y_offset = 50

image_loc = r"C:\Users\Christophe\Desktop\todo\OCTA_toolbox\output\beautiful_birds_6.jpg"
stimulus = Stimulus(background_color = "white")


stimulus.positions   = Positions.Create2DGrid(n_rows, n_cols, row_spacing, col_spacing, x_offset, y_offset)
stimulus.positions.JitterLocations(axis = "x", mu = 0, std = 10)
stimulus.positions.JitterLocations(axis = "y", distribution = "uniform", min_val = 0, max_val = 20)

stimulus.shapes      = patterns.BasicPattern([shapes.Image, shapes.Rectangle]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.size        = patterns.GridRepeater([30, 50], n_rows, n_cols, patterns.Style.AcrossColumns)
stimulus.colour      = patterns.GridGradient("red", "green", n_rows, n_cols).GradientAcrossRightDiagonal()
stimulus.orientation = patterns.SymmetryPattern([0], n_rows, n_cols, patterns.Style.AcrossRows)
stimulus.data        = patterns.BasicPattern(image_loc).DuplicatePatternToSize(n_rows * n_cols)
stimulus.Render()
stimulus.Show()
#stimulus.SaveJSON(r'output/test_stimulus')
#stimulus.SaveSVG(r'output/test_stimulus')

#%%
# stim_2 = Stimulus.LoadFromJSON(r"output/test_stimulus.json")
# stim_2.Render()
# stim_2.Show()


#stimulus.SaveJSON('test_stimulus')
#stimulus.SaveSVG('test_stimulus')

#%%
#stim_2 = Stimulus.LoadFromJSON("test_stimulus.json")
#stim_2.Render()
#stim_2.Show()

