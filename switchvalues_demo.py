from octa.Stimulus import Stimulus
from octa.Positions import Positions
from octa import shapes, patterns

### STANDARD PATTERN ###

n_rows = 5
n_cols = 5

row_spacing = 50
col_spacing = 50

stimulus = Stimulus(background_color = "white")

stimulus.positions   = Positions.Create2DGrid(n_rows, n_cols, row_spacing, col_spacing, x_offset = 50, y_offset = 50)
stimulus.shapes      = patterns.BasicPattern([shapes.Rectangle, shapes.Rectangle]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.size        = patterns.BasicPattern([(30,30), (20, 20)]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.colour      = patterns.GridRepeater(["red", "blue"], n_rows, n_cols).RepeatElements()
stimulus.orientation = patterns.SymmetryPattern([0], n_rows, n_cols).MirrorAcrossColumns()
stimulus.data        = patterns.BasicPattern(["none"]).DuplicatePatternToSize(n_rows * n_cols)

stimulus.Render()
stimulus.Show()

#%%
### ELEMENT SWITCHES ###
stimulus.positions   = Positions.Create2DGrid(n_rows, n_cols, row_spacing, col_spacing, x_offset = 50, y_offset = 50)
stimulus.shapes      = patterns.BasicPattern([shapes.Ellipse, shapes.Rectangle]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.colour      = patterns.GridRepeater(["red", "blue"], n_rows, n_cols).RepeatElements()
stimulus.orientation = patterns.SymmetryPattern([0,90], n_rows, n_cols).MirrorAcrossColumns()
stimulus.size        = patterns.BasicPattern([(10,10), (20,20)]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.data        = patterns.BasicPattern(["none"]).DuplicatePatternToSize(n_rows * n_cols)

stimulus             = stimulus.SwitchElements(n_switches = 1)

stimulus.Render()
stimulus.Show()

#%%
### SIZE SWITCHES ###
stimulus.positions   = Positions.Create2DGrid(n_rows, n_cols, row_spacing, col_spacing, x_offset = 50, y_offset = 50)
stimulus.shapes      = patterns.BasicPattern([shapes.Ellipse, shapes.Triangle, shapes.Rectangle]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.colour      = patterns.GridRepeater(["red", "blue"], n_rows, n_cols).RepeatElements()
stimulus.orientation = patterns.SymmetryPattern([0], n_rows, n_cols).MirrorAcrossColumns()
stimulus.data        = patterns.BasicPattern(["none"]).DuplicatePatternToSize(n_rows * n_cols)

stimulus.size        = patterns.BasicPattern([(10,10), (20,20), (20,20)]).DuplicatePatternToSize(n_rows * n_cols).SwitchValues(n_switches = 1)
stimulus.Render()
stimulus.Show()

#%%
### COLOR SWITCHES ###
stimulus.positions   = Positions.Create2DGrid(n_rows, n_cols, row_spacing, col_spacing, x_offset = 50, y_offset = 50)
stimulus.shapes      = patterns.BasicPattern([shapes.Rectangle, shapes.Rectangle]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.size        = patterns.BasicPattern([(30,30), (20, 20)]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.orientation = patterns.SymmetryPattern([0], n_rows, n_cols).MirrorAcrossColumns()
stimulus.data        = patterns.BasicPattern(["none"]).DuplicatePatternToSize(n_rows * n_cols)

stimulus.colour      = patterns.GridRepeater(["red", "blue"], n_rows, n_cols).RepeatAcrossRows().SwitchValues(n_switches = 1)
stimulus.Render()
stimulus.Show()

#%%
### ORIENTATION SWITCHES ###
stimulus.positions   = Positions.Create2DGrid(n_rows, n_cols, row_spacing, col_spacing, x_offset = 50, y_offset = 50)
stimulus.shapes      = patterns.BasicPattern([shapes.Rectangle, shapes.Rectangle]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.size        = patterns.BasicPattern([(30,30), (20, 20)]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.colour      = patterns.GridRepeater(["red", "blue"], n_rows, n_cols).RepeatAcrossRows()
stimulus.data        = patterns.BasicPattern(["none"]).DuplicatePatternToSize(n_rows * n_cols)

stimulus.orientation = patterns.SymmetryPattern([0, 45], n_rows, n_cols).MirrorAcrossColumns().SwitchValues(n_switches = 2)

stimulus.Render()
stimulus.Show()

#%%
### SWITCHES: ERROR WHEN TOO MANY SWITCHES ASKED FOR ###
stimulus.positions   = Positions.Create2DGrid(n_rows, n_cols, row_spacing, col_spacing, x_offset = 50, y_offset = 50)
stimulus.shapes      = patterns.BasicPattern([shapes.Rectangle, shapes.Rectangle]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.size        = patterns.BasicPattern([(30,30), (20, 20)]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.orientation = patterns.SymmetryPattern([0], n_rows, n_cols).MirrorAcrossColumns()
stimulus.data        = patterns.BasicPattern(["none"]).DuplicatePatternToSize(n_rows * n_cols)

#stimulus.colour      = GridRepeater(["red", "blue"], n_rows, n_cols).RepeatElements().SwitchValues(n_switches = 13)
stimulus.colour      = patterns.GridRepeater(["red", "blue"], n_rows, n_cols).RepeatAcrossRows().SwitchValues(n_switches = 15)

stimulus.Render()
stimulus.Show()

#%%
### SWITCHES: ERROR WHEN TOO FEW GROUPS OF VALUES IN FEATURE ###
stimulus.positions   = Positions.Create2DGrid(n_rows, n_cols, row_spacing, col_spacing, x_offset = 50, y_offset = 50)
stimulus.shapes      = patterns.BasicPattern([shapes.Rectangle, shapes.Rectangle]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.size        = patterns.BasicPattern([(30,30), (20, 20)]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.orientation = patterns.SymmetryPattern([0], n_rows, n_cols).MirrorAcrossColumns()
stimulus.data        = patterns.BasicPattern(["none"]).DuplicatePatternToSize(n_rows * n_cols)

stimulus.colour      = patterns.GridRepeater(["red"], n_rows, n_cols).RepeatAcrossRows().SwitchValues(n_switches = 1)

stimulus.Render()
stimulus.Show()






















