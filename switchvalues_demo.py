from Stimulus import Stimulus
from Positions import Positions
from BasicPattern import BasicPattern
from RepeaterPattern import GridRepeater
from GradientPattern import GridGradient
from SymmetryPattern import SymmetryPattern
from Ellipse import Ellipse
from Rectangle import Rectangle
from Triangle import Triangle

### STANDARD PATTERN ###

n_rows = 5
n_cols = 5

row_spacing = 50
col_spacing = 50

stimulus = Stimulus(background_color = "white")

stimulus.positions   = Positions.Create2DGrid(n_rows, n_cols, row_spacing, col_spacing, x_offset = 50, y_offset = 50)
stimulus.shapes      = BasicPattern([Rectangle, Rectangle]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.size        = BasicPattern([(30,30), (20, 20)]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.colour      = GridRepeater(["red", "blue"], n_rows, n_cols).RepeatElements()
stimulus.orientation = SymmetryPattern([0], n_rows, n_cols).MirrorAcrossColumns()

stimulus.Render()
stimulus.Show()

#%%
### SIZE SWITCHES ###
stimulus.positions   = Positions.Create2DGrid(n_rows, n_cols, row_spacing, col_spacing, x_offset = 50, y_offset = 50)
stimulus.shapes      = BasicPattern([Ellipse, Triangle, Rectangle]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.colour      = GridRepeater(["red", "blue"], n_rows, n_cols).RepeatElements()
stimulus.orientation = SymmetryPattern([0], n_rows, n_cols).MirrorAcrossColumns()

stimulus.size        = BasicPattern([(10,10), (20,20), (20,20)]).DuplicatePatternToSize(n_rows * n_cols).SwitchValues(n_switches = 1)
stimulus.Render()
stimulus.Show()

#%%
### COLOR SWITCHES ###
stimulus.positions   = Positions.Create2DGrid(n_rows, n_cols, row_spacing, col_spacing, x_offset = 50, y_offset = 50)
stimulus.shapes      = BasicPattern([Rectangle, Rectangle]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.size        = BasicPattern([(30,30), (20, 20)]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.orientation = SymmetryPattern([0], n_rows, n_cols).MirrorAcrossColumns()

stimulus.colour      = GridRepeater(["red", "blue"], n_rows, n_cols).RepeatAcrossRows().SwitchValues(n_switches = 1)
stimulus.Render()
stimulus.Show()

#%%
### ORIENTATION SWITCHES ###
stimulus.positions   = Positions.Create2DGrid(n_rows, n_cols, row_spacing, col_spacing, x_offset = 50, y_offset = 50)
stimulus.shapes      = BasicPattern([Rectangle, Rectangle]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.size        = BasicPattern([(30,30), (20, 20)]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.colour      = GridRepeater(["red", "blue"], n_rows, n_cols).RepeatAcrossRows()

stimulus.orientation = SymmetryPattern([0, 45], n_rows, n_cols).MirrorAcrossColumns().SwitchValues(n_switches = 2)

stimulus.Render()
stimulus.Show()

#%%
### SWITCHES: ERROR WHEN TOO MANY SWITCHES ASKED FOR ###
stimulus.positions   = Positions.Create2DGrid(n_rows, n_cols, row_spacing, col_spacing, x_offset = 50, y_offset = 50)
stimulus.shapes      = BasicPattern([Rectangle, Rectangle]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.size        = BasicPattern([(30,30), (20, 20)]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.orientation = SymmetryPattern([0], n_rows, n_cols).MirrorAcrossColumns()

#stimulus.colour      = GridRepeater(["red", "blue"], n_rows, n_cols).RepeatElements().SwitchValues(n_switches = 13)
stimulus.colour      = GridRepeater(["red", "blue"], n_rows, n_cols).RepeatAcrossRows().SwitchValues(n_switches = 15)

stimulus.Render()
stimulus.Show()

#%%
### SWITCHES: ERROR WHEN TOO FEW GROUPS OF VALUES IN FEATURE ###
stimulus.positions   = Positions.Create2DGrid(n_rows, n_cols, row_spacing, col_spacing, x_offset = 50, y_offset = 50)
stimulus.shapes      = BasicPattern([Rectangle, Rectangle]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.size        = BasicPattern([(30,30), (20, 20)]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.orientation = SymmetryPattern([0], n_rows, n_cols).MirrorAcrossColumns()

stimulus.colour      = GridRepeater(["red"], n_rows, n_cols).RepeatAcrossRows().SwitchValues(n_switches = 1)

stimulus.Render()
stimulus.Show()






















