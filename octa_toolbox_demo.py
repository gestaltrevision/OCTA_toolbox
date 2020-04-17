# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 12:31:15 2020

@author: Christophe
"""

from Stimulus import Stimulus
from Positions import Positions
from BasicPattern import BasicPattern
from RepeaterPattern import GridRepeater
from GradientPattern import GridGradient
from SymmetryPattern import SymmetryPattern
from Ellipse import Ellipse
from Rectangle import Rectangle
from Triangle import Triangle

n_rows = 10
n_cols = 10

row_spacing = 50
col_spacing = 50

stimulus = Stimulus(background_color = "white")

stimulus.positions   = Positions.Create2DGrid(n_rows, n_cols, row_spacing, col_spacing)
stimulus.shapes      = BasicPattern([Triangle, Rectangle]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.size        = BasicPattern([20, (10, 40)]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.colour      = GridGradient("red", "green", n_rows, n_cols).GradientAcrossRightDiagonal()
stimulus.orientation = SymmetryPattern([0,12,45], n_rows, n_cols).MirrorAcrossColumns()
stimulus.Render()
stimulus.Show()
stimulus.SaveJSON('test_stimulus')

#%%
stim_2 = Stimulus.LoadFromJSON("test_stimulus.json")
stim_2.Render()
stim_2.Show()