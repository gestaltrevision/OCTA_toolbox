"""
OCTA toolbox: demo
"""
from octa.Stimulus import Grid
from octa.patterns import GridPattern
from octa.shapes import Ellipse, Rectangle, Triangle

## Create new stimulus
stim = Grid(n_rows = 6, n_cols = 6, background_color = "none",
            row_spacing = 40, col_spacing = 40)

## Determine shape of elements used in the stimulus
stim.shapes = GridPattern.RepeatAcrossColumns([Rectangle, Triangle, Ellipse])

## Determine color of elements used in the stimulus
colors_to_use = ["#1b9fd8", "#6dd6ff", "#006ca1"]
stim.fillcolors = GridPattern.RepeatAcrossColumns(colors_to_use)

## Determine size of elements used in the stimulus
stim.boundingboxes = GridPattern.RepeatAcrossColumns([(30,30)])

stim.Show()


