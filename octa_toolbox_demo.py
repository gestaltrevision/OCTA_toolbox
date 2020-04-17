# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 12:31:15 2020

@author: Christophe
"""

from Stimulus import Stimulus
from Positions import Positions
from BasicPattern import BasicPattern
from RepeaterPattern import GridRepeater
from Circle import Circle
from Square import Square

n_rows = 5
n_cols = 5

row_spacing = 40
col_spacing = 40

stimulus = Stimulus()
#stimulus = Stimulus(background_color = "green")

stimulus.positions = Positions.Create2DGrid(n_rows, n_cols, row_spacing, col_spacing)
stimulus.shapes    = BasicPattern([Circle, Square]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.radii     = BasicPattern([10, 20]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.colour    = GridRepeater(["red", "blue", 'yellow'], n_rows, n_cols).RepeatAcrossLeftDiagonal()

stimulus.Render()
stimulus.Show()
#stimulus.CreateJSON()
#stimulus.Save("test")