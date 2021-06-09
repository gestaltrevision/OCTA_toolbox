# -*- coding: utf-8 -*-
"""
OCTA toolbox: demo stimulus orientation
"""
from octa.Stimulus import Grid, Stimulus
from octa.Positions import Positions
from octa.patterns import GridPattern, Pattern, Sequence, LinearGradient
from octa.shapes import Ellipse, Rectangle, Triangle, Image, FitImage, Text, Polygon, RegularPolygon, Path, PathSvg, ChangingEllipse
from octa.measurements import Complexity
import random


#%%

## Choose number of rows and number of columns
n_rows = 6
n_cols = 6

stimsize = (350,350)

clipshape = Ellipse(position = (stimsize[0]/2,stimsize[1]/2), bounding_box = stimsize)

stimulus = Grid(n_rows, n_cols, background_color = "lightgrey", stim_orientation = 30, row_spacing = 40, col_spacing = 40, size = stimsize, background_shape = clipshape)

## Determine shapes used in the stimulus
## Example shapes: Ellipse, Rectangle, Triangle, Polygon(n_sides = 8), ...
stimulus.shapes = GridPattern.RepeatAcrossColumns([Rectangle, Triangle, Ellipse])

## Determine colors used in the stimulus
colors_to_use = ['#1b9fd8', '#6dd6ff', '#006ca1'] 
stimulus.fillcolors = GridPattern.RepeatAcrossColumns(colors_to_use)

## Determine size of elements in the stimulus
stimulus.bounding_boxes = GridPattern.RepeatAcrossColumns([(30,30)])


stimulus.Show()
stimulus.SaveSVG("testori")

#%%

## Choose number of rows and number of columns
n_rows = 6
n_cols = 6

stimulus = Grid(n_rows, n_cols, background_color = "lightgrey", stim_orientation = 30, row_spacing = 40, col_spacing = 40, size = (350,350))

## Determine shapes used in the stimulus
## Example shapes: Ellipse, Rectangle, Triangle, Polygon(n_sides = 8), ...
stimulus.shapes = GridPattern.RepeatAcrossColumns([Rectangle, Triangle, Ellipse])

## Determine colors used in the stimulus
colors_to_use = ['#1b9fd8', '#6dd6ff', '#006ca1'] 
stimulus.fillcolors = GridPattern.RepeatAcrossColumns(colors_to_use)

## Determine size of elements in the stimulus
stimulus.bounding_boxes = GridPattern.RepeatAcrossColumns([(30,30)])


stimulus.Show()
stimulus.SaveSVG("testori2")